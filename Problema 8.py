dato=int(input("Ingrese el numero a calcular el factorial:  "))

def factorial_numero(numero):
    resultado=1
    for n in range(1,numero+1,1):
        resultado*=n
    print(resultado)

factorial_numero(dato)
