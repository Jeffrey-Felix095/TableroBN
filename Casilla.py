from turtle import width


class casilla():
    def __init__(self,posx,posy,ancho,largo,interfaz,color):#Recibe parametros de posicion, color y donde se van a pintar(La interfaz)
        #POO
        self.posx=posx
        self.posy=posy
        self.ancho=ancho
        self.largo=largo
        self.interfaz=interfaz
        self.color=color

    def dibujarse(self):#Funcion que dibuja la casilla
        #Dibuja un cuadrado de color en su correspondiente posicion
        self.interfaz.create_rectangle(self.posx,self.posy,self.ancho,self.largo,fill=self.color,width=3,outline="White")
