from turtle import width


class casilla():
    def __init__(self,posx,posy,ancho,largo,interfaz,color):
        self.posx=posx
        self.posy=posy
        self.ancho=ancho
        self.largo=largo
        self.interfaz=interfaz
        self.color=color

    def dibujarse(self):
        self.interfaz.create_rectangle(self.posx,self.posy,self.ancho,self.largo,fill=self.color,width=3,outline="White")
