#Ejercicio 4
#Los teléfonos de una empresa
#tienen el siguiente formato
#prefijo-número-extension donde
#el prefijo es el código del país
#+34, y la extensión tiene dos dígitos
#(por ejemplo +34-913724710-56).
#Escribir un programa que pregunte por
#un número de teléfono con este formato y
#muestre por pantalla el número de teléfono
#sin el prefijo y la extensión.

# Solicita el número de teléfono al usuario
telefono = input("Por favor, ingresa el número de teléfono en el formato +34-XXXXXXX-XX: ")

# Extrae solo el número sin el prefijo y la extensión
numero_sin_prefijo_extension = telefono.split('-')[1]

# Muestra el número de teléfono sin el prefijo y la extensión
print("Número de teléfono sin prefijo y extensión:", numero_sin_prefijo_extension)


