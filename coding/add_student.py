import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showerror, showwarning, showinfo
import sqlite3
import tkcalendar as tkc

class add_student():
     def window(self, notebook, window):


        frame = ttk.Frame(notebook, width=400, height=280)

        name_label = ttk.Label(frame, text="Student Name:")
        name_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        name_entry = ttk.Entry(frame)
        name_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        Studentid_label = ttk.Label(frame, text="Student ID:")
        Studentid_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        studentid_entry = ttk.Entry(frame)
        studentid_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        image_label = ttk.Label(frame, text="Student Image:")
        image_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

        self.image_show = tk.Text(frame, width=20, height=1)
        self.image_show.grid(column = 1, row = 2, sticky = tk.W, padx = 5, pady = 5)

        image_select = tk.Button(frame, text="select", command=lambda: [add_student.select(self, notebook)])
        image_select.grid(column = 2, row = 2, sticky = tk.W, padx = 5, pady = 5)


        return frame


     def select(self, notebook):
         filepath = filedialog.askopenfilename(initialdir='E:\\python projects\\hackathon\\pythonProject', title='select image')
         self.image_show.insert('1.0', filepath)
