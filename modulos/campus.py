import os
from .variables import save,aprob,crutas,ctrainer,camper

#Creacion campers
def create():
    #Impresion Menu
    print("""
+++++++++++++++++++++++++++++++
+  Menu Registro CampusLands  +
+++++++++++++++++++++++++++++++
""")
    #Se llama al metodo encargado de guardar los campers
    save()
    
def updpruebas():
    #Impresion Menu
    print("""
+++++++++++++++++++++++++++++++
+  Menu Registro CampusLands  +
+++++++++++++++++++++++++++++++
""")
    id = int(input("Ingrese el id del camper: "))
    #Se llama al metodo que hara el update
    aprob(id)

def rutas():
    print("""
+++++++++++++++++++++++++++++++
+  Menu Registro CampusLands  +
+++++++++++++++++++++++++++++++
""")
    crutas()
    
def ctrainers():
    print("""
+++++++++++++++++++++++++++++++
+  Menu Registro CampusLands  +
+++++++++++++++++++++++++++++++
""") 
    ctrainer()

def gmatriculas():
    print("""
+++++++++++++++++++++++++++++++
+  Menu Registro CampusLands  +
+++++++++++++++++++++++++++++++
""")
    for i in camper:
        if i["Pruebas"]["EstAprobado"] == "Aprobado":
            print(f"Nombre: {i['Nombre']} \nID: {i['Id']} \n Estado: {i['Pruebas']['EstAprobado']}")
                
    os.system('pause')
    
def menu():

    #Guarda las opciones del menu en un array
    menu = ["Crear camper", "Registro pruebas", "Crear Rutas", "Crear Trainer", "Gestionar Matriculas"]
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
                    case 1: create()
                    case 2: updpruebas()
                    case 3: rutas()
                    case 4: ctrainers()
                    case 5: gmatriculas()
        except ValueError:
            print("La opcion no esta habilitada")
            os.system('pause')
