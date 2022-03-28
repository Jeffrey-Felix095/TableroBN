from ast import Return
from email.mime import image
from Tablero import tablero
import tkinter as tk
from tkinter import  PhotoImage
from PIL import Image,ImageTk
import random


class batallaNaval():
    def __init__(self):
        self.numSubmarinos=0 
        self.numDestructores=0
        self.numCruceros=0
        self.numPortaaviones=0
        self.direccion=1
        self.numeroCasillas=0
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
        #self.tableroRival.dibujarse()#Llama a metodo dibujar tablero de la clase Tablero

    def __call__(self):
       
        self.ventana2.mainloop()#Esto es para que se abra la ventana al iniciar la app
        
    

    def botonJugarAccion1(self):#Metodo para pasar a otra pantalla
        self.ventana1.destroy()#Cierra la primera pantalla

        self.espacios=(self.numCruceros*3)+(self.numDestructores*2)+(self.numPortaaviones*4)+self.numSubmarinos
        if(self.espacios>=5):
            self.ventana = tk.Tk()#pantalla de juego
            self.ventana.title('Elección de flota')
            self.ventana.iconbitmap('IconoBN.ico')
            self.ventana.geometry("1300x900")
            self.interfaz=tk.Canvas(self.ventana)
            self.interfaz.pack(fill="both", expand=True)
            self.n=0
            if(self.espacios >= 5 and self.espacios<=10):
                self.n=5
            elif(self.espacios > 10 and self.espacios<=20):
                self.n=6
            elif(self.espacios > 20 and self.espacios<=30):
                self.n=7
            elif(self.espacios > 30 and self.espacios<=40):
                self.n=8
            elif(self.espacios > 40 and self.espacios<=50):
                self.n=10
            self.tableroJugador= tablero((self.ventana.winfo_screenheight()/4),50,self.interfaz,self.n,self)#Crea un tablero

            if(self.numSubmarinos!=0):
                for i in range(self.numSubmarinos):
                    pru=False
                    while(pru==False or pru==0):
                        posx = random.randint(0, self.n-1)
                        posy = random.randint(0, self.n-1)
                        pru=self.tableroJugador.posicionar(self.tableroJugador.getCasilla(posx,posy),1)
            if(self.numDestructores!=0):
                for i in range(self.numDestructores):
                    pru=False
                    while(pru==False):
                        posx = random.randint(0, self.n-1)
                        posy = random.randint(0, self.n-1)
                        pru=self.tableroJugador.posicionar(self.tableroJugador.getCasilla(posx,posy),2)
            if(self.numCruceros!=0):
                for i in range(self.numCruceros):
                    pru=False
                    while(pru==False):
                        posx = random.randint(0, self.n-1)
                        posy = random.randint(0, self.n-1)
                        pru=self.tableroJugador.posicionar(self.tableroJugador.getCasilla(posx,posy),3)
            if(self.numPortaaviones!=0):
                for i in range(self.numPortaaviones):
                    pru=False
                    while(pru==False or pru==0):
                        posx = random.randint(0, self.n-1)
                        posy = random.randint(0, self.n-1)
                        pru=self.tableroJugador.posicionar(self.tableroJugador.getCasilla(posx,posy),4)


            self.dibujarTablero()#Llama a la funcion dibujar
            #self.dibujarBarcosRestantes(self.interfaz)
        
        

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
        self.botonplussub= tk.Button(self.ventana1,image=self.boton1,command = self.aumentarSub)#Se crea el boton de agregar submarinos
        self.displayboton1= self.interfaz1.create_window(375,240, anchor="nw", window=self.botonplussub)#Se muestra el boton para añadir submarinos y se ubica en la interfaz
        self.botonminussub= tk.Button(self.ventana1,image=self.boton2,command = self.disminuirSub)#Se crea el boton de quitar submarinos
        self.displayboton2= self.interfaz1.create_window(10,240, anchor="nw", window=self.botonminussub)
        self.botonplusport= tk.Button(self.ventana1,image=self.boton4,command = self.aumentarPorta)#Se crea el boton de agregar portaaviones
        self.displayboton3= self.interfaz1.create_window(375,437, anchor="nw", window=self.botonplusport)
        self.botonminusport= tk.Button(self.ventana1,image=self.boton3,command = self.disminuirPorta)#Se crea el boton de quitar portaaviones
        self.displayboton4= self.interfaz1.create_window(10,437, anchor="nw", window=self.botonminusport)
        self.botonpluscru= tk.Button(self.ventana1,image=self.boton6,command = self.aumentarCru)#Se crea el boton de agregar cruceros
        self.displayboton6= self.interfaz1.create_window(875,240, anchor="nw", window=self.botonpluscru)#Se muestra el boton para añadir cruceros y se ubica en la interfaz
        self.botonminuscru= tk.Button(self.ventana1,image=self.boton5,command = self.disminuirCru)#Se crea el boton de quitar cruceros
        self.displayboton5= self.interfaz1.create_window(525,240, anchor="nw", window=self.botonminuscru)
        self.botonplusdest= tk.Button(self.ventana1,image=self.boton8,command = self.aumentarDes)#Se crea el boton de agregar destructores
        self.displayboton8= self.interfaz1.create_window(875,437, anchor="nw", window=self.botonplusdest)
        self.botonminusdest= tk.Button(self.ventana1,image=self.boton7,command = self.disminuirDes)#Se crea el boton de quitar destructores
        self.displayboton7= self.interfaz1.create_window(525,437, anchor="nw", window=self.botonminusdest)

        self.submarinos = tk.Label(self.interfaz1, text = self.numSubmarinos, font= ("Courier",30,"italic"),background="#aaaaaa").place(x=215,y=245)
        self.destructores = tk.Label(self.interfaz1, text = self.numDestructores, font= ("Courier",30,"italic"),background="#aaaaaa").place(x=215,y=442)
        self.cruceros = tk.Label(self.interfaz1, text = self.numCruceros, font= ("Courier",30,"italic"),background="#aaaaaa").place(x=730,y=245)
        self.portaaviones = tk.Label(self.interfaz1, text = self.numPortaaviones, font= ("Courier",30,"italic"),background="#aaaaaa").place(x=730,y=442)

    def aumentarSub(self):
        self.numSubmarinos=self.numSubmarinos+1
        self.submarinos = tk.Label(self.interfaz1, text = self.numSubmarinos, font= ("Courier",30,"italic"),background="#aaaaaa").place(x=215,y=245)
    def aumentarDes(self):
        self.numDestructores=self.numDestructores+1
        self.destructores = tk.Label(self.interfaz1, text = self.numDestructores, font= ("Courier",30,"italic"),background="#aaaaaa").place(x=730,y=442)
    def aumentarCru(self):
        self.numCruceros=self.numCruceros+1
        self.cruceros = tk.Label(self.interfaz1, text = self.numCruceros, font= ("Courier",30,"italic"),background="#aaaaaa").place(x=730,y=245)
    def aumentarPorta(self):
        self.numPortaaviones=self.numPortaaviones+1
        self.portaaviones = tk.Label(self.interfaz1, text = self.numPortaaviones, font= ("Courier",30,"italic"),background="#aaaaaa").place(x=215,y=442)
    def disminuirSub(self):
        if(self.numSubmarinos>0):
            self.numSubmarinos=self.numSubmarinos-1
            self.submarinos = tk.Label(self.interfaz1, text = self.numSubmarinos, font= ("Courier",30,"italic"),background="#aaaaaa").place(x=215,y=245)   
    def disminuirDes(self):
        if(self.numDestructores>0):
            self.numDestructores=self.numDestructores-1
            self.destructores = tk.Label(self.interfaz1, text = self.numDestructores, font= ("Courier",30,"italic"),background="#aaaaaa").place(x=730,y=442)
    def disminuirCru(self):
        if(self.numCruceros>0):
            self.numCruceros=self.numCruceros-1
            self.cruceros = tk.Label(self.interfaz1, text = self.numCruceros, font= ("Courier",30,"italic"),background="#aaaaaa").place(x=730,y=245)
    def disminuirPorta(self):
        if(self.numPortaaviones>0):
            self.numPortaaviones=self.numPortaaviones-1   
            self.portaaviones = tk.Label(self.interfaz1, text = self.numPortaaviones, font= ("Courier",30,"italic"),background="#aaaaaa").place(x=215,y=442)





    def getDireccion(self):
        return self.direccion
    def getNumeroCasillas(self):
        return self.numeroCasillas
            
inicio=batallaNaval()#instancia del batalla naval(La aplicacion como tal )

inicio()#Ejecuta el programa




