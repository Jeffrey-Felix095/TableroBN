from Casilla import casilla
import tkinter as tk

tablero = []

class tablero():
    def __init__(self, posx, posy,interfaz):
        self.posx=posx
        self.posy=posy
        self.interfaz=interfaz
        self.casillas=[]
        
        for i in range(10):
            for j in range(10):
                    self.casillas.append(casilla(i*40+posx,j*40+posy,(i+1)*40+posx,(j+1)*40+posy,self.interfaz,"#000000"))


    def dibujarse(self):
        for i in range(10*10):
            self.casillas[i].dibujarse()

    def verificarDisparo():
        pass


