import random   

alumnos=[]

def menu():
    while True():
        print("1.Registrar alumno")
        print("2.Listar todos los alumnos")
        print("3.Buscar alumnos por nivel")
        print("4.Salir del programa y guardar")

        opcion=int(input("Selecciona la Opcion que desea : "))
        
        if opcion==1:
            registrar()
        elif opcion==2:
            listar()
        elif opcion==3:
            busc_nivel()
        elif opcion==4:
            busc_nivel()




def registrar():
    nombre=input("Ingresa el nombre del Alumno:  ")
    apellido=input("Ingresa el apellido del Alumno:   ")
    edad=int(input("Ingresa edad del Alumno: "))
    nivel=input("Ingresa , Nivel (Ejemplo: 1°, 2°, 3°, etc.):  ")
    notas=[random.randint(1,10) for _ in range(5)]
    
    alumno ={
        "nombre" : nombre,
        "apellido" :apellido,
        "edad" : edad,
        "nivel" : nivel,
        "notas": notas 
    }
    alumnos.append(alumno)
    print("Alumno Registrado!   ")


def listar():
    if not alumnos:
        print("NO HAY ALUMNOS EN EL REGISTRO ! ")
    else:
        for alumno in alumnos:
            print(f"Nombre:{alumno['nombre']}, Apellido:{alumno['apellido']} , Nivel:{alumno['nivel']}")


def busc_nivel():
    nive_buscado=input("ingrese el nivel a buscar:  ")
    encontrados=[alumno for alumno in alumnos if alumno['nivel']==nivel_buscado]
        if not encontrados:
            print(f"NO HAY ALUMNOS EN EL NIVEL {nivel_buscado}")
        else
            for alumno in encontrados:
                 print(f"Nombre:{alumno['nombre']}, Apellido:{alumno['apellido']} , Nivel:{alumno['nivel']}")

def guardar_Data():
    with open("alumnos.txt", "w") as archivo: 
        for alumno in alumnos:
            archivo.write(f"{alumno['nombre']},{apellido['apellido']},{edad['edad']}.{nivel['nivel']}")
            print("DATA GUARDADA! ")
    breaks