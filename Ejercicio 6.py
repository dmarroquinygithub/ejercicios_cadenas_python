#Ejercicio 6
#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después
#muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

# Solicita una frase al usuario
frase = input("Por favor, ingresa una frase: ")

# Solicita una vocal al usuario
vocal = input("Por favor, ingresa una vocal: ")

# Reemplaza la vocal por su versión en mayúscula
frase_modificada = frase.replace(vocal, vocal.upper())

# Muestra la frase con la vocal en mayúscula
print("Frase con la vocal en mayúscula:", frase_modificada)

