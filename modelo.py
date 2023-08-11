#Categorizar una imagen de internet
from PIL import Image
import requests
from io import BytesIO
import cv2
import numpy as np
from tensorflow import keras

def categorizar(imagen):

    img = imagen
    img = np.array(img).astype(float)/255

    img = cv2.resize(img, (224,224))
    prediccion = modelo.predict(img.reshape(-1, 224, 224, 3))
    return np.argmax(prediccion[0], axis=-1)

razas={ 0:"Gallina Andaluza Azul",
        1:"Gallina Ayam Cemani",
        2:"Gallina Castellana Negra",
        3:"Gallina Isa Brown",
        4:"Gallina Leghorn",
        5:"Gallina Marans",
        6:"Gallina Orpington",
        7:"Gallina Paduana",
        8:"Gallina Pita Pinta Asturiana",
        9:"Gallina Plymouth Rock",
        10:"Gallina Rodhe Island",
        11:"Gallina Sebright",
        12:"Gallina Sedosa de Japon",
        13:"Gallina Serama",
        14:"Gallina Utrerana",
        15:"Gallina Wyandotte",
        16:"Gallina de Araucana",
        17:"Gallina de Guinea",
        18:"Gallina de Mos",
        19:"Gallina de Sussex",
        20:"Gallina de Cuello Pelado",
        21:"Gallina flor dametller"
        }

# Ruta al directorio que contiene el modelo guardado (.pb)
modelo_path = "./modelo_save/content/sample_data/modelo_save/"

# Cargando el modelo guardado
modelo = keras.models.load_model(modelo_path)

# Verifica la estructura y detalles del modelo cargado
# print(loaded_model.summary())
