import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
import sqlite3
from datetime import datetime
import sqlite3

class security():
    def window(self, notebook, window):
        frame = ttk.Frame(notebook, width=400, height=280)
        import weapon_detect
        scan_button = tk.Button(frame, text="Scan", command=lambda: [weapon_detect.detect()])
        scan_button.pack(anchor=tk.CENTER, padx=5, pady=5)

        return frame