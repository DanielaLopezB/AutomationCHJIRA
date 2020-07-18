#Autor: Daniela López Barahona - EQUIPO PROYECTOS
#CreationCHJIRA genera la intefaz para crea cambios en JIRA, a partir del llamado de las funciones correspondientes.
#Junio 2020

from tkinter import Button, Entry, Frame, Label, Message, StringVar, Tk
from future.moves.tkinter import filedialog

from lecturaDatos import ReadDataInfo
from lecturaSubTask import ReadDataSub
from creacionCHNormal import CreationCH
from creacionCHUrgencia import CreationCHU

# Definición de variables
root = Tk()
returnStatus = StringVar()
returnURL = StringVar()

# Función que realiza las acciones del boton Crear cambio


def codeCreateNormal():

    # Interfaz para seleccionar el archivo Excel que contienen los datos necesarios para la creación del cambio
    root.filename = filedialog.askopenfilename(
        filetypes=[("Excel files", ".xlsx .xls .xlsm")])

    # Guarda los respectivos datos para la creación del CH
    dataCH = ReadDataInfo(root.filename)
    tasks, countRB = ReadDataSub(root.filename)

    # crear el cambio
    estadoCH, urlCH = CreationCH(dataCH, tasks, countRB)

    # Devuelve el resultado de la ejecución del CH
    returnStatus.set(estadoCH)
    returnURL.set(urlCH)

    # Mensajes en la pantalla según el return de la funcion CreationCH
    resultStatus = Message(frame, textvariable=returnStatus, bg="#f8f8fb", fg="#c65185", font=(
        "Alata", 9), width=210, justify="center", cursor="center_ptr")
    resultStatus.place(x=108, y=150)

    resultURL = Entry(frame, textvariable=returnURL, bg="#f8f8fb",
                      fg="#3d3132", font=("Alata", 7), width=52, justify="center")
    resultURL.place(x=83, y=180)

def codeCreateUrgency():

    # Interfaz para seleccionar el archivo Excel que contienen los datos necesarios para la creación del cambio
    root.filename = filedialog.askopenfilename(
        filetypes=[("Excel files", ".xlsx .xls .xlsm")])

    # Guarda los respectivos datos para la creación del CH
    dataCH = ReadDataInfo(root.filename)
    tasks, countRB = ReadDataSub(root.filename)

    # crear el cambio
    estadoCH, urlCH = CreationCHU(dataCH, tasks, countRB)

    # Devuelve el resultado de la ejecución del CH
    returnStatus.set(estadoCH)
    returnURL.set(urlCH)

    # Mensajes en la pantalla según el return de la funcion CreationCH
    resultStatus = Message(frame, textvariable=returnStatus, bg="#f8f8fb", fg="#c65185", font=(
        "Alata", 9), width=210, justify="center", cursor="center_ptr")
    resultStatus.place(x=108, y=150)

    resultURL = Entry(frame, textvariable=returnURL, bg="#f8f8fb",
                      fg="#3d3132", font=("Alata", 7), width=52, justify="center")
    resultURL.place(x=83, y=180)

# ----------------------Elementos Pantalla----------------------------------------------------------------------------------------------------------------------------------


# Crea la raíz de la pantalla, con sus características
root.title("CH-Jira")
root.iconbitmap("./resources/accenture.ico")
root.resizable(False, False)

# Crea el frame que está en la raíz, con sus características
frame = Frame(root, width="400", height="255", bg='#f8f8fb')
frame.pack()

# Elementos de la pantalla, título, boton que llama las funciones del programa
tittleLabel = Label(frame, text="Creación de Cambios",
                    bg='#f8f8fb', fg="#472b7d", font="Alata").place(x=100, y=30)

buttomSelectNormal = Button(frame, text="Crear CH-Normal", bg="white", fg="#472b7d", font=(
    "Alata", 10), cursor="hand2", command=codeCreateNormal).place(x=70, y=90)

buttomSelectUrgency = Button(frame, text="Crear CH-Urgencia", bg="white", fg="#472b7d", font=(
    "Alata", 10), cursor="hand2", command=codeCreateUrgency).place(x=210, y=90)
root.mainloop()
