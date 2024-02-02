numeros_ingresados=[]
contador_par=0
contador_impar=0

while(True):
    print("Desea ingresar un número:  ")
    opcion=input(" ")
    if opcion == "SI":
        numero=int(input("Ingrese el número: "))
        numeros_ingresados.append(numero)
    elif opcion == "NO":
        break

for n in numeros_ingresados:
    if n % 2 ==0:
        contador_par+=1
    else:
        contador_impar+=1
print("Numeros ingresados:  ",numeros_ingresados)    
print("Cantidad de números pares:  ",contador_par)
print("Cantidad de números impares: ",contador_impar)
