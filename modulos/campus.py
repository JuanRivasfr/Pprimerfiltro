import os
from .variables import savecampers,aprob,crutas,ctrainer,bcampers,camper,bidcampers, ecampers, ucampers, savetrainers, savetrainers, savetrainers,btrainers, bidtrainers, etrainers, atrainers, crutas, btrutas,idruta,eruta, uruta, cgrupos

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
    savetrainers()
#Accede al menu para leer todos los campers
def buscartrainer(codigo=None):
    print("""
++++++++++++++
+  Trainer/s  +
++++++++++++++
""")
    if(codigo==None):
        btrainers()
    else :
        bidtrainers(codigo)
#Accede al menu para eliminar trainer
def eliminarTrainer(id):
    print("""
++++++++++++++++++++++
+  Eliminar Trainer  +
++++++++++++++++++++++
""")
    etrainers(id)
#Accede al menu para actualizar trainer
def actualizarTrainer(id):
    print("""
+++++++++++++++++++
+  Editar Camper  +
+++++++++++++++++++
""")
    atrainers(id)

#---------------------------------------------------------------------------------------------------------------------------------------------------------
#Accede al metodo para crear rutas
def createrutas():
    #Impresion Menu
    print("""
+++++++++++++++++++
+  Crear Rutas  +
+++++++++++++++++++
""")
    #Se llama al metodo encargado de guardar los campers
    crutas()
#Accede al menu para leer las rutas
def buscarrutas(codigo=None):
    print("""
++++++++++++
+  Ruta/s  +
++++++++++++
""")
    if(codigo==None):
        btrutas()
    else :
        idruta(codigo)
#Accede al metodo para eliminar rutas
def eliminarRuta(Nombre):
    eruta(Nombre)
#Accede al metodo para editar rutas
def actualizarRuta(nombre):
    print("""
++++++++++++++++++
+  Editar Rutas  +
++++++++++++++++++
""")
    uruta(nombre)

#---------------------------------------------------------------------------------------------------------------------------------------------------------
#Accede al metodo para crear grupos
def creategrupos():
    #Impresion Menu
    print("""
++++++++++++++++++
+  Crear Grupos  +
++++++++++++++++++
""")
    #Se llama al metodo encargado de guardar los campers
    cgrupos()
#---------------------------------------------------------------------------------------------------------------------------------------------------------
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
    menu = ["CRUD Campers", "CRUD Trainers", "Gestor de matriculas", "Crear Trainer", "Gestionar Matriculas", "Salir"]
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
                                             createtrainer()
                                        #Accede a buscar trainers y muestra el menu
                                        case 2:
                                            menubuscartrainer = ["Listar todos los trainers", "Listar por id", "Salir"]
                                            while(True):
                                                os.system('cls')
                                                print("""
+++++++++++++++++++
+  Buscar Trainer  +
+++++++++++++++++++
""")
                                                for i, value in enumerate(menubuscartrainer):
                                                    print(f"{i+1}. {value}")
                                                try:
                                                    opc=int(input(":"))
                                                    if(opc<=len(menubuscartrainer) and opc>0):
                                                        match(opc):
                                                            #Accede a listar todos los campers
                                                            case 1:
                                                                buscartrainer()
                                                            #Accede a buscar camper por id
                                                            case 2:
                                                                idt = int(input("Ingrese el id del trainer a buscar: "))
                                                                buscartrainer(idt)
                                                            case 3:
                                                                break
                                                except ValueError:
                                                    print("La opcion no esta habilitada")
                                                    os.system('pause')
                                        #Accede a eliminar trainers
                                        case 3:
                                            idc = int(input("Ingrese el id del trainer a eliminar: "))
                                            eliminarTrainer(idc)
                                        #Accede a actualizar campers
                                        case 4:
                                            idc = int(input("Ingrese el id del trainer a editar: "))
                                            actualizarTrainer(idc)
                                        case 5: 
                                            break
                            except ValueError:
                                print("La opcion no esta habilitada")
                                os.system('pause')   
                    case 3: 
                        menugestion = ["CRUD Rutas", "CRUD Grupos", "Eliminar ruta", "Editar ruta","Salir"]
                        while(True):
                            os.system('cls')
                            print("""
++++++++++++++++++
+  Menu Gestion  +
+++++++++++++++++
                                """)
                            for i,value in enumerate(menugestion):
                                print(f"{i+1}. {value}")
                            try: 
                                opc= int(input(":"))
                                if(opc<=len(menugestion) and opc>0):
                                    match(opc):
                                        #Accede a crear rutas y llama el metodo
                                        case 1:
                                            menurutas = ["Crear Rutas", "Consultar rutas", "Eliminar ruta", "Editar ruta","Salir"]
                                            while(True):
                                                os.system('cls')
                                                print("""
++++++++++++++++
+  Menu Rutas  +
++++++++++++++++
                                                    """)
                                                for i,value in enumerate(menurutas):
                                                    print(f"{i+1}. {value}")
                                                try: 
                                                    opc= int(input(":"))
                                                    if(opc<=len(menurutas) and opc>0):
                                                        match(opc):
                                                            #Accede a crear rutas y llama el metodo
                                                            case 1:
                                                                createrutas()
                                                            #Accede a buscar rutas
                                                            case 2:
                                                                menubuscarrutas = ["Listar todas las rutas", "Listar por nombre", "Salir"]
                                                                while(True):
                                                                    os.system('cls')
                                                                    print("""
+++++++++++++++++++
+  Buscar Rutas  +
+++++++++++++++++++
""")
                                                                    for i, value in enumerate(menubuscarrutas):
                                                                        print(f"{i+1}. {value}")
                                                                    try:
                                                                        opc=int(input(":"))
                                                                        if(opc<=len(menubuscarrutas) and opc>0):
                                                                            match(opc):
                                                                                #Accede a listar todas las rutas
                                                                                case 1:
                                                                                    buscarrutas()
                                                                                #Accede a buscar camper por id
                                                                                case 2:
                                                                                    idt = input("Ingrese el nombre de la ruta a buscar: ")
                                                                                    buscarrutas(idt)
                                                                                case 3:
                                                                                    break
                                                                    except ValueError:
                                                                        print("La opcion no esta habilitada")
                                                                        os.system('pause')
                                                            #Accede a eliminar rutas
                                                            case 3:
                                                                idc = input("Ingrese el nombre de la ruta a eliminar: ")
                                                                eliminarRuta(idc)
                                                            #Accede a actualizar ruta
                                                            case 4:
                                                                idc = input("Ingrese el nombre de la ruta a editar: ")
                                                                actualizarRuta(idc)
                                                            case 5: 
                                                                break
                                                except ValueError:
                                                    print("La opcion no esta habilitada")
                                                    os.system('pause')   
                                        case 2:
                                            menugrupos = ["Crear Grupos", "Consultar Grupos", "Eliminar Grupo", "Editar Grupo","Salir"]
                                            while(True):
                                                os.system('cls')
                                                print("""
++++++++++++++++
+  Menu Rutas  +
++++++++++++++++
                                                    """)
                                                for i,value in enumerate(menugrupos):
                                                    print(f"{i+1}. {value}")
                                                try: 
                                                    opc= int(input(":"))
                                                    if(opc<=len(menugrupos) and opc>0):
                                                        match(opc):
                                                            #Accede a crear grupos y llama el metodo
                                                            case 1:
                                                                creategrupos()
                                                            #Accede a buscar rutas
                                                            case 2:
                                                                menubuscarrutas = ["Listar todas las rutas", "Listar por nombre", "Salir"]
                                                                while(True):
                                                                    os.system('cls')
                                                                    print("""
+++++++++++++++++++
+  Buscar Rutas  +
+++++++++++++++++++
""")
                                                                    for i, value in enumerate(menubuscarrutas):
                                                                        print(f"{i+1}. {value}")
                                                                    try:
                                                                        opc=int(input(":"))
                                                                        if(opc<=len(menubuscarrutas) and opc>0):
                                                                            match(opc):
                                                                                #Accede a listar todas las rutas
                                                                                case 1:
                                                                                    buscarrutas()
                                                                                #Accede a buscar camper por id
                                                                                case 2:
                                                                                    idt = input("Ingrese el nombre de la ruta a buscar: ")
                                                                                    buscarrutas(idt)
                                                                                case 3:
                                                                                    break
                                                                    except ValueError:
                                                                        print("La opcion no esta habilitada")
                                                                        os.system('pause')
                                                            #Accede a eliminar rutas
                                                            case 3:
                                                                idc = input("Ingrese el nombre de la ruta a eliminar: ")
                                                                eliminarRuta(idc)
                                                            #Accede a actualizar ruta
                                                            case 4:
                                                                idc = input("Ingrese el nombre de la ruta a editar: ")
                                                                actualizarRuta(idc)
                                                            case 5: 
                                                                break
                                                except ValueError:
                                                    print("La opcion no esta habilitada")
                                                    os.system('pause')   
                                        case 5: break
                            except ValueError:
                                print("La opcion no esta habilitada")
                                os.system('pause')
                    case 4: ctrainers()
                    case 5: gmatriculas()
                    case 6: break
        except ValueError:
            print("La opcion no esta habilitada")
            os.system('pause')
