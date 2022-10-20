def contar(entrada):
    entrada = "".join(entrada.split(",")).upper()
    ultima_letra = entrada[0]
    conteo = 0
    letras = ""
    conteos = ""
    indice = 0
    for letra in entrada:
        if letra != ultima_letra:
            letras += ultima_letra + " "
            conteos += str(conteo) + " "
            conteo = 1
            ultima_letra = letra
        else:
            conteo += 1
        if indice+1 >= len(entrada):
            letras += ultima_letra+" "
            conteos += str(conteo) + " "
        indice += 1
    return letras, conteos
entrada = "E,E,e,E,E,d,E,E,D,c,C,E,E,B,E,E,a,E,A,E,g,E,G,E,f,E,f"
letras, conteos = contar(entrada)
print(letras)
print(conteos)
