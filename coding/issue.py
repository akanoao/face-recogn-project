import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
import mysql.connector as sql

class issue():
    def window(self):
        root_issue = tk.Tk()

        root_issue.columnconfigure(0, weight = 1)
        root_issue.columnconfigure(1, weight=1)
        root_issue.columnconfigure(2, weight=1)

        name_label = ttk.Label(root_issue, text="Name: ")
        name_label.grid(column = 0, row = 0, sticky = tk.W, padx = 5, pady = 10)

        self.name = tk.Text(root_issue, height=1, width=20)
        self.name.grid(column=1, row=0, sticky=tk.W, padx=5, pady=10)
        self.name["state"] = 'disabled'

        name_button = ttk.Button(root_issue, text="Scan")
        name_button.grid(column=2, row=0, sticky=tk.W, padx=5, pady=10)

        id_label = ttk.Label(root_issue, text="Book ID: ")
        id_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=10)

        self.id = tk.Text(root_issue, height = 1, width= 20)
        self.id.grid(column=1, row=1, sticky=tk.W, padx=5, pady=10)
        self.id["state"] = 'disabled'

        id_button = ttk.Button(root_issue, text="Scan", command=lambda: [issue.namescan(self)])
        id_button.grid(column=2, row=1, sticky=tk.W, padx=5, pady=10)

        ok_button = ttk.Button(root_issue, text="Ok")
        ok_button.grid(column=2, row=2, sticky=tk.W, padx=5, pady=10)

        from issue_return import issuereturn
        back_button = ttk.Button(root_issue, text="back", command=lambda: [root_issue.destroy(), issuereturn.window(self)])
        back_button.grid(column=0, row=2, sticky=tk.W, padx=5, pady=10)
        root_issue.mainloop()

    def namescan(self):
        from main import scanner
        data = scanner.scan_issue(self)
        self.id["state"] = 'normal'
        self.id.insert('1.0', data)
        self.id["state"] = 'disabled'
