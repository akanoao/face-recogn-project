import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
import sqlite3
from datetime import datetime
import sqlite3

class show():
    def window(self):
        root_att = tk.Tk()
        root_att.title("show")
        window_width = 600
        window_height = 200

        screen_width = root_att.winfo_screenwidth()
        screen_height = root_att.winfo_screenheight()

        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        root_att.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')



        amount = show.get(self)
        i = 0
        while(i < amount):
            root_att.columnconfigure(i, weight=1)

            namelabel = ttk.Label(root_att, text= self.info[i][0])
            namelabel.grid(column = 0, row = i, padx=10, pady=5)


            attlabel = ttk.Label(root_att, text = self.info[i][1])
            attlabel.grid(column = 1, row = i, padx=10, pady=5)

            timeslabel = ttk.Label(root_att, text = self.info[i][2])
            timeslabel.grid(column = 2, row = i, padx=10, pady=5)


            timeelabel = ttk.Label(root_att, text = self.info[i][3])
            timeelabel.grid(column = 3, row = i, padx=10, pady=5)

            i += 1

        from attendance import attendance
        button = ttk.Button(root_att, text='back', command=lambda: [root_att.destroy(), attendance.window(self)])
        button.grid(column=3, row=i+1, padx=10, pady=5)
        root_att.mainloop()

    def get(self):
        try:
            mydb = sqlite3.connect('attendance_database.sqlite')
            mycursor = mydb.cursor()
            mycursor.execute('select * from attendance')
            self.info = mycursor.fetchall()
            return len(self.info)
        except:
            showerror("error", "error")