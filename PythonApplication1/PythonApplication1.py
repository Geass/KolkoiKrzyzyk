import tkinter as tk
from tkinter import filedialog, Text
import os 
root = tk.Tk()
theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

board_keys = []


def body():
    
    root.title("Kółko i krzyżyk")
    root.iconbitmap(r'favicon.ico')
#okienko
    canvas = tk.Canvas(root, height =400, width= 400, bg="grey84")
    canvas.pack()
#linie
    canvas.create_line(125,0,125,400, fill='black', width=12)
    canvas.create_line(275,0,275,400, fill='black', width=12)
    canvas.create_line(0,125,400,125, fill='black', width=12)
    canvas.create_line(0,275,400,275, fill='black', width=12)

  
def zagrajponownie():
    ZagrajPonownie = tk.Button(root, text="Zagraj ponownie", fg="black",bg="grey")
    ZagrajPonownie.pack() 
def przycisk1():
    Button1= tk.Button(root, text='',fg="white",bg="grey", width=15, height=7).place(x=0, y=0)
    Button2= tk.Button(root, text='',fg="white",bg="grey", width=17, height=7).place(x=135, y=0)
    Button3= tk.Button(root, text='X',fg="white",bg="grey", width=15, height=7).place(x=285, y=0)
    Button4= tk.Button(root, text='',fg="white",bg="grey", width=15, height=8).place(x=0, y=132)
    Button5= tk.Button(root, text='O',fg="white",bg="grey", width=18, height=8).place(x=135, y=132)
    Button6= tk.Button(root, text='X',fg="white",bg="grey", width=15, height=8).place(x=285, y=132)
    Button7= tk.Button(root, text='O',fg="white",bg="grey", width=15, height=7).place(x=0, y=280)
    Button8= tk.Button(root, text='O',fg="white",bg="grey", width=18, height=7).place(x=130, y=280)
    Button9= tk.Button(root, text='X',fg="white",bg="grey", width=15, height=7).place(x=280, y=280)   
def mainprogram():
    turn ='X'
    count=0

    move=input()





body()
przycisk1()
zagrajponownie()

root.mainloop()