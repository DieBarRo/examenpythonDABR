#Modulo donde se guarda el diseño de y funcionalidad de los menus del programa

import os

#opciones del menu principal
def menuPrincipal():
    menu = input('''
--------------------------------------------
-------------MENU PRINCIPAL-----------------
--------------------------------------------
(1). Registro de Empleados
(2). Registro de Inasistencias
(3). Registro Bonos Extra-legales
(4). Calculo Nomina
(0). Cerrar programa

Elija una opcion a realizar: ''')
    limpiarTerminal()
    return menu

#opciones del menu volver, recibe str con el nombre del proceso a realizar
def menuVolver(opcionRequerimiento:str):
    menu = input(f'''
--------------------------------------------
-------------MENU REGRESAR-----------------
--------------------------------------------
(*). Cualquier tecla para continuar a {opcionRequerimiento.upper()}
(0). Volver al menu principal

Digite una opcion a realizar: ''')
    limpiarTerminal()
    return menu




def menuRegistrar():
    menu = input(f'''
-------------------------------------------------
(*). Cualquier tecla para registrar datos
(0). Cambiar los datos ingresados
-------------------------------------------------
Digite una opcion a realizar: ''')
    limpiarTerminal()
    return menu


#opciones del menu generar archivos
def menuArchivos():
    while True:
        opc = input('''
    --------------------------------------------
    -------------MENU ARCHIVOS-----------------
    --------------------------------------------
    (1). Guardar reporte como archivo .csv
    (0). Volver al menu principal

    Elija una opcion a realizar: ''')
        limpiarTerminal()
        match opc:
            case "1":
                return True
            case "0":
                return False
            case _:
                print("Por favor digitar '1' para guardar o '0' para volver")



#Funcion para limpiar la terminal dependiendo del sistema operativo en el que se corre el programa
def limpiarTerminal():
    # Para Windows
    if os.name == 'nt':
        placeHolder = os.system('cls')
    # Para macOS y Linux
    else:
        placeHolder = os.system('clear')
