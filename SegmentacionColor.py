import os
import cv2
import numpy as np

# Rutas de carpetas
CARPETA_ORIGINAL = "./flowers"
CARPETA_DESTINO = "./flowers_segmented"
TAMANO_RED = (150, 150) #Redimension a lo que pide collab

if not os.path.exists(CARPETA_DESTINO):
    os.makedirs(CARPETA_DESTINO)

print("Iniciando segmentacion por color... Esto removera los fondos verdes de las fotos.")

for clase in os.listdir(CARPETA_ORIGINAL):
    ruta_clase_origen = os.path.join(CARPETA_ORIGINAL, clase)
    if not os.path.isdir(ruta_clase_origen):
        continue
        
    ruta_clase_destino = os.path.join(CARPETA_DESTINO, clase)
    if not os.path.exists(ruta_clase_destino):
        os.makedirs(ruta_clase_destino)
        
    for archivo in os.listdir(ruta_clase_origen):
        ruta_img = os.path.join(ruta_clase_origen, archivo)
        img = cv2.imread(ruta_img)
        
        if img is None:
            continue
            
        # 1. Redimensionar al tamaño de la red
        img_res = cv2.resize(img, TAMANO_RED)
        
        # 2. Convertir a HSV para detectar el verde del fondo
        hsv = cv2.cvtColor(img_res, cv2.COLOR_BGR2HSV)

        # 3. Definir rangos para ubicar el color verde 
        baja_verde = np.array([35, 40, 40])
        alta_verde = np.array([85, 255, 255])
        
        # Creamos una mascara que detecta todo lo verde
        mascara_verde = cv2.inRange(hsv, baja_verde, alta_verde)
        
        # Invertimos la mascara que ahora selecciona todo lo que no es verde 
        mascara_flores = cv2.bitwise_not(mascara_verde)
        
        # 4. Aplicar la mascara sobre la imagen original para recortar el fondo
        img_segmentada = cv2.bitwise_and(img_res, img_res, mask=mascara_flores)
        
        # Guardar resultado en la nueva carpeta
        cv2.imwrite(os.path.join(ruta_clase_destino, archivo), img_segmentada)

print("Proceso terminado con exito, revise la carpeta 'flowers_segmented'.")