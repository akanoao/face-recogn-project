import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
import sqlite3
from datetime import datetime
import sqlite3

class show():
    def window(self):
        root_att = tk.Tk()
        root_att.resizable(False, True)
        root_att.title("show")
        window_width = 400
        window_height = 200

        screen_width = root_att.winfo_screenwidth()
        screen_height = root_att.winfo_screenheight()

        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        root_att.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        lf = ttk.LabelFrame(root_att, text='attendance')
        lf.grid(column=0, row=0, padx=15, pady=30)


        amount = show.get(self)
        i = 0
        name = ttk.Label(lf, text='NAME')
        name.grid(column=0, row=0, padx=10, pady=5)

        att = ttk.Label(lf, text='P/A')
        att.grid(column=1, row=0, padx=10, pady=5)

        times = ttk.Label(lf, text='Starting Time')
        times.grid(column=2, row=0, padx=10, pady=5)

        timee = ttk.Label(lf, text='Ending Time')
        timee.grid(column=3, row=0, padx=10, pady=5)

        while(i < amount):
            root_att.columnconfigure(i, weight=1)

            att = ttk.Label(lf, text= self.info[i][0])
            att.grid(column = 0, row = i+1, padx=10, pady=5)


            attlabel = ttk.Label(lf, text = self.info[i][1])
            attlabel.grid(column = 1, row = i+1, padx=10, pady=5)

            timeslabel = ttk.Label(lf, text = self.info[i][2])
            timeslabel.grid(column = 2, row = i+1, padx=10, pady=5)


            timeelabel = ttk.Label(lf, text = self.info[i][3])
            timeelabel.grid(column = 3, row = i+1, padx=10, pady=5)

            i += 1

        from attendance import attendance
        button = ttk.Button(lf, text='back', command=lambda: [root_att.destroy(), attendance.window(self)])
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