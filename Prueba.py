import tkinter as tk
class App():
    def __init__(self, l_cuadrado):
        self.l_cuadrado=l_cuadrado
        self.ventana = tk.Tk()
        self.ventana.title('Prueba de tablero')
        self.ventana.iconbitmap('IconoBN.ico')
        self.ventana.geometry(f"{str(l_cuadrado*10)}x{str(l_cuadrado*10)}")
        #self.ventana.resizable(0,0)

        self.interfaz=tk.Canvas(self.ventana)
        self.interfaz.pack(fill="both", expand=True)


    def __call__(self):
        self.ventana.mainloop()

    def dibujar(self):
        #self.interfaz.create_rectangle(x0,y0,x1,x2,fill=2)
        for i in range(10):
            for j in range(10):
                if (i+j) % 2 == 0:
                    self.interfaz.create_rectangle((i*self.l_cuadrado)+200,(j*self.l_cuadrado)+50,((i+1)*self.l_cuadrado)+200,((j+1)*self.l_cuadrado)+50,fill="#000000")
                else:
                    self.interfaz.create_rectangle((i*self.l_cuadrado)+200,(j*self.l_cuadrado)+50,((i+1)*self.l_cuadrado)+200,((j+1)*self.l_cuadrado)+50,fill="#FFFFFF")


TableroBN = App(40)
TableroBN.dibujar()

TableroBN()