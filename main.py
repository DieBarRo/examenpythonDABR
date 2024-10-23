#Donde inicia el programa

from menus import menuPrincipal, limpiarTerminal
from funcionalidadNomina import *

# Dependiendo de la opcion llama funcion de accionesInventario, 
# si no se escoge una opcion valida se repite
while True:
    
    opc = menuPrincipal()
    match opc:
        case '1':
            limpiarTerminal()
            registrarEmpleado()
        case '2':
            limpiarTerminal()
            registrarInasistencias()
        case '3':
            limpiarTerminal()
            registrarBonos()
        case '4':
            limpiarTerminal()
            generarNomina()
        case '0':
            print('Finalizando programa...\n')
            break
        case _:
            print('''
        ------LA OPCION NO ESTA DENTRO DEL RANGO-------
        --INGRESE UN VALOR ENTRE (1-4). 0 PARA SALIR.--''')