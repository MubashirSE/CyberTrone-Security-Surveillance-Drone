import CyberTrone as combo
import Surveillance_mode as surveillance
import Face_recognition_mode as face_recog
import Face_tracking_mode as face_track
import obj_dectection_mode as obj_detect
import Text_detector_mode as txt_detector
from Database_Module import *
import tkinter as tk
import threading

root = tk.Tk()
root.title('CyberTrone - Control Panel')
root.iconbitmap('Resources/UI Icons/main icon.ico')
root.geometry("700x700")
root.config(bg="white")

# Config our column rows and cols
#Grid.rowconfigure(root, index=0, weight=1)
tk.Grid.columnconfigure(root, index=0, weight=1)



# Header label text:
homeLabel = tk.Label(root, text="CyberTrone\nSecurity Surveillance Drone", font="Bahnschrift 15", bg='dodger blue', fg="white", height=2, padx=20)
homeLabel.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Create Mode Button
combo_img = tk.PhotoImage(file='Resources/UI Icons/combo.png')
combo_img = combo_img.subsample(3, 3)

mode_btn = tk.Button(root, image=combo_img, command=combo.main, bg='dodger blue')
mode_btn.grid(row=1, column=0, pady=20, padx=20, ipadx=50)


surveillance_img = tk.PhotoImage(file='Resources/UI Icons/surveillance.png')
surveillance_img = surveillance_img.subsample(3, 3)

surveillance_btn = tk.Button(root, image=surveillance_img, command=surveillance.main, bg='dodger blue')
surveillance_btn.grid(row=1, column=1, pady=20, padx=20, ipadx=50)


face_track_img = tk.PhotoImage(file='Resources/UI Icons/face track.png')
face_track_img = face_track_img.subsample(3, 3)

face_tracking_btn = tk.Button(root, image=face_track_img, command=face_track.main, bg='dodger blue')
face_tracking_btn.grid(row=2, column=0, pady=20, padx=20, ipadx=50)

face_recg_img = tk.PhotoImage(file='Resources/UI Icons/face_recog.png')
face_recg_img = face_recg_img.subsample(3, 3)


face_recognition_btn = tk.Button(root, image=face_recg_img, command=face_recog.main,bg='dodger blue')
face_recognition_btn.grid(row=2, column=1, pady=20, padx=20, ipadx=50)


obj_detect_img = tk.PhotoImage(file='Resources/UI Icons/obj detect.png')
obj_detect_img = obj_detect_img.subsample(3, 3)


obj_detect_btn = tk.Button(root, image=obj_detect_img, command=obj_detect.main, bg='dodger blue')
obj_detect_btn.grid(row=3, column=0, pady=20, padx=20, ipadx=50)

txt_detect_img = tk.PhotoImage(file='Resources/UI Icons/text detect.png')
txt_detect_img = txt_detect_img.subsample(3, 3)


text_detect_mode_btn = tk.Button(root, image=txt_detect_img, command=txt_detector.main, bg='dodger blue')
text_detect_mode_btn.grid(row=3, column=1, pady=20, padx=20, ipadx=50)


homeLabel = tk.Label(root, text="Database Tools", font="Bahnschrift 15", bg='dodger blue', fg="white", height=1, padx=20)
homeLabel.grid(row=4, column=0, columnspan=4, sticky="nsew")

# Create a Save recognized Data Button
save_recognized_btn = tk.Button(root, text="Save Authorized images", command=Save_recognized_data, font="Bahnschrift 11", bg='dodger blue', fg="white")
save_recognized_btn.grid(row=5, column=0, pady=20, padx=20, ipadx=50)


# Create A Retrieve Button
retrieve_recognized_btn = tk.Button(root, text="Retrieve Authorized images ", command=fetch_recognized_data, font="Bahnschrift 11",
                                                                                      bg='dodger blue', fg="white")
retrieve_recognized_btn.grid(row=5, column=1, pady=20, padx=20, ipadx=50)



# Create a Save unrecognized Data Button
save_unrecognized_btn = tk.Button(root, text="Save Unauthorized images", command=save_unrecognized_data, font="Bahnschrift 11",
                                                                                                bg='dodger blue', fg="white")
save_unrecognized_btn.grid(row=6, column=0, pady=20, padx=20, ipadx=50)



# Create A Retrieve Button
retrieve_unrecognized_btn = tk.Button(root, text="Retrieve Unauthorized images", command=fetch_unrecognized_data, font="Bahnschrift 11",
                                                                                        bg='dodger blue', fg="white")
retrieve_unrecognized_btn.grid(row=6, column=1, pady=20, padx=20, ipadx=50)


# Create A detected text Button
save_recognized_text_btn = tk.Button(root, text="Save detected text images", command=save_recognized_text, font="Bahnschrift 11",
                                                                                        bg='dodger blue', fg="white")
save_recognized_text_btn.grid(row=7, column=0, pady=20, padx=20, ipadx=50)


retrieve_recognized_text_btn = tk.Button(root, text="Retrieve detected text images", command=fetch_recognized_text, font="Bahnschrift 11",
                                                                                        bg='dodger blue', fg="white")
retrieve_recognized_text_btn.grid(row=7, column=1, pady=20, padx=20, ipadx=50)


exit_img = tk.PhotoImage(file='Resources/UI Icons/exit.png')
exit_img = exit_img.subsample(3,3)


Exit_btn = tk.Button(root, image=exit_img, command=exit, bg='dodger blue')
Exit_btn.grid(row=8, column=0, columnspan=2, pady=20, padx=20, ipadx=50)

root.mainloop()