def es_primo_o_no(numero):
    n=2
    contador=0
    for i in range(n,numero+1,1):
        if numero % i ==0:
            contador+=1
        
    if contador>2:
        print("El número {} no es primo, es compuesto".format(numero))
    else:
        print("El número {} es primo".format(numero))

es_primo_o_no(14)
es_primo_o_no(7)
