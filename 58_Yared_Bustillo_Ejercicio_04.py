#EJERCICIO 04
#Elabore un programa que indique cuantas mayúsculas y minúsculas hay en una cadena de caracteres ingresada por teclado.
cadena = input("Ingrese una palabra: ")
indice=0
mayusculas=0
minusculas=0
while indice < len(cadena):
  letra = cadena[indice]
  if letra.isupper() == True:
    mayusculas +=1
  else:
    minusculas +=1
  indice += 1

print("Total mayusculas: " , mayusculas)
print("Total minusculas: " , minusculas)
