"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""
from keras.models import load_model
import math
import cv2
import numpy as np
import cheatah

gt = cheatah.GazeTracking()
hpe = cheatah.HeadPoseEstimation()
ft = cheatah.FaceTracking()

webcam = cv2.VideoCapture(0)

class Center:
    def __init__(self):
        self.temp_axis = []
        self.temp_mean_x = 0
        self.temp_mean_y = 0
        self.max_length = 6

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
    
    def fit_ltt_model(self, ver, hor):
        output = []
        for i in range(len(ver)):
            data = np.array([[ver[i], hor[i]]])
            data = np.array(data)
            output.append(model.predict_classes(data))
            if output.count(1) >= 15:
                return True
            else:
                return False
            
c = Center()

hor = []
ver = []
y = list()
l_pupil_x = []
l_pupil_y = []
r_pupil_x = []
r_pupil_y = []
x_test = list()
y_test = list()

model = load_model('/Users/yangdongjae/Desktop/2020/대외활동/SW_-hackathon/src/GazeTracking/ML_MODEL/classification_model.h5', compile=False)

while True:
    try: 
        # We get a new frame from the webcam
        _, frame = webcam.read()
        
        ft.refresh(frame, width, height)
        gt.refresh(frame, width, height)
        hpe.refresh(frame, width, height)
        # We send this frame to GazeTracking to analyze it
        gaze.refresh(frame)

        frame = gaze.annotated_frame()
        text = ""

        if gaze.is_blinking():
            text = "Blinking"
        elif gaze.is_right():
            text = "Looking right"
        elif gaze.is_left():
            text = "Looking left"
        elif gaze.is_center():
            text = "Looking center"
                        
        cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
                        
        left_pupil = gaze.pupil_left_coords()
        right_pupil = gaze.pupil_right_coords()
            
        horizontal_ratio = gaze.horizontal_ratio()
        vertical_ratio = gaze.vertical_ratio()
            
        mimicked_x = 0
        mimicked_y = 0
            
        if horizontal_ratio is not None and vertical_ratio is not None:
            mimicked_x = math.floor(640 * horizontal_ratio)
            mimicked_y = math.floor(480 * vertical_ratio)
            centerized_axis = c.centerized(mimicked_x, mimicked_y)

        else:
            pass

        cv2.putText(frame, "L pupil: " + str(left_pupil), (0, 130), cv2.FONT_HERSHEY_DUPLEX, 0.6, (147, 58, 31), 1)
        cv2.putText(frame, "R pupil: " + str(right_pupil), (0, 165), cv2.FONT_HERSHEY_DUPLEX, 0.6, (147, 58, 31), 1)

        cv2.putText(frame, "Hor    : " + str(horizontal_ratio), (0, 200), cv2.FONT_HERSHEY_DUPLEX, 0.6, (147, 58, 31), 1)
        cv2.putText(frame, "Ver    : " + str(vertical_ratio), (0, 235), cv2.FONT_HERSHEY_DUPLEX, 0.6, (147, 58, 31), 1)
        
        ver.append(vertical_ratio)
        hor.append(horizontal_ratio)
    #    if left_pupil is not None and right_pupil is not None:
    #        l_pupil_x.append(left_pupil[0])
    #        l_pupil_y.append(left_pupil[1])
    #        r_pupil_x.append(right_pupil[0])
    #        r_pupil_y.append(right_pupil[1])
    #    else:
    #        l_pupil_x.append(None)
    #        l_pupil_y.append(None)
    #        r_pupil_x.append(None)
    #        r_pupil_y.append(None)
    #    y.append(0)        
        x_point , y_point = gaze.get_landmakr()

        cheating_judge = gaze.detect_exist_face(x_point)
        print(cheating_judge)

        if cheating_judge == 1 :
            cv2.putText(frame, "Cheating", (90, 400), cv2.FONT_HERSHEY_DUPLEX, 2.0, (0, 0, 255), 3)
        elif cheating_judge == 2:
            cv2.putText(frame, "left your seat", (90, 400), cv2.FONT_HERSHEY_DUPLEX, 2.0, (0, 0, 255), 3)

        x_test.append(x_point)
        y_test.append(y_point)
        
        for i in range(len(ver)):
            data = np.array([[ver[i], hor[i]]])
        if model.predict_classes(data) == 1:
            cv2.putText(frame, "Warning", (90, 400), cv2.FONT_HERSHEY_DUPLEX, 2.0, (0, 0, 255), 3)
        else:
            pass
    #    pd.DataFrame({'ver':ver , 'hor' : hor , 'l_pupil_x' : l_pupil_x, 'l_pupil_y' : l_pupil_y, 'r_pupil_x' : r_pupil_x, 'r_pupil_y' : r_pupil_y, 'y' : y}).to_csv(r"C:\Users\sejon\Anaconda\Project\EyeTracking/PredictData5.csv")
    #    cv2.putText(frame, "+", centerized_axis, cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 255), 3)
        print(model.predict_classes(data))
        cv2.imshow("Demo", frame)
        if cv2.waitKey(1) == 27:
            break
    except KeyboardInterrupt:
        print(f"esc")
