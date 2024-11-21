import tkinter as tk
import math

class GrafoVisual:
    def __init__(self, canvas, matriz_pesos):
        self.canvas = canvas
        self.matriz_pesos = matriz_pesos
        self.nodos = {}

    def dibujar(self):
        self.canvas.delete("all")
        num_nodos = len(self.matriz_pesos)
        radio = 150  # Radio del círculo
        centro_x, centro_y = 200, 200  # Centro del canvas
        angulo = 360 / num_nodos

        # Dibujar nodos en forma circular
        for i in range(num_nodos):
            x = centro_x + radio * math.cos(math.radians(angulo * i))
            y = centro_y + radio * math.sin(math.radians(angulo * i))
            self.nodos[i] = (x, y)
            self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="skyblue")
            self.canvas.create_text(x, y, text=f"{i + 1}", font=("Arial", 10))

        # Dibujar aristas con pesos
        for i in range(num_nodos):
            for j in range(num_nodos):
                if self.matriz_pesos[i][j] != 0:
                    x1, y1 = self.nodos[i]
                    x2, y2 = self.nodos[j]
                    # Dibujar la línea de la arista con un pequeño desplazamiento
                    dx = (x2 - x1) / 20
                    dy = (y2 - y1) / 20
                    self.canvas.create_line(x1 + dx, y1 + dy, x2 - dx, y2 - dy, arrow=tk.LAST, width=2)
                    # Calcular la posición del peso a un lado de la arista
                    peso_x = (x1 + x2) / 2 - dy * 2
                    peso_y = (y1 + y2) / 2 + dx * 2
                    self.canvas.create_text(peso_x, peso_y, text=str(self.matriz_pesos[i][j]), fill="red")