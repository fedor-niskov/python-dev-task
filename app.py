from tkinter import *

def inc_count():
	global counter
	counter += 1
	b_count_text.set("Pressed: " + str(counter))

def reset_count():
	global counter
	counter = 0
	b_count_text.set("Pressed: 0")

root = Tk()

b_exit = Button(root, command=root.quit, text="Exit")
b_exit.grid()

counter = 0
b_count_text = StringVar()
b_count_text.set("Pressed: 0")
b_count = Button(root, command=inc_count, textvariable=b_count_text)
b_count.grid()

b_reset = Button(root, command=reset_count, text="Reset")
b_reset.grid()

root.mainloop()

