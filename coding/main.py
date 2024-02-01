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
            for code in decode(self.image):
                self.data = code.data.decode('utf-8')
                self.cap.release()
                return self.data
            if cv2.waitKey(1) & 0xFF == ord("q"):
                self.cap.release()


