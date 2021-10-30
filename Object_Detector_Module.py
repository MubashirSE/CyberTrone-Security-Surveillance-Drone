import cv2
import cvzone
from djitellopy import Tello


#for Object Detection
classNames = []
classFile = 'Resources/coco.names'
with open(classFile, 'rt') as f:
        classNames = f.read().split('\n')


configPath = 'Resources/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightPath = 'Resources/frozen_inference_graph.pb'

thres = 0.6  # for Obejct Detection
nmsthres = 0.3  # for Obejct Detection

net = cv2.dnn_DetectionModel(weightPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)
#### Object Detection


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


def object_detection(frameRet):
    classIds, confs, bbox = net.detect(frameRet, confThreshold=thres, nmsThreshold=nmsthres)

    try:
        for classIds, conf, box in zip(classIds.flatten(), confs.flatten(), bbox):
            cvzone.cornerRect(frameRet, box)
            cv2.putText(frameRet, f'{classNames[classIds - 1].upper()} {round(conf * 100, 2)}',
                        (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 2)

    except:
        pass
