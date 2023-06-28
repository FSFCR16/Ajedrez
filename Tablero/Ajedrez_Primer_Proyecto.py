from tkinter import * 

import tkinter as tk

import ChessFichas
raiz=Tk()

class TableroAjedrez:

    def __init__(self, ventana, cuadrado):

        self.chess= ChessFichas.fichas()
        self.imagenes={}
        self.cuadrado=cuadrado
        self.ventana=ventana
        self.ventana.title("Chess")
        icon_grande=tk.PhotoImage(file="Aj.png")
        icon_chico=tk.PhotoImage(file="Aje.png")
        self.ventana.iconphoto(False, icon_grande, icon_chico)
        self.ventana.geometry(f"{str(cuadrado*8)}x{str(cuadrado*8)}")
        self.ventana.resizable(0,0)
        #Ubicar partes del tablero

        self.tablero=tk.Canvas(self.ventana)
        self.tablero.pack(fill="both", expand=True)

    
    def PartesTablero(self):

        for fila in range(8):
            for columna in range(8):
                if (fila+columna)%2==0:
                    self.tablero.create_rectangle(fila*self.cuadrado, columna*self.cuadrado, (fila+1)*self.cuadrado, (columna+1)*self.cuadrado, fill="#7D3B00")

                else: 
                    self.tablero.create_rectangle(fila*self.cuadrado, columna*self.cuadrado, (fila+1)*self.cuadrado,(columna+1)*self.cuadrado, fill="#E1AE80")


    def fichas(self):
        piezas=["AB", "AN" , "CB" , "CN" , "PB", "PN" , "RB", "RN", "REB", "REN", "TB", "TN"]

        for pieza in piezas:
            self.imagenes[pieza]= tk.PhotoImage(file="./Ajedrez/Tablero/piezas/"+ pieza + ".png").zoom(self.cuadrado).subsample(43)

    def posicionarPiezas(self):
        for indice, ileras in enumerate(self.chess.piezas):
            for indice_2, elemento  in enumerate(ileras):
                if elemento != "--":
                    self.tablero.create_image(indice_2*self.cuadrado, indice*self.cuadrado, image=self.imagenes[elemento], anchor="nw")
        

ajedrez=TableroAjedrez(raiz,50)
ajedrez.PartesTablero()
ajedrez.fichas()
ajedrez.posicionarPiezas()
raiz.mainloop()
