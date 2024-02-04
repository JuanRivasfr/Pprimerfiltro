import os
rutas = list()
camper = list()
trainer = list()

#--------------------------------------------------------------------------------------------------------------------------------

#CAMPERS

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

#TRAINERS

#Guarda los trainers
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
        "Rutas" : [],
    }
    
    while (True):
        h = int(input("¿Que horarios tiene disponible el trainer? \n1. 6-9AM \n2. 10-12AM \n3. 2-5PM \n4. 6-10PM \n: "))
        if h == 1:
            inft["HorariosD"].append("6-9AM")
        if h == 2:
            inft["HorariosD"].append("10-12AM")
        if h == 3:
            inft["HorariosD"].append("2-5PM")
        if h == 4:
            inft["HorariosD"].append("6-10PM")
        auxe = input("¿Desea agregar otro horario?(Si/No): ")
        if auxe == "No":
            break    
    for i, value in enumerate(trainer):
        if value["Id"] == inft["Id"]:
            print("Ya hay un registro creado con el mismo ID, por favor intente con otro")
            os.system('pause')
            return
    trainer.append(inft)
    print(trainer)
    os.system('pause')
#Busca todos los trainers    
def btrainers():
    for i,value in enumerate(trainer):
        print(f'Id: {value.get("Id")} \nNombre: {value.get("Nombre")} \nApellido: {value.get("Apellido")} \nEdad: {value.get("Edad")}')
        for i1, val in value.items():
            if i1 == "HorariosD":
                print("Horarios:")
                for i2 in (val):
                    print(i2)
        print('\n')
    os.system('pause')
#Busca trainer por id
def bidtrainers(id):
    for i, value in enumerate(trainer):
        if value["Id"] == id:
            print(f'Id: {value.get("Id")} \nNombre: {value.get("Nombre")} \nApellido: {value.get("Apellido")} \nEdad: {value.get("Edad")}')
            for i1, val in value.items():
                if i1 == "HorariosD":
                    print("Horarios:")
                    for i2 in (val):
                        print(i2)
    os.system('pause')
#Eliminar trainers
def etrainers(id):
    for i, value in enumerate(trainer):
        if value["Id"] == id:
            print(f'Id: {value.get("Id")} \nNombre: {value.get("Nombre")} \nApellido: {value.get("Apellido")} \nEdad: {value.get("Edad")}')
            for i1, val in value.items():
                if i1 == "HorariosD":
                    print("Horarios:")
                    for i2 in (val):
                        print(i2)
            auxe = input("¿Esta seguro que desea eliminar el trainer?(Si/No): ")
            if auxe == "Si":
                trainer.pop(i)
                print(trainer)
    os.system('pause')
#Actualizar trainers
def atrainers(id):
    for i, value in enumerate(trainer):
        if value["Id"] == id:
            print(f'Id: {value.get("Id")} \nNombre: {value.get("Nombre")} \nApellido: {value.get("Apellido")} \nEdad: {value.get("Edad")}')
            for i1, val in value.items():
                if i1 == "HorariosD":
                    print("Horarios:")
                    for i2 in (val):
                        print(i2)
            auxe = input("¿Esta seguro que desea editar el trainer?(Si/No): ")
            if auxe == "Si":
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
                "Rutas" : [],
                }

                while (True):
                    h = int(input("¿Que horarios tiene disponible el trainer? \n1. 6-9AM \n2. 10-12AM \n3. 2-5PM \n4. 6-10PM \n: "))
                    if h == 1:
                        inft["HorariosD"].append("6-9AM")
                    if h == 2:
                        inft["HorariosD"].append("10-12AM")
                    if h == 3:
                        inft["HorariosD"].append("2-5PM")
                    if h == 4:
                        inft["HorariosD"].append("6-10PM")
                    auxe = input("¿Desea agregar otro horario?(Si/No): ")
                    if auxe == "No":
                        break    
                for i, value in enumerate(trainer):
                    if value["Id"] == inft["Id"]:
                        print("Ya hay un registro creado con el mismo ID, por favor intente con otro")
                        os.system('pause')
                        return
                trainer[i] = inft
    print(trainer)
    os.system('pause')
                
#--------------------------------------------------------------------------------------------------------------------------------

#RUTAS

#Creacion de rutas
def crutas():
    inf = { 
        "Nombre": input("Ingrese el nombre de la ruta: "),
        "FPOO" : ["Introduccion a la algoritmia", "PSeInt", "Python"],
        "PWEB" : ["HTML", "CSS", "Bootstrap"],
        "PFORMAL" : ["Java", "JavaScript", "C#"],
        "BD" : {
            "Principal" : input("Ingrese la Base de Datos Principal: "),
            "Secundaria" : input("Ingrese la Base de Datos Secundaria: ")
            },
        "BEND" : [],
    }
    while (True):
        aux1 = int(input("¿Que temas desea agregar en el apartado BackEnd?: \n1.NetCore \n2.Spring Boot \n3.NodeJS \n4.Express \n5.Otro \n: "))
        if aux1 == 1:
            inf["BEND"].append("NetCore")
        if aux1 == 2:
            inf["BEND"].append("Spring Boot")
        if aux1 == 3:
            inf["BEND"].append("NodeJS")
        if aux1 == 4:
            inf["BEND"].append("Express")
        if aux1 == 5:
            otro = input("Ingrese el tema a ver: ")
            inf["BEND"].append(otro)
        auxe = input("¿Desea agregar otro tema?(Si/No): ")
        if auxe == "No":
            break
    rutas.append(inf)
    print(rutas)
    os.system('pause')
#Mostrar todas las rutas
def btrutas():
    for i,value in enumerate(rutas):
        print("----------------")
        print(f'Nombre: {value.get("Nombre")}')
        print("----------------")
        for i1, val in value.items():
            if i1 == "FPOO":
                print("Fundamentos de Programacion:")
                for i2 in (val):
                    print(i2)
                print("----------------")
            if i1 == "PWEB":
                print("Progamacion web:")
                for i2 in (val):
                    print(i2)
                print("----------------")
            if i1 == "PFORMAL":
                print("Progamacion formal:")
                for i2 in (val):
                    print(i2)
                print("----------------")
        print(f'Base de datos principal: {value["BD"].get("Principal")} \nBase de datos secundario: {value["BD"].get("Secundaria")}\n----------------')
        for header, contenido in value.items():
            if header == "BEND":
                print("Backend:")
                for index in contenido:
                    print(index)
        print('\n')
    os.system('pause')
#Mostrar una sola ruta
def idruta(nombre):
    for i,value in enumerate(rutas):
        if value["Nombre"] == nombre:
            print("----------------")
            print(f'Nombre: {value.get("Nombre")}')
            print("----------------")
            for i1, val in value.items():
                if i1 == "FPOO":
                    print("Fundamentos de Programacion:")
                    for i2 in (val):
                        print(i2)
                    print("----------------")
                if i1 == "PWEB":
                    print("Progamacion web:")
                    for i2 in (val):
                        print(i2)
                    print("----------------")
                if i1 == "PFORMAL":
                    print("Progamacion formal:")
                    for i2 in (val):
                        print(i2)
                    print("----------------")
            print(f'Base de datos principal: {value["BD"].get("Principal")} \nBase de datos secundario: {value["BD"].get("Secundaria")}\n----------------')
            for header, contenido in value.items():
                if header == "BEND":
                    print("Backend:")
                    for index in contenido:
                        print(index)
            print('\n')
    os.system('pause')
#Eliminar ruta
def eruta(nombre):
    for i, value in enumerate(rutas):
        if value["Nombre"] == nombre:
            print("----------------")
            print(f'Nombre: {value.get("Nombre")}')
            print("----------------")
            for i1, val in value.items():
                if i1 == "FPOO":
                    print("Fundamentos de Programacion:")
                    for i2 in (val):
                        print(i2)
                    print("----------------")
                if i1 == "PWEB":
                    print("Progamacion web:")
                    for i2 in (val):
                        print(i2)
                    print("----------------")
                if i1 == "PFORMAL":
                    print("Progamacion formal:")
                    for i2 in (val):
                        print(i2)
                    print("----------------")
            print(f'Base de datos principal: {value["BD"].get("Principal")} \nBase de datos secundario: {value["BD"].get("Secundaria")}\n----------------')
            for header, contenido in value.items():
                if header == "BEND":
                    print("Backend")
                    for index in contenido:
                        print(index)
            opc = input("¿Esta seguro que desea eliminar la ruta?(Si/No)")
            if opc == "Si":
                rutas.pop(i)
                print("Se ha eliminado el registro")
    print(rutas)
    os.system('pause')

def uruta(nombre):
    for i, value in enumerate(rutas):
        if value["Nombre"] == nombre:
            print("----------------")
            print(f'Nombre: {value.get("Nombre")}')
            print("----------------")
            for i1, val in value.items():
                if i1 == "FPOO":
                    print("Fundamentos de Programacion:")
                    for i2 in (val):
                        print(i2)
                    print("----------------")
                if i1 == "PWEB":
                    print("Progamacion web:")
                    for i2 in (val):
                        print(i2)
                    print("----------------")
                if i1 == "PFORMAL":
                    print("Progamacion formal:")
                    for i2 in (val):
                        print(i2)
                    print("----------------")
            print(f'Base de datos principal: {value["BD"].get("Principal")} \nBase de datos secundario: {value["BD"].get("Secundaria")}\n----------------')
            for header, contenido in value.items():
                if header == "BEND":
                    print("Backend:")
                    for index in contenido:
                        print(index)
            opc = input("¿Esta seguro que desea editar la ruta?(Si/No)")
            if opc == "Si":
                inf = { 
                    "Nombre": input("Ingrese el nombre de la ruta: "),
                    "FPOO" : [],
                    "PWEB" : [],
                    "PFORMAL" : [],
                    "BD" : {
                        "Principal" : input("Ingrese la Base de Datos Principal: "),
                        "Secundaria" : input("Ingrese la Base de Datos Secundaria: ")
                        },
                    "BEND" : [],
                }
                while (True):
                    aux1 = input("¿Que temas desea agregar en el apartado Fundamentos de Programacion? \n: ")
                    inf["FPOO"].append(aux1)
                    auxe = input("¿Desea agregar otro tema?(Si/No): ")
                    if auxe == "No":
                        break
                while (True):    
                    aux1 = input("¿Que temas desea agregar en el apartado de Programacion Web? \n: ")
                    inf["PWEB"].append(aux1)
                    auxe = input("¿Desea agregar otro tema?(Si/No): ")
                    if auxe == "No":
                        break
                while (True):    
                    aux1 = input("¿Que temas desea agregar en el apartado de Programacion Formal? \n: ")
                    inf["PFORMAL"].append(aux1)
                    auxe = input("¿Desea agregar otro tema?(Si/No): ")
                    if auxe == "No":
                        break
                while (True):
                    aux1 = input("¿Que temas desea agregar en el apartado de Back End \n: ")
                    inf["BEND"].append(aux1)
                    auxe = input("¿Desea agregar otro tema?(Si/No): ")
                    if auxe == "No":
                        break
                rutas[i] = inf
    print(rutas)
    os.system('pause')
                
    
#--------------------------------------------------------------------------------------------------------------------------------
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