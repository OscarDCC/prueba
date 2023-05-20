import os
import cv2
import numpy as np
from imutils import paths
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.svm import SVC
import pickle
import dlib
import face_recognition

# 1. Preprocesamiento de imágenes
def procesar_imagen(imagen):
    # Convertir a escala de grises
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    # Ecualización del histograma
    imagen = cv2.equalizeHist(imagen)
    # Reducción de ruido
    imagen = cv2.GaussianBlur(imagen, (5, 5), 0)
    return imagen

# 2. Cargar imágenes y etiquetas
imagenes = []
etiquetas = []
ruta_dataset = 'home/jetson/prueba/fotos'

for ruta_imagen in paths.list_images(ruta_dataset):
    # Extraer la etiqueta de la ruta de la imagen
    etiqueta = ruta_imagen.split(os.path.sep)[-2]
    # Cargar la imagen y preprocesarla
    imagen = cv2.imread(ruta_imagen)
    imagen = procesar_imagen(imagen)
    # Agregar la imagen y la etiqueta a las listas
    imagenes.append(imagen)
    etiquetas.append(etiqueta)

# 3. Codificación de etiquetas
le = LabelEncoder()
etiquetas_codificadas = le.fit_transform(etiquetas)

# 4. Separación en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(np.array(imagenes), etiquetas_codificadas, test_size=0.2, random_state=42)

# 5. Entrenamiento del modelo
modelo = SVC(kernel='linear', C=1.0, probability=True)
modelo.fit(X_train.reshape((X_train.shape[0], -1)), y_train)

# 6. Evaluación del modelo
predicciones = modelo.predict(X_test.reshape((X_test.shape[0], -1)))
print(classification_report(y_test, predicciones, target_names=le.classes_))

# 7. Guardar el modelo en un archivo
with open('modelo.pickle', 'wb') as archivo:
    archivo.write(pickle.dumps(modelo))

# 8. Actualización del modelo
for ruta_imagen in list(paths.list_images(directorio)):


