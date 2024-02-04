import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image
from tkinter.messagebox import showerror, showwarning, showinfo
import sqlite3
import tkcalendar as tkc

class add_student():
    def window(self, notebook, window):

        frame = ttk.Frame(notebook, width=400, height=280)

        self.name_label = ttk.Label(frame, text="Student Name:")
        self.name_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        self.name = tk.StringVar()
        self.name_entry = ttk.Entry(frame, textvariable=self.name)
        self.name_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        Studentid_label = ttk.Label(frame, text="Student ID:")
        Studentid_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        studentid_entry = ttk.Entry(frame)
        studentid_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        image_label = ttk.Label(frame, text="Student Image:")
        image_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

        self.image_show = tk.Text(frame, width=20, height=1)
        self.image_show.grid(column = 1, row = 2, sticky = tk.W, padx = 5, pady = 5)

        image_select = tk.Button(frame, text="select", command=lambda: [add_student.select(self)])
        image_select.grid(column = 2, row = 2, sticky = tk.W, padx = 5, pady = 5)

        add_button = tk.Button(frame, text="Add", command=lambda: [add_student.add(self)])
        add_button.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

        return frame


    def select(self):
        self.filepath = filedialog.askopenfilename(initialdir='E:\\python projects\\hackathon\\pythonProject', title='select image')
        fname = self.filepath.split('/')
        self.image_show.insert('1.0', fname[-1])

    def add(self):
        if os.path.isfile(f'E:/python projects/hackathon/pythonProject/images/{self.name.get()}.jpg') == False:
            im = Image.open(self.filepath)
            im.save(f'E:/python projects/hackathon/pythonProject/images/{self.name.get()}.jpg')
