import tkinter as tk
from tkinter import ttk
import random
from calculations import generar_matriz_k2, generar_matriz_k3
from graph_visualization import GrafoVisual

class Interfaz:
    def __init__(self, master):
        self.master = master

        # Marco principal
        self.frame = tk.Frame(master)
        self.frame.pack(padx=10, pady=10)

        # Número de nodos (puede variar entre 2 y 4)
        self.num_nodos = tk.IntVar(value=4)
        tk.Label(self.frame, text="Número de nodos (2-4):").grid(row=0, column=0, sticky="w")
        tk.Spinbox(self.frame, from_=2, to=4, textvariable=self.num_nodos, width=5).grid(row=0, column=1, sticky="w")

        # Sección: Matriz de Pesos
        self.matriz_pesos = self.generar_matriz_inicial(4)
        tk.Label(self.frame, text="Matriz de Pesos").grid(row=1, column=0, sticky="w")
        self.tabla_pesos = self.crear_tabla(4, 4)
        self.tabla_pesos.grid(row=2, column=0, pady=5)
        self.actualizar_tabla(self.tabla_pesos, self.matriz_pesos)

        # Botones para generar matrices y grafo
        tk.Button(self.frame, text="Dibujar Grafo", command=self.dibujar_grafo).grid(row=3, column=0, pady=5)
        tk.Button(self.frame, text="Generar Grafo Aleatorio", command=self.generar_grafo_aleatorio).grid(row=4, column=0, pady=5)

        # Panel del Grafo
        self.canvas_grafo = tk.Canvas(self.frame, width=400, height=400, bg="white")
        self.canvas_grafo.grid(row=0, column=2, rowspan=6, padx=10, pady=10)
        self.grafo_visual = GrafoVisual(self.canvas_grafo, self.matriz_pesos)

        # Sección: Matriz K2
        tk.Label(self.frame, text="Matriz K2").grid(row=5, column=0, sticky="w")
        self.tabla_k2 = self.crear_tabla(4, 4)
        self.tabla_k2.grid(row=6, column=0, pady=5)
        tk.Button(self.frame, text="Calcular K2", command=self.calcular_k2).grid(row=7, column=0, pady=5)

        # Sección: Matriz K3
        tk.Label(self.frame, text="Matriz K3").grid(row=5, column=2, sticky="w")
        self.tabla_k3 = self.crear_tabla(4, 4)
        self.tabla_k3.grid(row=6, column=2, pady=5)
        tk.Button(self.frame, text="Calcular K3", command=self.calcular_k3).grid(row=7, column=2, pady=5)

    def crear_tabla(self, filas, columnas):
        tabla = ttk.Treeview(self.frame, columns=list(range(columnas)), show="headings", height=filas)
        for i in range(columnas):
            tabla.heading(i, text=str(i + 1))
            tabla.column(i, width=50, anchor="center")
        return tabla

    def actualizar_tabla(self, tabla, matriz):
        tabla.delete(*tabla.get_children())
        for fila in matriz:
            tabla.insert("", "end", values=fila)

    def generar_matriz_inicial(self, n):
        return [[0 for _ in range(n)] for _ in range(n)]

    def dibujar_grafo(self):
        self.grafo_visual.matriz_pesos = self.matriz_pesos
        self.grafo_visual.dibujar()

    def generar_grafo_aleatorio(self):
        n = self.num_nodos.get()
        self.matriz_pesos = [[random.randint(0, 10) if i != j else 0 for j in range(n)] for i in range(n)]
        self.actualizar_tabla(self.tabla_pesos, self.matriz_pesos)
        self.dibujar_grafo()

    def calcular_k2(self):
        matriz_k2 = generar_matriz_k2(self.matriz_pesos)
        self.actualizar_tabla(self.tabla_k2, matriz_k2)

    def calcular_k3(self):
        matriz_k3 = generar_matriz_k3(self.matriz_pesos)
        self.actualizar_tabla(self.tabla_k3, matriz_k3)
