from turtle import width
import tkinter as tk

class casilla():
    def __init__(self,posMx,posMy,posx,posy,ancho,largo,interfaz,color,Tablero):#Recibe parametros de posicion, color y donde se van a pintar(La interfaz)
        #POO
        self.posMx=posMx
        self.posMy=posMy
        self.posx=posx
        self.posy=posy
        self.ancho=ancho
        self.largo=largo
        self.interfaz=interfaz
        self.color=color
        self.tablero=Tablero
        self.botonInterno=tk.Button()

    def dibujarse(self):#Funcion que dibuja la casilla
        #Dibuja un cuadrado de color en su correspondiente posicion
        self.botonInterno=tk.Button(self.interfaz,background=self.color,width=4,height=2).place(x=self.posx,y=self.posy)
       # self.interfaz.create_rectangle(self.posx,self.posy,self.ancho,self.largo,fill=self.color,width=3,outline="White")

    def getPosMx(self):
        return self.posMx
    
    def getPosMy(self):
        return self.posMy
    
    def posicionar(self):
        self.tablero.posicionar(self)

    def setColor(self,color):
        self.color=color
    
