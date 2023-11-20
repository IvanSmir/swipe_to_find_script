import os
import time
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' 


def detectar_numero(imagen, numero):
    """
    Esta función detecta si un número específico está presente en la imagen.
    Utiliza Pytesseract para OCR.
    """

    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

   
    texto = pytesseract.image_to_string(imagen_gris)
    lineas = texto.split('\n')
    if len(lineas) >= 5:
        print(lineas[4])  
    else:
        print("No hay suficientes líneas en el texto extraído.")
  
    return numero in texto

numero_deseado = "998"  

while True:
   
    os.system("adb shell screencap -p /sdcard/screen.png")
    os.system("adb pull /sdcard/screen.png screen.png >nul")

    imagen = cv2.imread('screen.png')
    

   
    if detectar_numero(imagen, numero_deseado):
        print("Número encontrado!")
        break

    
    os.system("adb shell input swipe 500 300 500 1600")  #
    time.sleep(1)

print("Proceso completado")
