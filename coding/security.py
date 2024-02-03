import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
import sqlite3
from datetime import datetime
import sqlite3

class security():
    def window(self):
        root_sec = tk.ttk()
        window_width = 600
        window_height = 200

        screen_width = root_sec.winfo_screenwidth()
        screen_height = root_sec.winfo_screenheight()

        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        root_sec.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        root_sec.mainloop()
