import numpy as np
from keras.models import load_model

class LttModule:
  def __init__(self):
    self.temp_axis = []
    self.temp_mean_x = 0
    self.temp_mean_y = 0
    self.max_length = 6
    self.model = load_model('/Users/yangdongjae/Desktop/2020/대외활동/SW_-hackathon/src/GazeTracking/ML_MODEL/classification_model.h5')

  def centerized(self, x, y):
    self.temp_axis.append((x, y))

    if len(self.temp_axis) < self.max_length:
      pass
    else:
      temp_total_x = 0
      temp_total_y = 0
      for i in range(self.max_length):
        for j in range(2):
          if j == 0:
            temp_total_x += self.temp_axis[i][j]
          elif j == 1:
            temp_total_y += self.temp_axis[i][j]
          else:
            pass
      del self.temp_axis[0]
      self.temp_mean_x = temp_total_x // self.max_length
      self.temp_mean_y = temp_total_y // self.max_length
    return (self.temp_mean_x, self.temp_mean_y)

  # def ltt_ratio_fit(self,ver_ratio , hor_ratio):
  #   result_list = []

  #   for i in range(len(ver_ratio)):
  #     data = np.array([[ver_ratio[i], hor_ratio[i]]])
  #   result_list.append(self.model.predict_classes(data))

  #   if result_list.count(1) >= 15:
  #     return True
  #   else:
  #     return False

  def ltt_ratio_fit(self, ver_ratio, hor_ratio):
    model_data = np.array([[ver_ratio, hor_ratio]])

    return self.model.predict_classes(model_data)

  def del_None_value(self, data_list):
    return_value = list()
    for i in data_list:
      if i is not None:
        return_value.append(i)
    return return_value


  # def get_mean(self, data_list):
  #   return_list = []

  #   for i in data_list:
  #     if i is not None:
  #       return_list.append(i)
  #   return(np.mean(return_list))
    