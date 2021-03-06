from Casilla import casilla
from Barco import barco
import numpy as np
import tkinter as tk
import random

class tablero():

    MR =[]
    LB = []

    def __init__(self, posx, posy,interfaz,n,batallaNaval):#Recibe las posiciones iniciales de donde se posiciona el tablero
        self.posx=posx
        self.posy=posy
        self.n=n
        self.batallaN=batallaNaval
        self.interfaz=interfaz
        self.direc=0
        self.MR=np.zeros((n,n))
        self.casillas=[]#Matriz o lista que guarda las posiciones de las casillas(Un tablero se conforma de casillas)
        self.habilitado=False
        self.numDisparos=0
        

        #Posiciona cada casilla para dar la forma del tablero
        for i in range(self.n):
            self.casillas.append([])
            for j in range(self.n):
                    self.casillas[i].append(casilla(i,j,i*40+posx,j*40+posy,(i+1)*40+posx,(j+1)*40+posy,self.interfaz,"#23BAC4",self))#Agrega a la lista una 
                    #instancia de casilla con su respectiva posicion


    def dibujarse(self):#Dibuja la lista de casillas
        for i in range(self.n):
            for j in range(self.n):
                self.casillas[i][j].dibujarse()#Llama la funcion de dibujar de cada casilla

    def verificarDisparo(self,casilla):#Proximamente
        x=casilla.getPosMx()
        y=casilla.getPosMy()
        if(self.MR[x][y]==0):
            return False
        elif(self.MR[x][y]==1 or self.MR[x][y]==2):
           self.MR[x][y]=2
           return True   
        return 0
                
    def disparo(self,casilla):
        if(self.habilitado):
            if(self.verificarDisparo(casilla)):
                casilla.setColor("#FF0000")
            elif(self.verificarDisparo(casilla)==False):
                casilla.setColor("#024A86")
            self.numDisparos+=1
            self.dibujarse()
            if(self.numDisparos==3):
                if(self.verificarGanador()):
                    self.batallaN.ganador(self)
                else:
                    self.batallaN.habilitacion()
                    self.numDisparos=0

    def posicionar(self,casilla,numCasillas,color):
        xTemp=casilla.getPosMx()
        yTemp=casilla.getPosMy()
        direccion=random.randint(0, 1)
        casillasTemp=numCasillas
        casillasBarcoTemp=[]
        if(self.verificarEspacio(casillasTemp,direccion,casilla.getPosMx(),casilla.getPosMy())==True):   
            print(direccion)
            if(direccion==0):
                for i in range(casillasTemp):
                    self.MR[xTemp,yTemp]=1
                    casillasBarcoTemp.append(self.casillas[xTemp][yTemp])
                    print("si")
                    self.casillas[xTemp][yTemp].setColor(color)
                    xTemp=xTemp-1
            elif(direccion==2):
                for i in range(casillasTemp):
                    self.MR[xTemp,yTemp]=1
                    casillasBarcoTemp.append(self.casillas[xTemp][yTemp])
                    print("si")
                    self.casillas[xTemp][yTemp].setColor(color)
                    xTemp=xTemp+1
            elif(direccion==1):
                print("no")
                for i in range(casillasTemp):
                    self.MR[xTemp,yTemp]=1
                    print("si")
                    casillasBarcoTemp.append(self.casillas[xTemp][yTemp])
                    self.casillas[xTemp][yTemp].setColor(color)
                    yTemp=yTemp-1
            elif(direccion==3):
                print("no")
                for i in range(casillasTemp):
                    self.MR[xTemp,yTemp]=1
                    print("si")
                    casillasBarcoTemp.append(self.casillas[xTemp][yTemp])
                    self.casillas[xTemp][yTemp].setColor(color)
                    yTemp=yTemp+1
            if(casillasTemp==1):
                self.LB.append(barco("Submarino",casillasTemp,casillasBarcoTemp))
            elif(casillasTemp==2):
                self.LB.append(barco("Destructor",casillasTemp,casillasBarcoTemp))
            elif(casillasTemp==3):
                self.LB.append(barco("Crucero",casillasTemp,casillasBarcoTemp))
            elif(casillasTemp==4):
                self.LB.append(barco("PortaAviones",casillasTemp,casillasBarcoTemp))
            return True
        elif(self.verificarEspacio(casillasTemp,direccion,casilla.getPosMx(),casilla.getPosMy())==False):
            return False
        elif(self.verificarEspacio(casillasTemp,direccion,casilla.getPosMx(),casilla.getPosMy())==0):
            return 0

    def verificarEspacio(self, numero, direccion, x,y):
        veri=True
        xTemp=x
        yTemp=y
        try:
             if(direccion==0):
                    for i in range(numero):
                        if(self.MR[xTemp,yTemp]!=0 or xTemp<0 or yTemp<0):
                            veri=False
                        xTemp=xTemp-1

             self.direc=0
        except:
            xTemp=x
            yTemp=y
            try:
                for i in range(numero):
                        if(self.MR[xTemp,yTemp]!=0 or xTemp<0 or yTemp<0):
                            veri=False
                        xTemp=xTemp+1
                self.direc=2
            except:
                veri=0
        try:
            if(direccion==1):
                for i in range(numero):
                        if(self.MR[xTemp,yTemp]!=0 or xTemp<0 or yTemp<0):
                            veri=False
                        yTemp=yTemp-1
            self.direc=1
        except:
            xTemp=x
            yTemp=y
            try:
                for i in range(numero):
                    if(self.MR[xTemp,yTemp]!=0 or xTemp<0 or yTemp<0):
                        veri=False
                    yTemp=yTemp+1
                self.direc=3
            except:
                veri=0
        return veri

    def agregarBarco(self, barco : barco):
        self.LB.append(barco)

    def getCasilla(self,i,j):
        return self.casillas[i][j]

    def getMR(self,i,j):
        return self.MR[i][j]
    
    def setHabilitado(self, habilitado):
        self.habilitado=habilitado
    def getHabilitado(self):
        return self.habilitado
    
    def verificarGanador(self):
        ganar=True
        for i in range(self.n):
            for j in range(self.n):
                if(self.MR[i][j]==1):
                    ganar=False
        return ganar

    



