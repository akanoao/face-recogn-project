import numpy as np
import cv2
import imutils
import datetime
from playsound import playsound
import time

def detect():
    gun_cascade = cv2.CascadeClassifier('cascade.xml')
    camera = cv2.VideoCapture(0)
    camera.set(3,1280)
    camera.set(4,720)
    firstFrame = None
    gun_exist = False
    while True:
        ret, frame = camera.read()
        if frame is None:
            break
        frame = imutils.resize(frame, width=500)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gun = gun_cascade.detectMultiScale(gray, 1.3, 20, minSize=(100, 100))
        if len(gun) > 0:
            gun_exist = True
            playsound('siren.mp3', block=False)

            # try:
            #     playsound("siren.mp3",block="False")
            #     time.sleep(2)
            # except:
            #     pass
        for (x, y, w, h) in gun:
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
        if firstFrame is None:
            firstFrame = gray
            continue
        cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S %p"),
        (10, frame.shape[0] - 10),cv2.FONT_HERSHEY_SIMPLEX,0.35, (0, 255, 255), 1)

        # print("Guns detected")
        cv2.imshow("pic",frame)
        # else:
        #     cv2.imshow("Security Feed", frame)
        # key = cv2.waitKey(1) & 0xFF
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()
