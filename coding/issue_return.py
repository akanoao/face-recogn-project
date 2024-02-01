import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
import mysql.connector as sql

class issuereturn():
    def window(self):
        root_issret = tk.Tk()
        root_issret.title("issue/return")
        window_width = 300
        window_height = 130

        screen_width = root_issret.winfo_screenwidth()
        screen_height = root_issret.winfo_screenheight()

        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        root_issret.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        from issue import issue
        issubutton = ttk.Button(root_issret, text='issue', command=lambda: [root_issret.destroy(), issue.window(self)])
        issubutton.pack(padx=10, pady=5, anchor=tk.CENTER)
        from Return import Return
        retbutton = ttk.Button(root_issret, text='return', command=lambda: [root_issret.destroy(), Return.window(self)])
        retbutton.pack(padx=10, pady=5, anchor=tk.CENTER)

        from options import options
        backbutton = ttk.Button(root_issret, text='back', command=lambda: [root_issret.destroy(), options.window(self)])
        backbutton.pack(padx=10, pady=5, anchor=tk.CENTER)
        root_issret.mainloop()