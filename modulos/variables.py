import os
rutas = list()
camper = list()
trainer = list()
#Guarda los campers
def savecampers():
    inf = { 
        "Id" : int(input("Ingrese el id del camper: ")),
        "Nombre": input("Ingrese el nombre del camper: "),
        "Apellido" : input("Ingrese el apellido del camper: "),
        "Edad" : int(input("Ingrese la edad del camper: ")),
        "Direccion" : input("Ingrese la direccion del camper: "),
        "Acudiente" : {},
        "Telefono" : [
            {
                f"{'Fijo' if(int(input('0. Celular 1. Fijo : '))) else 'Celular'}":
                int(input(f'Numero de contacto {x+1}: '))
            }
            for x in range((int(input("¿Cuantos numeros de contacto tiene?: "))))
        ],
        "Estado" : "",
        "Ruta" : "",
        "Area" : "",
    }
    if inf["Edad"] < 18:
        infaux = {
                "Nombre" : input("Ingrese el nombre del acudiente del menor: "),
                "Id" : input("Ingrese el id del acudiente del menor: ")
            }
        inf["Acudiente"] = infaux
    else :
        del inf["Acudiente"]
    for i, value in enumerate(camper):
        if value["Id"] == inf["Id"]:
            print("Ya hay un registro creado con el mismo ID, por favor intente con otro")
            os.system('pause')
            return
    camper.append(inf)
    print(camper)
    os.system('pause')
#Busca todos los campers
def bcampers():
    for i,value in enumerate(camper):
        print(f'Id: {value.get("Id")} \nNombre: {value.get("Nombre")} \nApellido: {value.get("Apellido")} \nEdad: {value.get("Edad")} \nEstado: {value.get("Estado")} \nRuta : {value.get("Ruta")} \n')
    os.system('pause')
#Busca un solo camper
def bidcampers(id):
    for i, value in enumerate(camper):
        if value["Id"] == id:
            print(f'Id: {value.get("Id")} \nNombre: {value.get("Nombre")} \nApellido: {value.get("Apellido")} \nEdad: {value.get("Edad")} \nEstado: {value.get("Estado")} \nRuta : {value.get("Ruta")} \n')
    os.system('pause')
#Elimina un camper
def ecampers(id):
    for i, value in enumerate(camper):
        if value["Id"] == id:
            print(f'Id: {value.get("Id")} \nNombre: {value.get("Nombre")} \nApellido: {value.get("Apellido")} \nEdad: {value.get("Edad")} \nEstado: {value.get("Estado")} \nRuta : {value.get("Ruta")} \n')
            auxe = input("¿Esta seguro que desea eliminar el camper?(Si/No): ")
            if auxe == "Si":
                camper.pop(i)
                print(camper)
    os.system('pause')
#Edita un camper
def ucampers(id):
    for i, value in enumerate(camper):
        if value["Id"] == id:
            print(f'Id: {value.get("Id")} \nNombre: {value.get("Nombre")} \nApellido: {value.get("Apellido")} \nEdad: {value.get("Edad")} \nEstado: {value.get("Estado")} \nRuta : {value.get("Ruta")} \n')
            auxe = input("¿Esta seguro que desea editar el camper?(Si/No): ")
            
            if auxe == "Si":
                inf = { 
                        "Id" : int(input("Ingrese el id del camper: ")),
                        "Nombre": input("Ingrese el nombre del camper: "),
                        "Apellido" : input("Ingrese el apellido del camper: "),
                        "Edad" : int(input("Ingrese la edad del camper: ")),
                        "Direccion" : input("Ingrese la direccion del camper: "),
                        "Acudiente" : {},
                        "Telefono" : [
                            {
                                f"{'Fijo' if(int(input('0. Celular 1. Fijo : '))) else 'Celular'}":
                                int(input(f'Numero de contacto {x+1}: '))
                            }
                            for x in range((int(input("¿Cuantos numeros de contacto tiene?: "))))
                        ],
                        "Estado" : "",
                        "Ruta" : "",
                        "Area" : "",
                }
                if inf["Edad"] < 18:
                    infaux = {
                            "Nombre" : input("Ingrese el nombre del acudiente del menor: "),
                            "Id" : input("Ingrese el id del acudiente del menor: ")
                        }
                    inf["Acudiente"] = infaux
                else :
                    del inf["Acudiente"]
                for i, value in enumerate(camper):
                    if value["Id"] == inf["Id"]:
                        print("Ya hay un registro creado con el mismo ID, por favor intente con otro")
                        os.system('pause')
                        return
                    
                camper[i] = inf
    print(camper)
    os.system('pause')

#--------------------------------------------------------------------------------------------------------------------------------

def savetrainers():
    inft = { 
        "Id" : int(input("Ingrese el id del trainer: ")),
        "Nombre": input("Ingrese el nombre del trainer: "),
        "Apellido" : input("Ingrese el apellido del trainer: "),
        "Edad" : int(input("Ingrese la edad del trainer: ")),
        "Direccion" : input("Ingrese la direccion del trainer: "),
        "HorariosD" : [],
        "Telefono" : [
            {
                f"{'Fijo' if(int(input('0. Celular 1. Fijo : '))) else 'Celular'}":
                int(input(f'Numero de contacto {x+1}: '))
            }
            for x in range((int(input("¿Cuantos numeros de contacto tiene?: "))))
        ],
        "Rutas" : "",
    }
     h = input("¿Que horarios tiene disponible el trainer? \n1.6-9AM \n2.10-12AM \n3.2-5PM \n4.6-10PM \n: ")
    for i, value in enumerate(trainer):
        if value["Id"] == inft["Id"]:
            print("Ya hay un registro creado con el mismo ID, por favor intente con otro")
            os.system('pause')
            return
    trainer.append(inft)
    print(trainer)
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
            
def exitaux():
    pass