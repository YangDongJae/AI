import csv
from pathlib import Path

path = Path('/Users/yangdongjae/Desktop/2020/대외활동/SW_-hackathon/data/test.csv')
f = path.open('r')
rdr = csv.reader(f)
rdr_matrix = []
for row in rdr:
    tmp_list = []
    for i in row:
        if i:
            try:
                tmp_list.append(eval(i))
            except:
                tmp_list.append(None)
        else:
            tmp_list.append(None)
    rdr_matrix.append(tmp_list)

del rdr_matrix[0]

while True:
    if rdr_matrix[0][1] is not None and rdr_matrix[0][2] is not None:
        break
    else:
        del rdr_matrix[0]

while True:
    if rdr_matrix[-1][1] is not None and rdr_matrix[-1][2] is not None:
        break
    else:
        del rdr_matrix[-1]

start_index = 0
end_index = 0
for i, row in enumerate(rdr_matrix):
    if row[1] is not None and row[2] is not None:
        if start_index == end_index:
            start_index = i
            end_index = i
        else:
            end_index = i
            blank_count = end_index - start_index
            delta_x1 = (rdr_matrix[end_index][1] - rdr_matrix[start_index][1]) / blank_count
            delta_x2 = (rdr_matrix[end_index][2] - rdr_matrix[start_index][2]) / blank_count
            for j in range(1, blank_count + 1):
                rdr_matrix[start_index + j][1] = rdr_matrix[start_index][1] + j * delta_x1
                rdr_matrix[start_index + j][2] = rdr_matrix[start_index][2] + j * delta_x2

            start_index = i
            end_index = i
    else:
        end_index = i

path = Path('data.out.csv')
with path.open('w', encoding="utf-8") as f:
    f.write(',ver,hor\n')
    for row in rdr_matrix:
        f.write(f'{row[0]},{row[1]},{row[2]}\n')

print('success')
