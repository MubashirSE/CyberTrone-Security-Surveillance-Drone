from djitellopy import Tello
import cv2
import numpy as np
import time
from datetime import datetime
import os
import argparse
from HandTrackingModule import HandDetector
from Saving_Record_Module import Text_detection


# standard argparse stuff
parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter, add_help=False)
parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                    help='** = required')
parser.add_argument('-d', '--distance', type=int, default=3,
                    help='use -d to change the distance of the drone. Range 0-6')
parser.add_argument('-sx', '--saftey_x', type=int, default=100,
                    help='use -sx to change the saftey bound on the x axis . Range 0-480')
parser.add_argument('-sy', '--saftey_y', type=int, default=55,
                    help='use -sy to change the saftey bound on the y axis . Range 0-360')
parser.add_argument('-os', '--override_speed', type=int, default=1,
                    help='use -os to change override speed. Range 0-3')
parser.add_argument('-ss', "--save_session", action='store_true',
                    help='add the -ss flag to save your session as an image sequence in the Sessions folder')
parser.add_argument('-D', "--debug", action='store_true',
                    help='add the -D flag to enable debug mode. Everything works the same, but no commands will be sent to the drone')

args = parser.parse_args()

# Speed of the drone
S = 20
S2 = 5
UDOffset = 150


# These are the values in which kicks in speed up mode, as of now, this hasn't been finalized or fine tuned so be careful
# Tested are 3, 4, 5
acc = [500, 250, 250, 150, 110, 70, 50]

# Frames per second of the pygame window display
FPS = 25
dimensions = (960, 720)

##### FOR  Hand Detection
detector = HandDetector(detectionCon=0.8, maxHands=2)
####################################################################################

# If we are to save our sessions, we need to make sure the proper directories exist
if args.save_session:
    ddir = "D:\All Laptop Data\TelloTV-master\Sessions"

    if not os.path.isdir(ddir):
        os.mkdir(ddir)

    ddir = "D:\All Laptop Data\TelloTV-master\Sessions\Session {}".format(
        str(datetime.datetime.now()).replace(':', '-').replace('.', '_'))
    os.mkdir(ddir)


class FrontEnd(object):

    def __init__(self):
        # Init Tello object that interacts with the Tello drone
        self.tello = Tello()

        # Drone velocities between -100~100
        self.for_back_velocity = 0
        self.left_right_velocity = 0
        self.up_down_velocity = 0
        self.yaw_velocity = 0
        self.speed = 10

        self.send_rc_control = False

    def run(self):

        if not self.tello.connect():
            print("Tello not connected")
            return

        if not self.tello.set_speed(self.speed):
            print("Not set speed to lowest possible")
            return

        # In case streaming is on. This happens when we quit this program without the escape key.
        if not self.tello.streamoff():
            print("Could not stop video stream")
            return

        if not self.tello.streamon():
            print("Could not start video stream")
            return

        frame_read = self.tello.get_frame_read()

        should_stop = False
        imgCount = 0
        OVERRIDE = False

        oSpeed = args.override_speed
        self.tello.get_battery()

        if args.debug:
            print("DEBUG MODE ENABLED!")

        while not should_stop:
            self.update()

            if frame_read.stopped:
                frame_read.stop()
                break

            theTime = str(datetime.now()).replace(':', '-').replace('.', '_')

            frame = cv2.cvtColor(frame_read.frame, cv2.COLOR_BGR2RGB)
            frameRet = frame_read.frame

            vid = self.tello.get_video_capture()

            if args.save_session:
                cv2.imwrite("{}/tellocap{}.jpg".format(ddir, imgCount), frameRet)

            frame = np.rot90(frame)
            imgCount += 1

            time.sleep(1 / FPS)

            # Listen for key presses
            k = cv2.waitKey(20)

            # Press 1 to set distance to 1
            if k == ord('1'):
                if OVERRIDE:
                    oSpeed = 1

            # Press 2 to set distance to 2
            if k == ord('2'):
                if OVERRIDE:
                    oSpeed = 2

            # Press 3 to set distance to 3
            if k == ord('3'):
                if OVERRIDE:
                    oSpeed = 3

            # Press T to take off
            if k == ord('t'):
                if not args.debug:
                    print("Taking Off")
                    self.tello.takeoff()
                    self.tello.get_battery()

                self.send_rc_control = True

            # Press L to land
            if k == ord('l'):
                if not args.debug:
                    print("Landing")
                    self.tello.land()
                self.send_rc_control = False

            # Press Backspace for controls override
            if k == 8:
                if not OVERRIDE:
                    OVERRIDE = True
                    print("OVERRIDE ENABLED")
                else:
                    OVERRIDE = False
                    print("OVERRIDE DISABLED")

            if OVERRIDE:
                Text_detection(frameRet)

                # S & W to fly forward & back
                if k == ord('w'):
                    self.for_back_velocity = int(S * oSpeed)
                elif k == ord('s'):
                    self.for_back_velocity = -int(S * oSpeed)
                else:
                    self.for_back_velocity = 0

                # a & d to pan left & right
                if k == ord('a'):
                    self.yaw_velocity = int(S * oSpeed)
                elif k == ord('d'):
                    self.yaw_velocity = -int(S * oSpeed)
                else:
                    self.yaw_velocity = 0

                # Q & E to fly up & down
                if k == ord('q'):
                    self.up_down_velocity = int(S * oSpeed)
                elif k == ord('e'):
                    self.up_down_velocity = -int(S * oSpeed)
                else:
                    self.up_down_velocity = 0

                # c & z to fly left & right
                if k == ord('z'):
                    self.left_right_velocity = int(S * oSpeed)
                elif k == ord('c'):
                    self.left_right_velocity = -int(S * oSpeed)
                else:
                    self.left_right_velocity = 0

            # Quit the software
            if k == 27:
                should_stop = True
                break

            if OVERRIDE:
                show = "Text Detector Mode: Drone_Speed: {}".format(oSpeed)
                #dCol = (255, 255, 255)
            else:
                show = "Text Detector: Disabled"

            # Draw the distance choosen
            cv2.putText(frameRet, show, (32, 664), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

            # Display the resulting frame
            cv2.imshow(f'Tello Tracking...', frameRet)

        # On exit, print the battery
        self.tello.get_battery()

        # When everything done, release the capture
        cv2.destroyAllWindows()

        # Call it always before finishing. I deallocate resources.
        #self.tello.end()

    def battery(self):
        return self.tello.get_battery()[:2]

    def update(self):
        """ Update routine. Send velocities to Tello."""
        if self.send_rc_control:
            self.tello.send_rc_control(self.left_right_velocity, self.for_back_velocity, self.up_down_velocity,
                                       self.yaw_velocity)


def lerp(a, b, c):
    return a + c * (b - a)


def main():
    frontend = FrontEnd()

    # run frontend
    frontend.run()