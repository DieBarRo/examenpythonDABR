#Donde se genera la funcionalidad principal del app

from menus import menuVolver, menuRegistrar, limpiarTerminal
from validaciones import validarStrings, cedulaExiste, esNumero, cantidadApropiada, fechaValida, mesValido
from manejoArchivos import leerEmpleados, actualizarEmpleados, generarReporte
from datetime import datetime

def registrarEmpleado():
    identificacion = ""
    nombre = ""
    apellido = ""
    cargo = ""
    salario = ""
    
    #Repetir hasta que el usuario quiera volver al menu principal
    opc = menuVolver("registro empleados")
    while True: 
        if opc == "0":
            limpiarTerminal()
            break

        #Ingreso de datos por el usuario
        if not identificacion:
            identificacion = input("Digite la CEDULA del empleado, Los espacios vacios al inicio y al final se eliminan: ").strip()
            if cedulaExiste(identificacion, mostrarErrores=False) or not esNumero(identificacion):
                print(f"La cedula '{identificacion}' ya pertenece a un empleado registrado o No es un Numero\n")
                identificacion = ""
                continue

        if not salario:
            salario = input("Digite el valor del SALARIO. Solo se aceptan ENTEROS mayores a 0: ").strip()
            if not cantidadApropiada(salario):
                salario = ""
                continue

        if not nombre:
            nombre = input("Digite el NOMBRE del empleado, Los espacios vacios al inicio y al final se eliminan: ").strip()
            if not validarStrings(nombre):
                nombre = ""
                continue
        
        if not apellido:
            apellido = input("Digite el APELLIDO del empleado, Los espacios vacios al inicio y al final se eliminan: ").strip()
            if not validarStrings(apellido):
                apellido = ""
                continue
        
        if not cargo:
            cargo = input("Digite el CARGO del empleado, Los espacios vacios al inicio y al final se eliminan: ").strip()
            if not validarStrings(cargo):
                cargo = ""
                continue

        
        #Confirmar si el usuario quiere ingresar los datos del empleado
        print(f"La cedula del empleado es: {identificacion}")
        print(f"El nombre es: {nombre}")
        print(f"El apellido es: {apellido}")
        print(f"El cargo es: {cargo}")
        print(f"Con un salario de: {salario}\n")
        confirmacionFinal = menuRegistrar()
        
        if confirmacionFinal == "0":
            identificacion = ""
            nombre = ""
            apellido = ""
            cargo = ""
            salario = ""
            continue

        empleado = {
            "cedula": identificacion,
            "nombre": nombre,
            "apellido": apellido,
            "cargo": cargo,
            "salario": salario,
            "inasistencias": [],
            "bonos": []
        }
        empleados = leerEmpleados()
        empleados.append(empleado)
        actualizarEmpleados(empleados)
        identificacion = ""
        nombre = ""
        apellido = ""
        cargo = ""
        salario = ""
        opc = menuVolver("registro empleados")


def registrarInasistencias():
    identificacion = ""
    year = ""
    mes = ""
    dia = ""
    
    #Repetir hasta que el usuario quiera volver al menu principal
    opc = menuVolver("inasistencias")
    while True: 
        if opc == "0":
            limpiarTerminal()
            break

        #Ingreso de datos por el usuario
        if not identificacion:
            identificacion = input("Digite la CEDULA del empleado, Los espacios vacios al inicio y al final se eliminan: ").strip()
            if not cedulaExiste(identificacion):
                identificacion = ""
                continue

        if not (year and mes and dia):
            year = input("Digite el año de la inasistencia (Entre 1990 y 2050), formato YYYY porfavor: ")
            mes = input("Digite el mes de la inasistencia, formato MM porfavor: ")
            dia = input("Digite el dia de la inasistencia, formato DD porfavor: ")
            if not fechaValida((year, mes, dia)):
                year = ""
                mes = ""
                dia = ""
                continue
        fecha = str(datetime.date(datetime.fromisoformat(f'{year.zfill(4)}-{mes.zfill(2)}-{dia.zfill(2)}')))

        
        #Confirmar si el usuario quiere ingresar los datos del empleado
        print(f"La cedula del empleado es: {identificacion}")
        print(f"Fecha de la inasistencia: {fecha}\n")
        confirmacionFinal = menuRegistrar()
        
        if confirmacionFinal == "0":
            identificacion = ""
            year = ""
            mes = ""
            dia = ""
            continue

        empleados = leerEmpleados()
        for empleado in empleados:
            if empleado["cedula"] == identificacion:
                empleado["inasistencias"].append(fecha)
        actualizarEmpleados(empleados)
        identificacion = ""
        year = ""
        mes = ""
        dia = ""
        opc = menuVolver("inasistencias")


def registrarBonos():
    identificacion = ""
    valor = ""
    concepto = ""
    year = ""
    mes = ""
    dia = ""
    
    #Repetir hasta que el usuario quiera volver al menu principal
    opc = menuVolver("bonos")
    while True: 
        if opc == "0":
            limpiarTerminal()
            break

        #Ingreso de datos por el usuario
        if not identificacion:
            identificacion = input("Digite la CEDULA del empleado, Los espacios vacios al inicio y al final se eliminan: ").strip()
            if not cedulaExiste(identificacion):
                identificacion = ""
                continue
        
        if not valor:
            valor = input("Digite el valor del BONO. Solo se aceptan ENTEROS mayores a 0: ").strip()
            if not cantidadApropiada(valor):
                valor = ""
                continue

        if not concepto:
            concepto= input("Digite el CONCEPTO del bono del empleado, Los espacios vacios al inicio y al final se eliminan: ").strip()
            if not validarStrings(concepto):
                concepto = ""
                continue

        if not (year and mes and dia):
            year = input("Digite el año de la inasistencia (Entre 1990 y 2050), formato YYYY porfavor: ")
            mes = input("Digite el mes de la inasistencia, formato MM porfavor: ")
            dia = input("Digite el dia de la inasistencia, formato DD porfavor: ")
            if not fechaValida((year, mes, dia)):
                year = ""
                mes = ""
                dia = ""
                continue
        fecha = str(datetime.date(datetime.fromisoformat(f'{year.zfill(4)}-{mes.zfill(2)}-{dia.zfill(2)}')))

        
        #Confirmar si el usuario quiere ingresar los datos del empleado
        print(f"La cedula del empleado es: {identificacion}")
        print(f"Motivo del bono: {concepto}")
        print(f"Valor del bono: {valor}")
        print(f"Fecha del bono: {fecha}\n")
        confirmacionFinal = menuRegistrar()
        
        if confirmacionFinal == "0":
            identificacion = ""
            valor = ""
            concepto = ""
            year = ""
            mes = ""
            dia = ""
            continue

        bono = {
            "fecha": fecha,
            "valor": valor,
            "concepto": concepto,
        }

        empleados = leerEmpleados()
        for empleado in empleados:
            if empleado["cedula"] == identificacion:
                empleado["bonos"].append(bono)
        actualizarEmpleados(empleados)
        identificacion = ""
        valor = ""
        concepto = ""
        year = ""
        mes = ""
        dia = ""
        opc = menuVolver("bonos")


def generarNomina():
    identificacion = ""
    mes = ""
    
    #Repetir hasta que el usuario quiera volver al menu principal
    opc = menuVolver("nominas")
    while True: 
        if opc == "0":
            limpiarTerminal()
            break

        #Ingreso de datos por el usuario
        if not identificacion:
            identificacion = input("Digite la CEDULA del empleado, Los espacios vacios al inicio y al final se eliminan: ").strip()
            if not cedulaExiste(identificacion):
                identificacion = ""
                continue

        if not mes:
            mes = input("Digite el mes de la inasistencia, formato MM porfavor: ")
            if not mesValido(mes):
                print("mes no valido")
                mes = ""
                continue
        mes = mes.zfill(2)

        
        empleados = leerEmpleados()
        
        #calcular bonos
        totalBonos = 0
        for empleado in empleados:
            if empleado["cedula"] == identificacion:
                for bono in empleado["bonos"]:
                    fechaBono = str(datetime.date(datetime.fromisoformat(bono["fecha"])).month).zfill(2)
                    if fechaBono == mes:
                        totalBonos += int(bono["valor"])

        #calcular inasistencias
        totalInasistencias = 0
        for empleado in empleados:
            if empleado["cedula"] == identificacion:
                for inasistencia in empleado["inasistencias"]:
                    fechaInasistencia = str(datetime.date(datetime.fromisoformat(inasistencia)).month).zfill(2)
                    if fechaInasistencia == mes:
                        totalInasistencias += 1
        
        descuentoSalud = 0
        for empleado in empleados:
            if empleado["cedula"] == identificacion:
                descuentoSalud = int(empleado["salario"])*0.04

        descuentoPension = 0
        for empleado in empleados:
            if empleado["cedula"] == identificacion:
                descuentoPension = int(empleado["salario"])*0.04
        
        descuentoInasistencias = 0
        for empleado in empleados:
            if empleado["cedula"] == identificacion:
                salarioDia = int(empleado["salario"])/30
                descuentoInasistencias = salarioDia*totalInasistencias

        transporte = 0
        for empleado in empleados:
            if empleado["cedula"] == identificacion:
                if int(empleado["salario"]) < 2000000:
                    transporte = int(empleado["salario"])*0.1


        for empleado in empleados:
            if empleado["cedula"] == identificacion:
                nombre = empleado["nombre"]
                apellido = empleado["apellido"]
                cargo = empleado["cargo"]
                salario = int(empleado["salario"])
        informacion = [{
        'cedula':identificacion,
        'nombre': nombre,
        'apellido': apellido,
        'cargo': cargo,
        'salario': salario,
        'descuento salud': descuentoSalud,
        'descuento pension' : descuentoPension,
        'faltas' : totalInasistencias,
        'bonos': totalBonos,
        'total': salario - descuentoSalud - descuentoPension - descuentoInasistencias + totalBonos,
        }]
        print(type(informacion))

        generarReporte(informacion,identificacion)

        


        identificacion = ""
        mes = ""
        opc = menuVolver("nominas")
