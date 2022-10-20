#EJERCICIO 05
def espacio(cadena): 
    contar = 0
    for i in range(0, len(cadena)):      
        if cadena[i] == " ": 
            contar += 1
    return contar 
cadena = str(input("Ingrese la palabra o frase: "))
print("Numero de espacios: ",espacio(cadena)) 
