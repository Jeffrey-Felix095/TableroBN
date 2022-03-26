from Tablero import tablero
import tkinter as tk
from PIL import Image



class batallaNaval():
    def __init__(self):
        self.ventana2 = tk.Tk()#pantalla de inicio
        self.ventana2.title('Batalla Naval')
        self.ventana2.iconbitmap('IconoBN.ico')
        self.interfaz2=tk.Canvas(self.ventana2)
        self.interfaz2.pack(fill="both", expand=True)

        imagenBTNjugar= Image.open('Jugar.png')
        imagenBTNjugar = ImageTk.PhotoImage(imagenBTNjugar)

        self.botonJugar= tk.Button(self.ventana2, text="Jugar", image=imagenBTNjugar,command = self.botonJugarAccion)
        self.botonJugar.pack()
        
    
    def dibujarTablero(self):
        self.tableroJugador.dibujarse()
        self.tableroRival.dibujarse()

    def __call__(self):
        self.ventana2.mainloop()

    def botonJugarAccion(self):
        self.ventana2.destroy()
        self.ventana = tk.Tk()#pantalla de juego
        self.ventana.title('Tablero de Juego')
        self.ventana.iconbitmap('IconoBN.ico')
        self.interfaz=tk.Canvas(self.ventana)
        self.interfaz.pack(fill="both", expand=True)
        self.tableroJugador= tablero(200,50,self.interfaz)
        self.tableroRival= tablero(800,50,self.interfaz)
        self.dibujarTablero()

inicio=batallaNaval()

inicio()




