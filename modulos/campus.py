import os
from .variables import savecampers,aprob,crutas,ctrainer,bcampers,camper,bidcampers, ecampers, ucampers

menuu = ("""
+++++++++++++++++++++++++++++++
+  Menu Registro CampusLands  +
+++++++++++++++++++++++++++++++
""")
#Creacion campers
def createcamper():
    #Impresion Menu
    print("""
++++++++++++++++++
+  Crear Camper  +
++++++++++++++++++
""")
    #Se llama al metodo encargado de guardar los campers
    savecampers()
#Busca todos los campers
def buscarcamper(codigo=None):
    print("""
++++++++++++++
+  Camper/s  +
++++++++++++++
""")
    if(codigo==None):
        bcampers()
    else :
        bidcampers(codigo)
#Elimina los campers
def eliminarCamper(id):
    os.system('cls')
    print("""
+++++++++++++++++++++
+  Eliminar Camper  +
+++++++++++++++++++++
""")
    ecampers(id)
#Actualiza los campers
def actualizarCamper(id):
    print("""
+++++++++++++++++++
+  Editar Camper  +
+++++++++++++++++++
""")
    ucampers(id)

#---------------------------------------------------------------------------------------------------------------------------------------------------------
#Accede al metodo para crear trainers
def createtrainer():
    #Impresion Menu
    print("""
+++++++++++++++++++
+  Crear Trainer  +
+++++++++++++++++++
""")
    #Se llama al metodo encargado de guardar los campers
    savecampers()

def updpruebas():
    #Impresion Menu
    print(menuu)
    id = int(input("Ingrese el id del camper: "))
    #Se llama al metodo que hara el update
    aprob(id)

def rutas():
    print(menuu)
    crutas()
    
def ctrainers():
    print(menuu)
    ctrainer()

def gmatriculas():
    print(menuu)
    for i in camper:
        if i["Pruebas"]["EstAprobado"] == "Aprobado":
            print(f"Nombre: {i['Nombre']} \nID: {i['Id']} \n Estado: {i['Pruebas']['EstAprobado']}")
                
    os.system('pause')
    
def menu():

    #Guarda las opciones del menu en un array
    menu = ["CRUD Campers", "CRUD trainers", "Crear Rutas", "Crear Trainer", "Gestionar Matriculas", "Salir"]
    while(True):
        os.system('cls')
        print("""
++++++++++++++++++++++++++++++++
+  Administracion CampusLands  +
++++++++++++++++++++++++++++++++
            """)
        for i,value in enumerate(menu):
            print(f"{i+1}. {value}")
        try:
            opc = int(input(":"))
            #Condicion para entrar al menu
            if(opc<=len(menu) and opc>0):
                match(opc):
                    #Accede al menu de crud campers, crear, buscar, actualizar y eliminar
                    case 1: 
                        menucamper = ["Crear campers", "Buscar campers", "Eliminar campers", "Editar campers","Salir"]
                        while(True):
                            os.system('cls')
                            print("""
++++++++++++++++++
+  Menu Campers  +
++++++++++++++++++
                                """)
                            for i,value in enumerate(menucamper):
                                print(f"{i+1}. {value}")
                            try: 
                                opc= int(input(":"))
                                if(opc<=len(menucamper) and opc>0):
                                    match(opc):
                                        #Accede a crear campers y llama el metodo
                                        case 1:
                                             createcamper()
                                        #Accede a buscar campers y muestra el menu
                                        case 2:
                                            menubuscarcamper = ["Listar todos los campers", "Listar por id", "Salir"]
                                            while(True):
                                                os.system('cls')
                                                print("""
+++++++++++++++++++
+  Buscar Camper  +
+++++++++++++++++++
""")
                                                for i, value in enumerate(menubuscarcamper):
                                                    print(f"{i+1}. {value}")
                                                try:
                                                    opc=int(input(":"))
                                                    if(opc<=len(menubuscarcamper) and opc>0):
                                                        match(opc):
                                                            #Accede a listar todos los campers
                                                            case 1:
                                                                buscarcamper()
                                                            #Accede a buscar camper por id
                                                            case 2:
                                                                idc = int(input("Ingrese el id del camper a buscar: "))
                                                                buscarcamper(idc)
                                                            case 3:
                                                                break
                                                except ValueError:
                                                    print("La opcion no esta habilitada")
                                                    os.system('pause')
                                        #Accede a eliminar campers
                                        case 3:
                                            idc = int(input("Ingrese el id del camper a eliminar: "))
                                            eliminarCamper(idc)
                                        case 4:
                                            idc = int(input("Ingrese el id del camper a editar: "))
                                            actualizarCamper(idc)
                                        case 5: 
                                            break
                            except ValueError:
                                print("La opcion no esta habilitada")
                                os.system('pause')   
                    case 2: 
                        menutrainer = ["Crear trainer", "Buscar trainer", "Eliminar trainer", "Editar trainer","Salir"]
                        while(True):
                            os.system('cls')
                            print("""
+++++++++++++++++++
+  Menu Trainers  +
+++++++++++++++++++
                                """)
                            for i,value in enumerate(menutrainer):
                                print(f"{i+1}. {value}")
                            try: 
                                opc= int(input(":"))
                                if(opc<=len(menutrainer) and opc>0):
                                    match(opc):
                                        #Accede a crear trainers y llama el metodo
                                        case 1:
                                             createcamper()
                                        #Accede a buscar campers y muestra el menu
                                        case 2:
                                            menubuscarcamper = ["Listar todos los campers", "Listar por id", "Salir"]
                                            while(True):
                                                os.system('cls')
                                                print("""
+++++++++++++++++++
+  Buscar Camper  +
+++++++++++++++++++
""")
                                                for i, value in enumerate(menubuscarcamper):
                                                    print(f"{i+1}. {value}")
                                                try:
                                                    opc=int(input(":"))
                                                    if(opc<=len(menubuscarcamper) and opc>0):
                                                        match(opc):
                                                            #Accede a listar todos los campers
                                                            case 1:
                                                                buscarcamper()
                                                            #Accede a buscar camper por id
                                                            case 2:
                                                                idc = int(input("Ingrese el id del camper a buscar: "))
                                                                buscarcamper(idc)
                                                            case 3:
                                                                break
                                                except ValueError:
                                                    print("La opcion no esta habilitada")
                                                    os.system('pause')
                                        #Accede a eliminar campers
                                        case 3:
                                            idc = int(input("Ingrese el id del camper a eliminar: "))
                                            eliminarCamper(idc)
                                        case 4:
                                            idc = int(input("Ingrese el id del camper a editar: "))
                                            actualizarCamper(idc)
                                        case 5: 
                                            break
                            except ValueError:
                                print("La opcion no esta habilitada")
                                os.system('pause')   
                    case 3: rutas()
                    case 4: ctrainers()
                    case 5: gmatriculas()
                    case 6: break
        except ValueError:
            print("La opcion no esta habilitada")
            os.system('pause')
