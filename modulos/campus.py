import os
from .variables import save,aprob,crutas,ctrainer,camper

menuu = ("""
+++++++++++++++++++++++++++++++
+  Menu Registro CampusLands  +
+++++++++++++++++++++++++++++++
""")
#Creacion campers
def create():
    #Impresion Menu
    print(menuu)
    #Se llama al metodo encargado de guardar los campers
    save()
    
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
    menu = ["CRUD CAMPERS", "Registro pruebas", "Crear Rutas", "Crear Trainer", "Gestionar Matriculas"]
    while(True):
        os.system('cls')
        print("""
+++++++++++++++++++++++++++++++
+  Menu Registro CampusLands  +
+++++++++++++++++++++++++++++++
""")
        for i,value in enumerate(menu):
            print(f"{i+1}. {value}")
        try:
            opc = int(input(":"))
            #Condicion para entrar al menu
            if(opc<=len(menu) and opc>0):
                match(opc):
                    case 1: 
                        while(True):
                            os.sytem('cls')
                            print("""
                                ++++++++++++++++++
                                +  Menu Campers  +
                                ++++++++++++++++++
                                """)
                            menu = ["Crear campers", "Buscar campers", "Eliminar campers", "Editar campers"]
                            for i,value in enumerate(menu):
                                print(f"{i+1}. {value}")
                            try: 
                                opc= int(input(":"))
                                if(opc<=len(menu) and opc>0):
                                    match(opc):
                                        case 1:
                                            save()
                            except ValueError:
                                print("La opcion no esta habilitada")
                                os.system('pause')   
                    case 2: updpruebas()
                    case 3: rutas()
                    case 4: ctrainers()
                    case 5: gmatriculas()
        except ValueError:
            print("La opcion no esta habilitada")
            os.system('pause')
