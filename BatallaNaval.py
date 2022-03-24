from Tablero import tablero
import tkinter as tk
class batallaNaval():
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Prueba de tablero')
        self.ventana.iconbitmap('IconoBN.ico')
        self.interfaz=tk.Canvas(self.ventana)
        self.interfaz.pack(fill="both", expand=True)
        self.tableroJugador= tablero(200,50,self.interfaz)
        self.tableroRival= tablero(800,50,self.interfaz)
    
    def dibujarTablero(self):
        self.tableroJugador.dibujarse()
        self.tableroRival.dibujarse()

    def __call__(self):
        self.ventana.mainloop()

inicio=batallaNaval()

inicio.dibujarTablero()
inicio()




