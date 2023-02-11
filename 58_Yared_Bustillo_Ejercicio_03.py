#EJERCICIO 03
#Un programa que pida el ingreso de una cadena e indique si esta inicia con letra mayúscula o minúscula.
print("Ejercicio 03")
palabra = str(input("Ingrese una palabra: "))

letra1 = palabra[0]
if palabra[0].isupper():
    print("Es mayuscula")
else:
    print("Es minuscula")


