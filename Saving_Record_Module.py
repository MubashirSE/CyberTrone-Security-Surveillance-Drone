from datetime import datetime
import pytesseract
import cv2
import os
from djitellopy import Tello
import time
############### For Text_Detection ####################
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

############################################################


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


def Save_Records():
    path = 'Resources/detected_text_records/detected_images_text'
    images = []
    myList = os.listdir(path)
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)

    with open('Resources/detected_text_records/Records.csv', 'r+') as f:
        myDataList = f.readline()
        # print(myClassifier.list_labels)
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        for images in images:
            result = cv2.cvtColor(images, cv2.COLOR_BGR2RGB)
            # print(pytesseract.image_to_data(result))
            hImg, wImg, _ = result.shape
            boxes = pytesseract.image_to_data(result)
            # print(boxes)
            for x, b in enumerate(boxes.splitlines()):
                if x != 0:
                    b = b.split()
                    if len(b) == 12:
                        x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                        if b not in nameList:
                            now = datetime.now()
                            dtString = now.strftime('%H:%M:%S')
                            f.writelines(f'\n{b[11]},{dtString}')


def Text_detection(frameRet):
    frame = cv2.cvtColor(frameRet, cv2.COLOR_BGR2RGB)
    hImg, wImg, _ = frame.shape
    boxes = pytesseract.image_to_data(frame)
    for x, b in enumerate(boxes.splitlines()):
        if x != 0:
            b = b.split()
            if len(b) == 12:
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(frameRet, (x, y), (w + x, h + y), (0, 0, 255), 3)
                cv2.putText(frameRet, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)
                cv2.imwrite(f'Resources/detected_text_records/detected_images_text/{time.time()}.jpg', frameRet)
                #Save_Records()