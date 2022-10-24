from tkinter import *
import tkinter.filedialog

root = Tk("Text Editor")
#root.geometry("1600x900")

text = Text(root)
text.grid()

# Button to save the file

def saveas():
	global text
	t = text.get("1.0", "end-1c")
	savelocation = tkinter.filedialog.asksaveasfilename()
	file1 = open(savelocation, "w+")
	file1.write(t)
	file1.close()

button = Button(root, text="Save", command=saveas)
button.grid()

##########################################


# Font menu button

def fontHelvetica():
	global text
	text.config(font="Helvetica")

def fontCourier():
	global text
	text.config(font="Courier")

def fontTimes():
	global text
	text.config(font="Times")

font = Menubutton(root, text="Font")
font.grid()
font.menu = Menu(font, tearoff=0)
font["menu"] = font.menu

helvetica = IntVar()
courier = IntVar()
times = IntVar()

font.menu.add_radiobutton(label="Helvetica", variable=helvetica, command=fontHelvetica)
font.menu.add_radiobutton(label="Courier", variable=courier, command=fontCourier)
font.menu.add_radiobutton(label="Times", variable=times, command=fontTimes)

##########################################

root.mainloop()



