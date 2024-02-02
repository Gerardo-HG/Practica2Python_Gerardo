print("**************")
cantidad=int(input("Ingrese la cantidad de alumnos a registrar:  "))

lista_alumnos=[]

for c in range(cantidad):
        nombre=input("Ingrese el nombre del alumno:  ")
        notas_alumno=[]
        for n in range(3):
            nota=int(input("Ingrese la nota[]->: "))
            
            notas_alumno.append(nota)
            

        diccionario_alumno={"Alumno":nombre,"Notas":notas_alumno}
        lista_alumnos.append(diccionario_alumno) 
print(lista_alumnos)
