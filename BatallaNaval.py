from email.mime import image
from Tablero import tablero
import tkinter as tk
from tkinter import  PhotoImage
from PIL import Image,ImageTk

class batallaNaval():
    def __init__(self):
        self.ventana2 = tk.Tk()#pantalla de inicio
        self.ventana2.title('Batalla Naval')#Titulo de la ventana
        self.ventana2.iconbitmap('IconoBN.ico')#Imagen del icono
        self.ventana2.geometry("960x540")# se define un tamaño fijo de pantalla
        self.interfaz2=tk.Canvas(self.ventana2)#Se define(o crea) una interfaz para la ventana
        self.interfaz2.pack(fill="both", expand=True)#Esto es para la configuración del tamaño de la ventana

        self.imagenJugar = PhotoImage(file="Jugar.png")
        self.imagenFondo = PhotoImage(file="pantalla inicio.png")
        self.interfaz2.create_image(0,0, image=self.imagenFondo, anchor='nw')#se coloca la imagen da fondo sobre la interzaz o canva
        self.botonJugar= tk.Button(self.ventana2,image=self.imagenJugar,command = self.botonJugarAccion)#Se crea el boton de jugar de la pantalla inicial
        self.displaybotonjug= self.interfaz2.create_window(317,376, anchor="nw", window=self.botonJugar)
    
    def dibujarTablero(self):#Este es el metodo para dibujar el tablero
        self.tableroJugador.dibujarse()#Llama a metodo dibujar tablero de la clase Tablero
        self.tableroRival.dibujarse()#Llama a metodo dibujar tablero de la clase Tablero

    def __call__(self):
       
        self.ventana2.mainloop()#Esto es para que se abra la ventana al iniciar la app
        

    def botonJugarAccion1(self):#Metodo para pasar a otra pantalla
        self.ventana1.destroy()#Cierra la primera pantalla
        self.ventana = tk.Tk()#pantalla de juego
        self.ventana.title('Eleccion de flota')
        self.ventana.iconbitmap('IconoBN.ico')
        self.ventana.geometry("960x540")
        self.interfaz=tk.Canvas(self.ventana)
        self.interfaz.pack(fill="both", expand=True)
        self.tableroJugador= tablero(200,50,self.interfaz)#Crea un tablero
        self.tableroRival= tablero(800,50,self.interfaz)#crea un tablero
        self.dibujarTablero()#Llama a la funcion dibujar

    def botonJugarAccion(self):#Metodo para pasar a otra pantalla
        self.ventana2.destroy()#Cierra la primera pantalla
        self.ventana1 = tk.Tk()#pantalla de juego
        self.ventana1.title('Tablero de Juego')
        self.ventana1.iconbitmap('IconoBN.ico')
        self.ventana1.geometry("960x540")
        self.interfaz1=tk.Canvas(self.ventana1)
        self.interfaz1.pack(fill="both", expand=True)
        self.imagenJugar = PhotoImage(file="Start.png")
        self.imagenFondo = PhotoImage(file="seleccion de flota.png")
        self.boton1 = PhotoImage(file="boton1.png")
        self.boton2 = PhotoImage(file="boton2.png")
        self.boton3 = PhotoImage(file="boton3.png")
        self.boton4 = PhotoImage(file="boton4.png")
        self.boton5 = PhotoImage(file="boton5.png")
        self.boton6 = PhotoImage(file="boton6.png")
        self.boton7 = PhotoImage(file="boton7.png")
        self.boton8 = PhotoImage(file="boton8.png")
        self.interfaz1.create_image(0,0, image=self.imagenFondo, anchor='nw')#se coloca la imagen da fondo sobre la interzaz o canva
        self.botonJugar= tk.Button(self.ventana1,image=self.imagenJugar,command = self.botonJugarAccion1)#Se crea el boton de empezar
        self.displaybotonjug= self.interfaz1.create_window(387,330, anchor="nw", window=self.botonJugar)#Se muestra el boton empezar pantalla secundaria y se ubica en la interfaz
        self.botonplussub= tk.Button(self.ventana1,image=self.boton1)#Se crea el boton de agregar submarinos
        self.displayboton1= self.interfaz1.create_window(375,240, anchor="nw", window=self.botonplussub)#Se muestra el boton para añadir submarinos y se ubica en la interfaz
        self.botonminussub= tk.Button(self.ventana1,image=self.boton2)#Se crea el boton de quitar submarinos
        self.displayboton2= self.interfaz1.create_window(10,240, anchor="nw", window=self.botonminussub)
        self.botonplusport= tk.Button(self.ventana1,image=self.boton4)#Se crea el boton de agregar portaaviones
        self.displayboton3= self.interfaz1.create_window(375,437, anchor="nw", window=self.botonplusport)
        self.botonminusport= tk.Button(self.ventana1,image=self.boton3)#Se crea el boton de quitar portaaviones
        self.displayboton4= self.interfaz1.create_window(10,437, anchor="nw", window=self.botonminusport)
        self.botonpluscru= tk.Button(self.ventana1,image=self.boton6)#Se crea el boton de agregar cruceros
        self.displayboton6= self.interfaz1.create_window(875,240, anchor="nw", window=self.botonpluscru)#Se muestra el boton para añadir cruceros y se ubica en la interfaz
        self.botonminuscru= tk.Button(self.ventana1,image=self.boton5)#Se crea el boton de quitar cruceros
        self.displayboton5= self.interfaz1.create_window(525,240, anchor="nw", window=self.botonminuscru)
        self.botonplusdest= tk.Button(self.ventana1,image=self.boton8)#Se crea el boton de agregar destructores
        self.displayboton8= self.interfaz1.create_window(875,437, anchor="nw", window=self.botonplusdest)
        self.botonminusdest= tk.Button(self.ventana1,image=self.boton7)#Se crea el boton de quitar destructores
        self.displayboton7= self.interfaz1.create_window(525,437, anchor="nw", window=self.botonminusdest)
        
inicio=batallaNaval()#instancia del batalla naval(La aplicacion como tal )

inicio()#Ejecuta el programa




