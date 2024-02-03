import sqlite3
import time
import datetime
import pytz
import face_recognition
import cv2
import numpy as np

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)


# Load a sample picture and learn how to recognize it.
obama_image = face_recognition.load_image_file("indv1.jpeg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# Load a second sample picture and learn how to recognize it.
biden_image = face_recognition.load_image_file("harsh.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    obama_face_encoding,
    biden_face_encoding
]
known_face_names = [
    "daksh",
    "harsh"
]

# Initialize some variables
known_face_counters = {}
# detect = 0
# attendance_dict = {}
present_list = []
# absent_list = []
face_locat = []
face_encodings = []
face_nam = []
process_this_frame = True
intial_time = time.time()
TIME_ZONE = pytz.timezone('Asia/Kolkata')
start_time = datetime.datetime.now().astimezone(TIME_ZONE).strftime("%Y-%m-%d %H:%M:%S")
DURATION = 30 # ex - for 2min or 120 sec put 100sec coz 20 sec is taken for detection
DETECTION_TIME = 5
HALF_TIME = (DURATION//2)+DETECTION_TIME
DELAY_TIME = (int(DURATION//2)-DETECTION_TIME)*1000 # 5 10 5 10 5

while True:
    if round(time.time()-intial_time) in [DETECTION_TIME,HALF_TIME]:
        video_capture.release()
        cv2.destroyAllWindows()
        cv2.waitKey(DELAY_TIME)
        face_nam.append(known_face_counters)
        known_face_counters = {}
        video_capture = cv2.VideoCapture(0)

    if round(time.time()-intial_time) == (DURATION+DETECTION_TIME):
        face_nam.append(known_face_counters)
        break

    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Only process every other frame of video to save time
    if process_this_frame:
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.58)
            name = "Unknown"

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                known_face_counters[name] = known_face_counters.get(name, 0) + 1
                # detect+=1
            face_names.append(name)
        # face_nam.append(face_names)
    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# print(face_nam)
# print(detect)

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
end_time = datetime.datetime.now().astimezone(TIME_ZONE).strftime("%Y-%m-%d %H:%M:%S")
print(start_time, end_time, end="\n")
# MOYE MOYE MOYE MOYE MOYE MOYE MOYE MOYE MOYE MOYE MOYE
# for j in range(len(face_nam)):
#     for i in face_nam[j].keys():
#         if i in face_nam[(j+1)%3] and face_nam[(j+2)%3]:
#             attendance_dict[i] = 1
#         else:
#             attendance_dict[i] = 0

for i in face_nam[0].keys():
    if i in face_nam[1] and face_nam[2]:
        present_list.append(i)
# for i in known_face_names:
#     if i not in present_list:
#         absent_list.append(i)

# name status date time
conn = sqlite3.connect("attendance_database.sqlite")
cur = conn.cursor()

cur.executescript(
    """
CREATE TABLE IF NOT EXISTS "attendance" (
	"student_name"	varchar(100) NOT NULL,
	"attendance_status"	INTEGER NOT NULL,
	"start_time"	datetime NOT NULL,
	"end_time"	datetime NOT NULL
)
"""
)
for i in known_face_names:
    if i in present_list:
        cur.execute(
            """INSERT INTO attendance VALUES(?,?,?,?)""",
            (i, "1", start_time, end_time),
        )
    else:
        cur.execute(
            """INSERT INTO attendance VALUES(?,?,?,?)""",
            (i, "0", start_time, end_time),
        )
