import os
import re
from datetime import datetime
from manejoArchivos import leerEmpleados

MINYEAR = 1990
MAXYEAR = 2050



def cedulaExiste(cedula, mostrarErrores=True):
    empleados = leerEmpleados()
    if empleados:
        for empleado in empleados:
            if empleado["cedula"] == cedula:
                return True
        if mostrarErrores:
            print(f"No hay empleado con cedula: '{cedula}'")
        return False
    else:
        if mostrarErrores:
            print("Aun no se han registrado empleados")
        return False


#Recibe multiples strings como parametros, si todos cumplen con no ser vacios o
# ser solo espacios en blanco retorna True, de lo contrario informa al usuario y retorna False 
def validarStrings(*textosEvaluados):
    sinEspacios = True
    for texto in textosEvaluados:
        if not texto or texto.isspace():
            sinEspacios = False
    if sinEspacios:
        return True
    print("\nNo se aceptan textos vacios o de solo espacios\n")
    return False

#Recibe un numero (como str) y revisa que solo contenga numeros enteros
def esNumero(valorIngresado):
    if not valorIngresado.isdigit():
        return False
    return True

#Recibe un numero (como str) y revisa que sea un int mayor a 0, de lo contrario devuelve False e
#Informa al ususario
def cantidadApropiada(valorIngresado):

    if not esNumero(valorIngresado):
        print("\nEl valor ingresado debe contener solo numeros enteros positivos\n")
        return esNumero(valorIngresado)

    if int(valorIngresado) == 0:
        print("\nEl valor ingresado debe ser mayor a 0\n")
        return False
    else:
        return True
    


# #Revisar si el nombre deseado para un archivo contiene caracteres prohibidos que dependen
# # del sistema operativo usado, recibe el string que desea ingresar devolviendo True si todo en orden
# #False de lo contrario
# def validacionNombreArchivo(nombreArchivoDeseado):
#     caracteresInvalidosWindows = r'[<>:"/\\|?*]'
#     caracteresInvalidosLinux = r'/'
#     if os.name == "nt":
#         nombresReservadosWindows = ['CON', 'PRN', 'AUX', 'NUL', 'COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9', 'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LPT9']
#         invalidosEncontradosWindows = re.findall(caracteresInvalidosWindows, nombreArchivoDeseado)
#         if nombreArchivoDeseado in nombresReservadosWindows or invalidosEncontradosWindows:
#             return False
#         return True 
#     else:
#         invalidosEncontradosLinux = re.findall(caracteresInvalidosLinux, nombreArchivoDeseado) 
#         if invalidosEncontradosLinux:
#             return False
#         return True


# #Revisa si ya existe un archivo txt con el nombre que se pasa como parametro, 
# # si existe devulve true, false de lo contrario
# def archivoExiste(nombreArchivoDeseado):
#     if os.path.isfile(f"{nombreArchivoDeseado}.txt"):
#         return True
#     return False


#Revisar si el mes es valido
def mesValido(mes:str):
    if not mes.isdigit():
        return False
    
    mes = int(mes)
    if mes > 12 or mes < 1:
        
        return False
    
    return True


#Recibe tupla con año mes y dia en formato {anio:YYYY, mes:MM, dia:DD}
#Y devuelve un boolean o el error si es False
def fechaValida(fecha:tuple):
    for valor in fecha:
        if not valor.isdigit():
            print("\nLas fechas debe contener solo numeros enteros positivos\n")
            return False
        
    year = int(fecha[0])
    mes = int(fecha[1])
    dia = int(fecha[2])
    if year > MAXYEAR or year < MINYEAR:
        print("\nEl año ingresado se sale del rango valido\n")
        return False
    
    if not mesValido(fecha[1]):
        print("\nEl mes ingresado no es valido\n")
        return mesValido(fecha[1])
    
    if mes == 12:
        mesComparacion = "01"
        yearComparacion = str(year+1).zfill(4)
    else:
        mesComparacion = str(mes+1).zfill(2)
        yearComparacion = str(year).zfill(4)
    
    if year == MAXYEAR and mes == 12:
        diasMes = 31
    else:
        diasMes = (datetime.date(datetime.fromisoformat(f'{yearComparacion}-{mesComparacion}-01')) - datetime.date(datetime.fromisoformat(f'{str(year).zfill(4)}-{str(mes).zfill(2)}-01'))).days

    if dia < 1 or dia > diasMes:
        print("\nEl dia ingresado no es valido\n")
        return False

    return True


#pruebas

#print(fechaValida(("1997","0","21")))