#EJERCICIO 05
#Un programa que ingrese una cadena, muestre cuantos espacios hay en ella.
def espacio(cadena): 
    contar = 0
    for i in range(0, len(cadena)):      
        if cadena[i] == " ": 
            contar += 1
    return contar 
cadena = str(input("Ingrese la palabra o frase: "))
print("Numero de espacios: ",espacio(cadena)) 
