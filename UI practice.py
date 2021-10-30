from tkinter import *
import CyberTrone as combo


root = Tk()
root.title('Codemy.com - Flip The Switch!')
#root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x300")

# Keep track of the button state on/off
global is_on
is_on = True




# Create Label
my_label = Label(root,
	text="Combo Version OFF",
	fg="green",
	font=("Helvetica", 32))

my_label.pack(pady=20)

def switch():
	global is_on
	# Determin is on or off
	if is_on:
		on_button.config(image=off)
		my_label.config(text="The Switch is Off", fg="grey")
		is_on = False
	else:
		on_button.config(image=on, command=combo.main)
		my_label.config(text="The Switch is On", fg="green")
		is_on = True


# Define Our Images
on = PhotoImage(file="Resources/UI Icons/combo.png")
off = PhotoImage(file="Resources/UI Icons/surveillance.png")

# Create A Button
on_button = Button(root, image=on, bd=0, command=switch)
on_button.pack(pady=50)

root.mainloop()
