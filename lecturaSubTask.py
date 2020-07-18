#Autor: Daniela López Barahona
#lecturaDatos leer los datos de las tareas inscritas en un excel, creando los diccionarios respectivos.
#Marzo 2020

import openpyxl

def ReadDataSub(filepath):
    
    excel_document = openpyxl.load_workbook(filepath)
    sheet = excel_document.get_sheet_by_name('DatosSubTareas')
    all_rows = sheet.rows
        
    tasks  = []
    countED = 0
    countRB = 0

    for row in all_rows :
        countED += 1
        if countED > 1 and row[0].value != None:
            tasks.append((row[0].value, row[1].value, row[2].value, row[3].value, row[4].value, row[5].value))
            if row[0].value == 'RollBack Activity':
                    countRB += 1

    return tasks, countRB
        