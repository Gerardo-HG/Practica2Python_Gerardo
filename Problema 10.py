def generar_formato_correcto(month,day,year):
    if month == "Enero":
        print(f"{year}-{1:02}-{day:02}")
    elif month == "Febrero":
        print(f"{year}-{2:02}-{day:02}")
    elif month == "Marzo":
        print(f"{year}-{3:02}-{day:02}")
    elif month == "Abril":
        print(f"{year}-{4:02}-{day:02}")        
    elif month == "Mayo":
        print(f"{year}-{5:02}-{day:02}")
    elif month == "Junio":
        print(f"{year}-{6:02}-{day:02}")        
    elif month == "Julio":
        print(f"{year}-{7:02}-{day:02}")        
    elif month == "Agosto":
        print(f"{year}-{8:02}-{day:02}")        
    elif month == "Setiembre":
        print(f"{year}-{9:02}-{day:02}")        
    elif month == "Octubre":
        print(f"{year}-{10}-{day:02}")        
    elif month == "Noviembre":
        print(f"{year}-{11}-{day:02}")        
    elif month == "Diciembre":
        print(f"{year}-{12}-{day:02}")   


def generar_formato_correcto_2(month,day,year):
    print("\nFormato Correcto")
    print(f"{year}-{month:02}-{day:02}")
    return True

print("*****FORMATO PARA INGRESO DE FECHA*****")
print("OPCION DE FORMATO DE INGRESO DE FECHA -> Ejemplo: (1. Setiembre 8, 1636 O 2. 8/9/1636)")
fecha=input("Ingrese la fecha en orden mes-dia-año:  ")
opcion=int(input("Ingrese la opcion:  "))

if opcion == 1:
    fecha_separada=fecha.split(",")
    anio=fecha_separada[1].strip()
    #print(fecha_separada[0].split(" "))
    mes=fecha_separada[0].split(" ")[0]
    dia=int(fecha_separada[0].split(" ")[1])
    generar_formato_correcto(mes,dia,anio)
    
elif opcion == 2:
    #9/8/1636
    fecha_separada=fecha.split("/")
    anio=fecha_separada[2]
    dia=int(fecha_separada[0])
    mes=int(fecha_separada[1])
    generar_formato_correcto_2(mes,dia,anio)
    
#print(mes)
#print(dia)    
#print(anio)
