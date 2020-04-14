# Create a function

def my_function():
  print("Hola kmostas")

# 
# my_function()

# Arguments
# Se definen después del nombre de la función, dentro de parentesis y se pueden definir
# Tantos como queramos, separados por comas
# args

# Parametros o Argumentos?
# Parametros: Lo que va a recibir la variable
# Argumentos: El valor que se le manda a la función cuando es llamada

def print_name(name, last_name):
  print("Hola,", name, last_name)

# print_name("Arturo")
# print_name("Melo")
# print_name("Topi")

# Ponemos un asterisco antes de el nombre del parametro cuando no se conoce el número de argumentos
# Esto hará que se reciba una tupla de argumentos
def name(*kids):
  print("El niño más peque es", kids[2])

# name("Arturo", "Melo", "Topi")

# Si agregamos el nombre del parametro, podemos definirle un valor sin necesidad
# De pasar los argumentos en orden
def morritos(morrito1, morrito2, morrito3):
  print("El más cool es", morrito2)

# morritos(morrito2 = "Melo", morrito1 = "Yo merengues", morrito3 = "Tu sipsi")

def pais(pais = "Tangamandapio"):
  print("Yo vivo en", pais)

# pais()
# pais("Mi casa")

# No es necesario definir el tipo de dato que va a recibir la función
def comida(comida):
  for comidita in comida:
    print(comidita)

# comida("Maruchans")

# Regresar algún valor llamando una función
def multiplicación(x):
  return 5 * x

# print(multiplicación(5))

def pruebita():
  pass

# pruebita()


# Recursividad
# Llamar una función dentro de si misma

def factorial(x):
  if x ==1:
      return 1
  else:
      return x * factorial(x-1)

print(factorial(5))


lista = ["Arturo", "Melo", "Topi"]

for elemento in lista:
  print(elemento)


# Hacer un for con recursividad
# Recrear la lógica de arriba sin utilizar el for