#Autor: Daniela López Barahona - EQUIPO PROYECTOS
#lecturaDatos leer los datos del cambio inscrito en un excel, creando los diccionarios respectivos.
#Marzo 2020

import openpyxl

def ReadDataInfo(filepath):
    
    excel_document = openpyxl.load_workbook(filepath)
    sheet = excel_document.get_sheet_by_name('DatosJiraCH')
    all_rows = sheet.rows
        
    dataCH = []

    for row in all_rows :
        dataCH.append((row[0].value, row[1].value))
    
    return dataCH
        