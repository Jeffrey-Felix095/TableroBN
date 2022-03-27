from Tablero import tablero
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image,ImageTk

class batallaNaval():
    def __init__(self):
        self.ventana2 = tk.Tk()#pantalla de inicio
        self.ventana2.title('Batalla Naval')#Titulo de la ventana
        self.ventana2.iconbitmap('IconoBN.ico')#Imagen del icono
        self.interfaz2=tk.Canvas(self.ventana2)#Se define(o crea) una interfaz para la ventana
        self.interfaz2.pack(fill="both", expand=True)#Esto es para la configuración del tamaño de la ventana

        self.imagenJugar = PhotoImage(file="Jugar.png")
        self.botonJugar= tk.Button(self.ventana2,image=self.imagenJugar,command = self.botonJugarAccion)#Se crea el boton de jugar de la pantalla inicial
        self.botonJugar.pack()#El .pack() es para mostrar los cambios hechos en el boton
        
    
    def dibujarTablero(self):#Este es el metodo para dibujar el tablero
        self.tableroJugador.dibujarse()#Llama a metodo dibujar tablero de la clase Tablero
        self.tableroRival.dibujarse()#Llama a metodo dibujar tablero de la clase Tablero

    def __call__(self):
       
        self.ventana2.mainloop()#Esto es para que se abra la ventana al iniciar la app
        

    def botonJugarAccion(self):#Metodo para pasar a otra pantalla
        self.ventana2.destroy()#Cierra la primera pantalla
        self.ventana = tk.Tk()#pantalla de juego
        self.ventana.title('Tablero de Juego')
        self.ventana.iconbitmap('IconoBN.ico')
        self.interfaz=tk.Canvas(self.ventana)
        self.interfaz.pack(fill="both", expand=True)
        self.tableroJugador= tablero(200,50,self.interfaz)#Crea un tablero
        self.tableroRival= tablero(800,50,self.interfaz)#crea un tablero
        self.dibujarTablero()#Llama a la funcion dibujar

inicio=batallaNaval()#instancia del batalla naval(La aplicacion como tal )

inicio()#Ejecuta el programa




