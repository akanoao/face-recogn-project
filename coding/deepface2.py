from deepface import DeepFace
#models = [
#  "VGG-Face",
#  "Facenet",
#  "Facenet512",
#  "OpenFace",
#  "DeepFace",
#  "DeepID",
#  "ArcFace",
#  "Dlib",
#  "SFace",
#]

#face verification
#result = DeepFace.verify(img1_path = "indv1.jpeg",
#      img2_path = "indv2.jpeg",
#      model_name = models[0]
#)


#face recognition
#objs = DeepFace.analyze(img_path = "indv1.jpeg",
#        actions = ['age', 'gender', 'race', 'emotion']
#)



backends = [
  'opencv',
  'ssd',
  'dlib',
  'mtcnn',
  'retinaface',
  'mediapipe',
  'yolov8',
  'yunet',
  'fastmtcnn',
]

#face verification

#face recognition
#dfs = DeepFace.find(img_path = "indv1.jpeg",
#        db_path = "my_db",
#        detector_backend = backends[0]
#)



#facial analysis
#demographies = DeepFace.analyze(img_path ="my_db/ayush/indv1.jpeg",
#                                detector_backend = backends[0]
#                                )


DeepFace.stream(db_path = "my_db")


#print(demographies)
