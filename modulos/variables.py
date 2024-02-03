import os
rutas = list()
camper = list()
trainers = list()
#Guarda los campers
def save():
    inf = { 
        "Id" : int(input("Ingrese el id del camper: ")),
        "Nombre": input("Ingrese el nombre del camper: "),
        "Apellido" : input("Ingrese el apellido del camper: "),
        "Direccion" : input("Ingrese la direccion del camper: "),
        "Acudiente" : input("Ingrese el nombre del acudiente del camper: "),
        "Telefono" : [
            {
                f"{'Fijo' if(int(input('1. Fijo 0. Celular: '))) else 'Celular'}":
                input(f'Numero de contacto{x+1}: ')
            }
            for x in range((int(input("¿Cuantos numeros de contacto tiene?: "))))
        ],
        "Estado" : "",
        "Ruta" : "",
        "Area" : "",
    }
    camper.append(inf)
    print(camper)
    os.system('pause')
    
def aprob(id):
    for i,value in enumerate(camper):
        if value["Id"] == id:  
            teo = int(input("Ingrese la nota de la prueba teorica: "))
            prac = int(input("Ingrese la nota de la prueba practica: "))
            prom = (teo + prac) / 2
            if prom >= 60:
                ap = str("Aprobado")
            else: 
                ap = str("Desaprobado")
            inf = {
                 "Nota teorica" : teo,
                 "Nota practica" : prac,
                 "EstAprobado" : ap,
             }
            camper[i]["Pruebas"] = inf
            print(camper) 
    os.system('pause')
    
def crutas():
    inf = {
        "Nombre ruta" : input("Ingrese el nombre de la ruta: "),
        "Fundamentos de programacion" : input("Ingrese los fundamentos de programacion a ver(Introducción a la algoritmia, PSeInt y Python): "), 
        "Programación Web" : input("Ingrese los temas de programacion a ver(HTML, CSS y Bootstrap): "), 
        "Programación formal" : input("Ingrese los temas a ver en programacion formal(Java, JavaScript, C#): "), 
        "Bases de datos" : input("Ingrese las bases de datos a ver(Mysql, MongoDb y Postgresql) \nCada ruta tiene un SGDB principal y un alternativo: "),
        "Backend" : input("Ingrese los temas a ver en Backend(NetCore, Spring Boot, NodeJS y Express): ")
    }
    rutas.append(inf)
    print(rutas)
    os.system('pause')
    
def ctrainer():
    inf = {
        "Nombre" : input("Ingrese el nombre completo del trainer: "),
        "Horario" : {
            "Mañana" : {
                "Disph1" : "",
                "Disph2" : ""
            },
            "Tarde" : {
                "Disph1" : "",
                "Disph2" : ""
            }
        }
    }
    trainers.append(inf)
    print(trainers)
    os.system('pause')
    
def maprobados():
    for iexterno in camper:
        print(iexterno)
        for i, value in iexterno.items():
            print(value)
            print(i)