def contar_digito(numero,digito):
    lista=[]
    for n in numero:
        
        lista.append(n)
    
    print("Número ingresado: ",numero)
    print("Cantidad de veces {} en el número: {}".format(digito,lista.count(digito)))
contar_digito("15789000","0")
