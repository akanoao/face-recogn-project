import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showerror, showwarning, showinfo
import sqlite3
import mysql.connector as sql

class notebook():
    def window(self):
        root_opt = tk.Tk()
        root_opt.title("option")
        window_width = 400
        window_height = 125

        screen_width = root_opt.winfo_screenwidth()
        screen_height = root_opt.winfo_screenheight()

        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        root_opt.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        notebookv = ttk.Notebook(root_opt)
        notebookv.pack(pady=10, expand=True, anchor = tk.NW, fill = tk.BOTH)

        from issue_return import issuereturn
        frame1 = issuereturn.window(self, notebookv, root_opt)
        frame1.pack(fill='both', expand=True)
        notebookv.add(frame1, text='library')

        from attendance import attendance
        frame2 = attendance.window(self, notebookv, root_opt)
        frame2.pack(fill='both', expand = True)
        notebookv.add(frame2, text='attendance')

        from add_student import add_student

        frame3 = add_student.window(self, notebookv, root_opt)
        frame3.pack(fill='both', expand=True)

        notebookv.add(frame3, text='Add Student')
        root_opt.mainloop()



