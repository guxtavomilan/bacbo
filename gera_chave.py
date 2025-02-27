
def aleatoria():
    import random as rd
    import string

    letras = list(string.ascii_uppercase) #lista com letras maiusculas
    numeros = list(string.digits) #lista com numeros de 0 a 9
    caracteres = letras + numeros + numeros #para numeros e letras aparecerem em proporções menos desiguais

    sorteio = rd.choices(caracteres, k=5)

    chave = ''.join(sorteio)
    
    return chave