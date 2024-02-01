import time

import numpy as np
from datetime import datetime
from pyzbar.pyzbar import decode
from PIL import Image
from tkinter.messagebox import showerror, showwarning, showinfo
import mysql.connector as sql
import cv2

class scanner():
    def scan_issue(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 1280)
        self.cap.set(4, 720)

        while True:
            success, self.image = self.cap.read()
            cv2.imshow('scanner', self.image)
            scanner.issue(self)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                self.cap.release()

    def issue(self):
        for code in decode(self.image):
            data = code.data.decode('utf-8')
            time.sleep(5)
            try:
                mydb = sql.connect(host='localhost', user='root', password='anurag11')
                mycursor = mydb.cursor()
                mycursor.execute('use project')
                mycursor.execute('select * from issue where book_id = ("{}")'.format(data))
                info = mycursor.fetchall()
                if (len(info) == 0):
                    date = datetime.today().strftime('%Y-%m-%d')
                    mycursor.execute('insert into issue values ("{}", "{}", "anuj")'.format(date, data))
                mydb.commit()
                mydb.close()
            except:
                showerror("error", "error")

