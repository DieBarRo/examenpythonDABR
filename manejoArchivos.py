# Para leer y escribir en el csv
from csv import DictReader, DictWriter 
import json


#abrir el json de productos y retorna los productos que son una lista de diccionarios
#si no existe el archivo crea la estructura basica y la retorna
def leerEmpleados():
    try:
        with open("empleados.json", "r") as file:
            empleados = json.load(file)
            return empleados
    except FileNotFoundError:
        empleados = [

        ]
        jsonEmpleados = json.dumps(empleados, indent=4)
        with open("empleados.json", "w") as file:
            file.write(jsonEmpleados)
            return empleados
        

#Recibe la lista de diccionarios: productos, la convierte a un Json indentado para mayor legibilidad
#Y la guarda en el archivo productos.json
def actualizarEmpleados(empleados):
    jsonEmpleados = json.dumps(empleados, indent=4)
    with open("empleados.json", "w") as file:
        file.write(jsonEmpleados)



# #abrir el csv llamado baseDatos como una lista de diccionarios, si no existe crear el archivo
# def leerBaseDatos():
#     try:
#         with open("baseDatos.csv", "r") as file:
#             dictReader_obj = DictReader(file)
#             listaMovimientos = []
#             for item in dictReader_obj:
#                 listaMovimientos.append(item)
#             return listaMovimientos
#     except FileNotFoundError:
#         headers = [
#         'fecha',
#         'movimiento',
#         'tipo',
#         'descripcion',
#         'valor',
#         ]
        
#         with open("baseDatos.csv", "w", newline='') as file:
#             writer = DictWriter(file, fieldnames=headers)
#             writer.writeheader()
#             return []

        



#Recibe la lista de diccionarios: baseDatos y la guarda en el archivo baseDatos.csv
#Todas las columnas las guarda como un string
def generarReporte(reporte:dict, cedula):
    headers = [
        'cedula',
        'nombre',
        'apellido',
        'cargo',
        'salario',
        'descuento salud',
        'descuento pension',
        'faltas',
        'bonos',
        'total',
        ]
        
    with open(fr"{cedula}.csv", "w", newline='') as file:
        writer = DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(reporte)



# #guarda el reporte como un archivo .txt, 
# # recibe un String con lo que registrar y el nombre del archivo en la segunda posicion
# def guardarReporte(reporte, nombreArchivo):
#     with open(fr"{nombreArchivo}.txt", "w") as archivo:
# 	    archivo.write(reporte)




# #Zona de pruebas:
# baseDatos = [
#             {"fecha" : '12-10-24',
#             "movimiento": 'ingreso',
#             'tipo': 'laboral',
#             'descripcion': 'no me importa',
#             'valor':  4800,
#             },{"fecha" : '13-10-24',
#             "movimiento": 'egreso',
#             'tipo': 'salud',
#             'descripcion': 'me jodi la pierna',
#             'valor':  800,
#             }]

# leerBaseDatos()
# print(leerBaseDatos())
# actualizarBaseDatos(baseDatos)
# print(leerBaseDatos())

