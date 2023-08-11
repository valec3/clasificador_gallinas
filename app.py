from PIL import Image
import streamlit as st
import cv2
# Cargar el modelo previamente entrenado
from modelo import razas,categorizar


def main():
    st.title("Clasificador de Razas de Gallinas")
    st.write("Carga una imagen desde tu computadora o utiliza la cámara para clasificarla.")

    opcion = st.radio("Selecciona una opción:", ("Cargar imagen", "Usar cámara"))

    if opcion == "Cargar imagen":
        imagen = st.file_uploader("Selecciona una imagen", type=["jpg", "jpeg", "png"])
        if imagen is not None:
            imagen = Image.open(imagen)
            st.image(imagen, caption="Imagen seleccionada", use_column_width=True)
            if st.button("Clasificar"):
                clase = razas[categorizar(imagen)]
                st.write(f"La imagen de la gallina pertenece a la raza {clase}")

    elif opcion == "Usar cámara":
        st.write("Presiona el botón para capturar una imagen desde la cámara")
        if st.button("Capturar"):
            # Capturar imagen desde la cámara utilizando cv2
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            cap.release()

            if ret:
                # Convertir el frame de BGR a RGB
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Mostrar la imagen capturada en Streamlit
                imagen_capturada = Image.fromarray(frame)
                st.image(imagen_capturada, caption="Imagen capturada", use_column_width=True)

                # Realizar la clasificación con la imagen capturada
                clase = razas[categorizar(imagen_capturada)]
                st.write(f"La imagen de la gallina pertenece a la raza {clase}")

if __name__ == "__main__":
    main()
