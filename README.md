# Clasificacion de Flores mediante Limpieza de Fondo (HSV)

**Estudiante:** Carlos Alberto Gutierrez Flores  
**Asignatura:** Sistemas Distribuidos  
**Fecha:** Junio 2026  

## 1. ¿De que trata la propuesta? 
Las fotografias originales del dataset de flores vienen con mucha "basura" o ruido visual de fondo, como pasto, hojas verdes, ramas, tierra y sombras. Para una Inteligencia Artificial, todo ese entorno es una distraccion que dificulta el aprendizaje.

Este proyecto propone un script de preprocesamiento usando **OpenCV** que limpia las imagenes antes de mandarlas a la Red Neuronal (CNN). El codigo realiza tres pasos simples:
1. Cambia la imagen al formato **HSV**, que es excelente para identificar colores sin que le afecten los cambios de luz o sombras.
2. Detecta de forma automatica todos los tonos verdes y cafes del fondo.
3. Borra todo ese fondo ruidoso y lo sustituye por un negro absoluto, dejando unicamente la flor flotando en la oscuridad.

### ¿Como ayuda esto a la Red Neuronal?
Al dejar el fondo completamente negro, le entregamos a la Inteligencia Artificial un dataset limpio y directo. Los filtros de la CNN ya no pierden tiempo procesando el pasto o el suelo; ahora van directo al grano a revisar la forma, los bordes y los colores de los petalos. Gracias a esto, el modelo aprendio mucho mejor y **el Accuracy Global subio del 78% al 84.34%**.

## 2. Evidencia Visual (Original vs. Procesada)
Durante el proceso, el script tambien ajusta de forma automatica el tamaño de todas las imagenes a 150 x 150 píxeles para que coincidan exactamente con la entrada de la red:

## 3. Guia de Ejecucion de codigo

### Paso 1: Procesar las imagenes en tu computadora
1.Descargar el dataset de https://www.kaggle.com/datasets/alxmamaev/flowers-recognition
2.Descomprime el dataset en la carpeta que tu prefieras
3.Coloca la carpeta original de imágenes llamada `flowers` en el mismo directorio donde tengas el script.
4. Ejecuta el script de Python en la mismca carpeta donde descomprimiste el dataset, para limpiar los fondos de todo el dataset de golpe:
   python SegmentacionColor.py
5.El programa creara una nueva carpeta llamada flowers_segmented con las fotos limpias a tamaño 150 x 150.

## 4. Entrenar la Red Neuronal en Google Colab

OPCION 1 DE FORMA LOCAL(MAS RAPIDO)

1.ingresa a el link del proyecto https://colab.research.google.com/drive/10veQvQ0oRC7_7rpPX3TamjcFUE91Khab?usp=sharing
2. Sube el archivo flowers_segmented.zip directamente a la pestaña de "Archivos" en el panel izquierdo de Colab.
3.Descomprime el dataset ejecutando esta linea en una celda de codigo:
!unzip -q /content/flowers_segmented.zip -d /content/dataset_final
4.Modifica la ruta en el script para que apunte a la carpeta local:
RUTA_DATOS = "/content/dataset_final/flowers_segmented" O DATASET_DIR = "/content/drive/MyDrive/dataset_original"
4.1: Para mejorar la velocidad dirigete a la opcion Entorno de ejecucion > cambiar tipo de entorno de ejecucion > gpu t4 > guardar, esto hara que la gpu se encargue de procesar todo bajando el tiempo de horas a cuestion de minutos.

OPCION 2 CON GOOGLE DRIVE

1.ingresa a el link del proyecto https://colab.research.google.com/drive/10veQvQ0oRC7_7rpPX3TamjcFUE91Khab?usp=sharing
2.Sube tu carpeta de flowers_segmented a tu drive en una carpeta que elijas (por ejemplo, dentro de una carpeta llamada ProyectoCNN).
3.Cambia la ruta por defecto del proyecto a la ruta en la que subiste la carpeta
consola
RUTA_DATOS = "/content/drive/MyDrive/ProyectoCNN/flowers_segmented"
4.ejecuta el codigo del collab acepta que se conecte a tu cuenta de google drive y listo

