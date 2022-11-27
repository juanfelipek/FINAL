import tkinter as tk

from tkinter import *

import os

root=tk.Tk()

root.title("Gestor de datos")

root.geometry("1000x500")
root.config(bg="white")

def clear():

 os.system('cls')

def add_contact():

    f = open("contact_data.txt","a")

    ID = IDENTIFICACION.get()
    f.write("\n"+ID)
    name = NOMBRE.get()
    f.write("\n"+name)
    apellido = APELLIDO.get()
    f.write("\n"+apellido)

    ventana=Tk()
    ventana.title("Mensaje")
    ventana.geometry("200x200")
    ventana.config(bg="white")
    M = Label(ventana, text="Agregado satisfactoriamente..!!", bg="white")
    M.place(relx=0.05, rely=0.1, relheight=0.1, relwidth=0.9)
    b = Button(ventana, text="Salir", command=ventana.destroy, height=3, width=12, bg="#32f2d8")
    b.place(relx=0.25, rely=0.5)


    ventana.mainloop()

    f.close()


def query_contact():
    f = open("contact_data.txt","r")
    flag = 0
    ID = IDENTIFICACION.get()
    for line in f:
        if(line.rstrip("\n") == ID):
            print("\nID : ",line.rstrip("\n"))
            name = next(f)
            print("Nombre : ",name.rstrip("\n"))
            apellido = next(f)
            print("Apellido : ",apellido.rstrip("\n"))
            flag = 1
            break
    if(flag == 0):
        print("\n No encontrado")
    f.close()

def delete_contact():
    f = open("contact_data.txt","r")
    lines = f.readlines()
    f.close()
    f = open("contact_data.txt","w")
    flag = 0
    ID = IDENTIFICACION.get()
    for line in lines:
        if(line.rstrip("\n") == ID):
            flag = 1
            continue
        f.write(line)
    if(flag == 0):
        print("\n No encontrado")


    f = open("contact_data.txt", "r")
    lines = f.readlines()
    f.close()
    f = open("contact_data.txt", "w")
    flag = 0
    Nombre = NOMBRE.get()
    for line in lines:
        if (line.rstrip("\n") == Nombre):
            flag = 1
            continue
        f.write(line)
    if (flag == 0):
        print("\n No encontrado")

    f = open("contact_data.txt", "r")
    lines = f.readlines()
    f.close()
    f = open("contact_data.txt", "w")
    flag = 0
    Apellido = APELLIDO.get()
    for line in lines:
        if (line.rstrip("\n") == Apellido):
            flag = 1
            continue
        f.write(line)
    if (flag == 0):
        print("\n No encontrado")
    else:
        print("\n Borrado satisfactoriamente..!!")
    f.close()

def modify_contact():
    f = open("contact_data.txt","r")
    lines = f.readlines()
    f.close()
    f = open("contact_data.txt","w")
    flag = 0
    ID = input("\n Escriba el número de ID : ")
    for line in lines:
        if(line.rstrip("\n") == ID):
            flag = 1
            name = input("\n Escriba el nombre : ")
            apellido = input("\n Escriba el apellido : ")
            f.write(ID+"\n"+name+"\n"+apellido)
            continue
        f.write(line)
    if(flag == 0):
        print("\n No encontrado")
    f.close()

btn=Button(root,text="Agregar",command=add_contact,height=1,width=30,bg="#52f232")
btn.place(x=600,y=60)
btn=Button(root,text="Consultar",command=query_contact,height=1,width=30,bg="#3832f2")
btn.place(x=600,y=120)
btn=Button(root,text="Borrar",command=delete_contact,height=1,width=30,bg="#f23278")
btn.place(x=600,y=180)
btn=Button(root,text="Modificar",command=modify_contact,height=1,width=30,bg="#f2b832")
btn.place(x=600,y=240)
btn=Button(root,text="Salir",command=exit,height=1,width=30,bg="#32f2d8")
btn.place(x=600,y=300)

CEDULA=Label(root,text="Identificación",bg="white")
CEDULA.place(x=40,y=80,height=20,width=100)
IDENTIFICACION=Entry(root,bg="#a1c1cc")
IDENTIFICACION.place(x=180,y=80,height=20,width=350)

N1=Label(root,text="Nombre",bg="white")
N1.place(x=40,y=120,height=20,width=100)
NOMBRE=Entry(root,bg="#a1c1cc")
NOMBRE.place(x=180,y=120,height=20,width=350)

A1=Label(root,text="Apellido",bg="white")
A1.place(x=40,y=160,height=20,width=100)
APELLIDO=Entry(root,bg="#a1c1cc")
APELLIDO.place(x=180,y=160,height=20,width=350)

root.mainloop()