# Escribir en un archivo de texto

# modos para trabajar con archivos
# r -  Abrir un archivo para lectura
# w - Abrir un archivo para escritura, si no existe, crea un nuevo archivo; si existe, lo sobreescribe
# x - Crear un archivo nuevo; Si el archivo ya existe, la operación falla
# a - Abrir un archivo para añadir, si el archivo no existe, crea uno nuevo
# t - Abre el archivo en modo texto
# b - Abre el archivo en modo binario
# + - Abre el archivo para lectura y escritura

def binario():
  archivo = open("texto.txt", "bt")

  contenido = archivo.read()
  print(contenido)

  archivo.close()

def texto():
  archivo = open("texto.txt", "rt")

  contenido = archivo.read()
  print(contenido)

  archivo.close()

def create():
  archivo = open("archivo_nuevo.txt", "x+")

  archivo.write("Escribe esto, porfi")

  contenido = archivo.readlines()
  print(contenido)

  archivo.close()

def read():
  archivo = open("texto.txt", "r")

  if archivo.mode == 'r':
    content = archivo.read()
    print(content)
  
  archivo.close()

def append():
  archivo = open("texto.txt", "a+")

  for i in range(5):
    archivo.write(f"Esta linea esta apendada {i+1}\n")

  archivo.close()

def main():
  archivo = open("texto.txt", "w+")

  for i in range(10):
    archivo.write(f"Texto aleatorio que se me ocurrio {i+1}\n")

  archivo.close()

texto()
