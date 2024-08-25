#Ejercicio 7
#Escribir un programa que pregunte
#el correo electrónico del usuario
#en la consola y muestre por pantalla
#otro correo electrónico con el mismo
#nombre (la parte delante de la arroba @)
#pero con dominio ceu.es.

# Solicita el correo electrónico al usuario
correo = input("Por favor, ingresa tu correo electrónico: ")

nombre_usuario = correo.split('@')[0]

nuevo_correo = nombre_usuario + "@ceu.es"

print("Nuevo correo electrónico:", nuevo_correo)
