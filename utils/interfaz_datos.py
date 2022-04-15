import tkinter
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
from tkinter import Label
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import pickle
from funciones import predecir

## Importando modelo ###
with open('model/my_model', 'rb') as archivo_entrada:
    model_1 = pickle.load(archivo_entrada)

model_1

# Ventana Principal #
ventana = tkinter.Tk()
ventana.title("Predictor precio de venta de coches")
ventana.iconbitmap("ico-coche.ico")
ventana.geometry("1200x250")

# Cajas para escribir datos #
cajaTexto_marca = tkinter.Entry(ventana,borderwidth=5,highlightthickness=2)
cajaTexto_modelo = tkinter.Entry(ventana,borderwidth=5,highlightthickness=2)
cajaTexto_combustible = tkinter.Entry(ventana,borderwidth=5,highlightthickness=2)
cajaTexto_año = tkinter.Entry(ventana,borderwidth=5,highlightthickness=2)
cajaTexto_kms = tkinter.Entry(ventana,borderwidth=5,highlightthickness=2)
cajaTexto_cv = tkinter.Entry(ventana,borderwidth=5,highlightthickness=2)
cajaTexto_puertas = tkinter.Entry(ventana,borderwidth=5,highlightthickness=2)
cajaTexto_cambio = tkinter.Entry(ventana,borderwidth=5,highlightthickness=2)
cajaTexto_color = tkinter.Entry(ventana,borderwidth=5,highlightthickness=2)
cajaTexto_fotos = tkinter.Entry(ventana,borderwidth=5,highlightthickness=2)
cajaTexto_provincia = tkinter.Entry(ventana,borderwidth=5,highlightthickness=2)
cajaTexto_TDG = tkinter.Entry(ventana,borderwidth=5,highlightthickness=2)


dato_1 = []
datos = [dato_1]
def texto():
    entrada1 = cajaTexto_marca.get()
    entrada2 = cajaTexto_modelo.get()
    entrada4 = cajaTexto_combustible.get()
    entrada5 = cajaTexto_año.get()
    entrada6 = cajaTexto_kms.get()
    entrada7 = cajaTexto_cv.get()
    entrada8 = cajaTexto_puertas.get()
    entrada9 = cajaTexto_cambio.get()
    entrada10 = cajaTexto_color.get()
    entrada11 = cajaTexto_fotos.get()
    entrada12 = cajaTexto_provincia.get()
    entrada13 = cajaTexto_TDG.get()
    #print(entrada)
    dato_1.append(entrada1)
    dato_1.append(entrada2)
    dato_1.append(entrada4)
    dato_1.append(entrada5)
    dato_1.append(entrada6)
    dato_1.append(entrada7)
    dato_1.append(entrada8)
    dato_1.append(entrada9)
    dato_1.append(entrada10)
    dato_1.append(entrada11)
    dato_1.append(entrada12)
    dato_1.append(entrada13)
    print(datos)

def borrar():
    cajaTexto_marca.delete("0","end")
    cajaTexto_modelo.delete("0","end")
    cajaTexto_combustible.delete("0","end")
    cajaTexto_año.delete("0","end")
    cajaTexto_kms.delete("0","end")
    cajaTexto_cv.delete("0","end")
    cajaTexto_puertas.delete("0","end")
    cajaTexto_cambio.delete("0","end")
    cajaTexto_color.delete("0","end")
    cajaTexto_fotos.delete("0","end")
    cajaTexto_provincia.delete("0","end")
    cajaTexto_TDG.delete("0","end")

# Botón confirmación # 

boton1 = tkinter.Button(ventana, text="Confirmar",command=texto,border=5,font='Helvetica',bg='#0052cc',fg='#ffffff')
boton1.grid(row=4,column=2,ipadx=10,ipady=30,columnspan=2)

boton2 = tkinter.Button(ventana, text="Borrar datos",command=borrar,border=5,font='Helvetica',bg='#0052cc',fg='#ffffff')
boton2.grid(row=4,column=4,ipadx=10,ipady=30,columnspan=2)

############

# Colocación cajas  #
cajaTexto_marca.grid(row=1,column=0,ipadx=10,ipady=5)
cajaTexto_modelo.grid(row=1, column=1,ipadx=10,ipady=5)
cajaTexto_TDG.grid(row=1, column=2,ipadx=10,ipady=5)
cajaTexto_combustible.grid(row=1, column=3,ipadx=10,ipady=5)
cajaTexto_año.grid(row=1, column=4,ipadx=10,ipady=5)
cajaTexto_kms.grid(row=1, column=5,ipadx=10,ipady=5)
cajaTexto_cv.grid(row=1, column=6,ipadx=10,ipady=5)
cajaTexto_puertas.grid(row=3, column=0,ipadx=10,ipady=5)
cajaTexto_cambio.grid(row=3, column=1,ipadx=10,ipady=5)
cajaTexto_color.grid(row=3, column=2,ipadx=10,ipady=5)
cajaTexto_fotos.grid(row=3, column=3,ipadx=10,ipady=5)
cajaTexto_provincia.grid(row=3, column=4,ipadx=10,ipady=5)

# Labels #

Label(ventana, text="Marca",font='Helvetica').grid(row=0,column=0)
Label(ventana, text="Modelo",font='Helvetica').grid(row=0,column=1)
Label(ventana, text="TDG",font='Helvetica').grid(row=0,column=2)
Label(ventana, text="Combustible",font='Helvetica').grid(row=0,column=3)
Label(ventana, text="Antigüedad",font='Helvetica').grid(row=0,column=4)
Label(ventana, text="kms",font='Helvetica').grid(row=0,column=5)
Label(ventana, text="Caballos",font='Helvetica').grid(row=0,column=6)
Label(ventana, text="Número de puertas",font='Helvetica').grid(row=2,column=0)
Label(ventana, text="Tipo de cambio",font='Helvetica').grid(row=2,column=1)
Label(ventana, text="Color",font='Helvetica').grid(row=2,column=2)
Label(ventana, text="Nº de fotos",font='Helvetica').grid(row=2,column=3)
Label(ventana, text="Provincia",font='Helvetica').grid(row=2,column=4)



ventana.mainloop()



arr_dato = np.array(dato_1)

df = pd.DataFrame(columns=['Marca','Modelo','Tipo_Combustible','Año','kms','CV','N_Puertas','Tipo_Cambio',
'color','N_Fotos','Provincia','TDG'])

df = df.append({'Marca': arr_dato[0], 'Modelo':arr_dato[1],'Tipo_Combustible':arr_dato[3],'Año':arr_dato[4],
                'kms':arr_dato[5],'CV':arr_dato[6],'N_Puertas':arr_dato[7],'Tipo_Cambio':arr_dato[8],
                'color': arr_dato[9],'N_Fotos':arr_dato[10],'Provincia':arr_dato[11],'TDG':arr_dato[2]}, ignore_index=True)

precio = predecir(df)
print(precio)



