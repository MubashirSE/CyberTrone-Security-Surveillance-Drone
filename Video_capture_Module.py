import time
import cv2
from djitellopy import Tello
from threading import Thread

tello = Tello()
tello.connect()
keepRecording = True
tello.streamon()
frame_read = tello.get_frame_read()


def videoRecorder():
    height, width, _ = frame_read
    video = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

    while keepRecording:
        video.write(frame_read)
        time.sleep(1 / 30)

    video.release()


recorder = Thread(target=videoRecorder)
recorder.start()

tello.takeoff()
tello.land()

keepRecording = False
recorder.join()
