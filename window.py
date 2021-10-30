from tkinter import *
import CyberTrone as combo
import Surveillance_mode as surveillance
import Face_recognition_mode as face_recog
import Face_tracking_mode as face_track
import obj_dectection_mode as obj_detect
import Text_detector_mode as txt_detector
from Database_Module import *

window = Tk()

window.geometry("900x700")
window.configure(bg="#ffffff")
canvas = Canvas(window, bg="#ffffff", height=700, width=900, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

img0 = PhotoImage(file=f"Resources/UI Icons/img0.png")
b0 = Button(image=img0, borderwidth=0, highlightthickness=0, command=txt_detector.main, relief="flat")

b0.place(x=515, y=345, width=191, height=63)

img1 = PhotoImage(file=f"Resources/UI Icons/img1.png")
b1 = Button(image=img1, borderwidth=0, highlightthickness=0, command=combo.main, relief="flat")

b1.place(x=152, y=155, width=191, height=63)

img2 = PhotoImage(file=f"Resources/UI Icons/img2.png")
b2 = Button(image=img2, borderwidth=0, highlightthickness=0, command=Save_data, relief="flat")

b2.place(x=152, y=512, width=191, height=63)

img3 = PhotoImage(file=f"Resources/UI Icons/img3.png")
b3 = Button(image=img3, borderwidth=0, highlightthickness=0, command=fetch_data, relief="flat")

b3.place(x=515, y=512, width=191, height=63)

img4 = PhotoImage(file=f"Resources/UI Icons/img4.png")
b4 = Button(image=img4, borderwidth=0, highlightthickness=0, command=face_track, relief="flat")

b4.place(x=152, y=250, width=191, height=63)

img5 = PhotoImage(file=f"Resources/UI Icons/img5.png")
b5 = Button(image=img5, borderwidth=0, highlightthickness=0, command=obj_detect.main, relief="flat")

b5.place(x=152, y=345, width=191, height=63)

img6 = PhotoImage(file = f"Resources/UI Icons/img6.png")
b6 = Button(image=img6, borderwidth=0, highlightthickness=0, command=surveillance.main, relief="flat")

b6.place(x=515, y=155, width=191, height=63)

img7 = PhotoImage(file=f"Resources/UI Icons/img7.png")
b7 = Button(image=img7, borderwidth=0, highlightthickness=0, command=face_recog.main, relief="flat")

b7.place(x=515, y=250, width=191, height=63)

background_img = PhotoImage(file=f"Resources/UI Icons/background.png")
background = canvas.create_image(450.0, 247.0, image=background_img)

window.resizable(False, False)
window.mainloop()
