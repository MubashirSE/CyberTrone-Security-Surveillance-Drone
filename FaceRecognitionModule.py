from djitellopy import Tello
import cv2
import time
import cvzone


# For Face Tracking
face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Facial_Recognition Classifier
myClassifier = cvzone.Classifier('Resources/keras_model.h5', 'Resources/labels.txt')


def IntializeTello():
    tello = Tello()
    tello.for_back_velocity = 0
    tello.left_right_velocity = 0
    tello.up_down_velocity = 0
    tello.yaw_velocity = 0
    tello.speed = 10
    return tello


def telloGetFrame(tello, w=360, h=240):
    frame_read = tello.get_frame_read()
    frame = cv2.cvtColor(frame_read.frame, cv2.COLOR_BGR2RGB)
    frameRet = frame_read.frame
    return frameRet


def Face_recognition(frameRet):
    gray = cv2.cvtColor(frameRet, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=2)
    for (x, y, w, h) in faces:
        # end coords are the end of the bounding box x & y
        end_cord_x = x + w
        end_cord_y = y + h
        end_size = w * 2
        cv2.rectangle(frameRet, (x, y), (end_cord_x, end_cord_y), (255, 0, 0), 2)
        predict = predictions, index = myClassifier.getPrediction(frameRet, pos=(x, y), scale=1, color=(0, 255, 0))
        if predict:
            cv2.imwrite(f'Resources/Recognized_Personel/{time.time()}.jpg', frameRet)
            time.sleep(0.3)
            #Save_Records()
        return predict
