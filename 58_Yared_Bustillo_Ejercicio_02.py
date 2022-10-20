#EJERCICIO 02
def contar(frase):
    frase = "".join(frase.split(",")).lower()
    ultima_letra = frase[0]
    conteo = 0
    letras = ""
    conteos = ""
    indice = 0
    for letra in frase:
        if letra != ultima_letra:
            letras += ultima_letra + " "
            conteos += str(conteo) + " "
            conteo = 1
            ultima_letra = letra
        else:
            conteo += 1
        if indice+1 >= len(frase):
            letras += ultima_letra+" "
            conteos += str(conteo) + " "
        indice += 1
    return letras, conteos


frase = str(input("Ingrese una palabra o frase: "))
letras, conteos = contar(frase)
print(letras)
print(conteos)
