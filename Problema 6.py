def serie_fibonacci(numero):
    lista=[]
    a=0
    b=1
    for i in range(numero):
        if a > numero:
            break
        else:        
            #0, 1, 1, 2, 3,
            lista.append(a)
            c=a+b #1 2 3 5 8
            a=b   #1 1 2 3 5
            b=c   #1 2  3 5 8
    print("Serie de Fibonnaci hasta {}".format(numero))
    for n in lista:
        print(n,end=' ')
serie_fibonacci(50)
