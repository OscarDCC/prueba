import cv2
import os
import numpy as np
import face_recognition
from sklearn import svm
import pickle

# Directorio con las imagenes de entrenamiento
directorio = "/home/jetson/prueba/fotos"

# Lectura de las imagenes y generación de los encodings y etiquetas
encodings = []
labels = []
for subdir, dirs, files in os.walk(directorio):
    for file in files:
        img_path = os.path.join(subdir, file)
        label = os.path.basename(subdir)
        img = cv2.imread(img_path)
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(rgb_img, model="hog")
        encodings_img = face_recognition.face_encodings(rgb_img, boxes)
        for encoding in encodings_img:
            encodings.append(encoding)
            labels.append(label)

# Entrenar modelo
print("Entrenando modelo...")
classifier = svm.LinearSVC()
classifier.fit(encodings, labels)

# Guardar modelo
print("Guardando modelo...")
with open('modelo.pickle', 'wb') as f:
    pickle.dump(classifier, f)

print("Modelo entrenado y guardado exitosamente!")

