import face_recognition
from PIL import Image

#known image
my_pic = face_recognition.load_image_file("daksh.jpg")
my_pic_encoding = face_recognition.face_encodings(my_pic)[0]

#unknown image

unknown_pic = face_recognition.load_image_file("WhatsApp Image 2024-01-29 at 00.31.34 (2).jpeg")
unknown_pic_encoding = face_recognition.face_encodings(unknown_pic)

results = face_recognition.compare_faces(my_pic_encoding, unknown_pic_encoding)
print(results)

if True in results:
    print("daksh is present")