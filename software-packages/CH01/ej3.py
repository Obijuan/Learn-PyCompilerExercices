import sys

# -- Ejercicio 3
# -- Leer el fichero p0103.txt
# -- Mostrar primero las palabras y después los números

FICHERO = 'p0103.txt'

# -- Abrir el fichero y leer los datos
try:
    with open(FICHERO, "r") as fd:
        # -- Data es una cadena, con la informacion leida del fichero
        data = fd.read()

except IOError:
    print(f"Error leyendo fichero {FICHERO}")
    sys.exit(1)

# -- Imprimir el contenido del fichero original
print()
print("CONTENIDO FICHERO:")
print(data)

# -- Obtener la primera linea (sin el \n)
data = data.splitlines()

# -- Separar la linea en palabras
items = data[0].split(' ')

# -- Lista de palabras
words = []

# -- Lista de numeros
nums = []

# -- Recorrer la lista original clasificando los items
# -- en palabras o numeros
for item in items:
    if item.isalpha():
        words.append(item)
    elif item.isdigit():
        nums.append(item)

# -- Imprimir las palabras:
print("PALABRAS:")
for word in words:
    print(f'{word}', end=' ')
print()

# -- Imprimir los numeros
print()
print("NUMEROS:")
for num in nums:
    print(f'{num}', end=' ')
print()
print()
