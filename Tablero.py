from Casilla import casilla
import numpy as np
import tkinter as tk

class tablero():

    MR =[]

    def __init__(self, posx, posy,interfaz):#Recibe las posiciones iniciales de donde se posiciona el tablero
        self.posx=posx
        self.posy=posy
        self.interfaz=interfaz
        self.MR=np.zeros((10,10))
        self.casillas=[]#Matriz o lista que guarda las posiciones de las casillas(Un tablero se conforma de casillas)
        
        #Posiciona cada casilla para dar la forma del tablero
        for i in range(10):
            for j in range(10):
                    self.casillas.append(casilla(i*40+posx,j*40+posy,(i+1)*40+posx,(j+1)*40+posy,self.interfaz,"#000000"))#Agrega a la lista una 
                    #instancia de casilla con su respectiva posicion


    def dibujarse(self):#Dibuja la lista de casillas
        for i in range(10*10):
            self.casillas[i].dibujarse()#Llama la funcion de dibujar de cada casilla

    def verificarDisparo():#Proximamente
        pass


