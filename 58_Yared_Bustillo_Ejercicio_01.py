#EJERCICIO 01
import time

print("POSICION DE LETRAS EN PALABRAS")
print("")
palabra = input("Ingrese una palabra: ")
ultima_l = len(palabra)
ultima_l = palabra[ultima_l-1]
primera_l = palabra[0]

media_l = int(len(palabra)/2)
media_l = palabra[media_l-1]

print("La primera es: ",primera_l,", la media es: ",media_l," y la última es: ",ultima_l)
print("La letra inicial es: ",primera_l)
print("La última letra es: ",ultima_l)
time.sleep(5)
