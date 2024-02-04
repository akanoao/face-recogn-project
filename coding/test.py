from tkinter import *
import tkinter as tk
from tkinter import filedialog

# Create an instance of tkinter window
win = Tk()

# Define the geometry of the window
win.geometry("700x500")

frame = Frame(win, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
filepath = filedialog.askopenfilename(initialdir='E:\\python projects\\hackathon\\pythonProject', title='select image')
pic = tk.PhotoImage(file=filepath)

# Create a Label Widget to display the text or Image
label = Label(frame, image = pic)
label.pack()

win.mainloop()