frase=input("Ingrese la frase completa:  ")
def omitir_vocales(palabra):
    lista=[]
    for i in palabra:
        if i != 'a' and i != 'e' and i !='i' and i!='o' and i!='u':
            lista.append(i)
    print("".join(lista))    
omitir_vocales(frase)
