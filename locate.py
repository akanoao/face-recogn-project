import face_recognition
from PIL import Image

#loading the image
image = face_recognition.load_image_file("WhatsApp Image 2024-01-29 at 00.31.34 (2).jpeg") 
face_locations = face_recognition.face_locations(image)

# print(face_locations)
for face_location in face_locations:
    top = face_location[0]
    right = face_location[1]
    bottom = face_location[2]
    left = face_location[3]

    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()
