import random
import tkinter as tk
import webbrowser
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np
from calculations import generar_matriz_k2, generar_matriz_k3
from graph_visualization import GrafoVisual


class Interfaz:
    def __init__(self, master):
        self.master = master

        # Contador para rastrear el número de veces que se ha generado un grafo aleatorio
        self.contador_grafos = 0

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
        self.actualizar_tabla(self.tabla_pesos, self.matriz_pesos, 4)

        # Botones para generar matrices y grafo
        tk.Button(self.frame, text="Dibujar Grafo", command=self.dibujar_grafo).grid(row=3, column=0, pady=5)
        tk.Button(self.frame, text="Generar Grafo Aleatorio", command=self.generar_grafo_aleatorio).grid(row=4,
                                                                                                         column=0,
                                                                                                         pady=5)
        tk.Button(self.frame, text="Mostrar Grafo 3D", command=self.generar_grafo_3d).grid(row=5, column=0, pady=5)

        # Panel del Grafo
        self.canvas_grafo = tk.Canvas(self.frame, width=400, height=400, bg="white")
        self.canvas_grafo.grid(row=0, column=2, rowspan=6, padx=10, pady=10)
        self.grafo_visual = GrafoVisual(self.canvas_grafo, self.matriz_pesos)

        # Sección: Matriz K2
        tk.Label(self.frame, text="Matriz K2").grid(row=6, column=0, sticky="w")
        tk.Button(self.frame, text="Calcular K2", command=self.calcular_k2).grid(row=6, column=1, pady=5,
                                                                                 padx=4)  # Ubicado junto al título Matriz K2
        self.tabla_k2 = self.crear_tabla(4, 4)
        self.tabla_k2.grid(row=7, column=0, columnspan=2, pady=5)

        # Sección: Matriz K3
        tk.Label(self.frame, text="Matriz K3").grid(row=6, column=2, sticky="w")
        tk.Button(self.frame, text="Calcular K3", command=self.calcular_k3).grid(row=7, column=3, pady=4,
                                                                                 padx=3)  # Ubicado junto al título Matriz K3
        self.tabla_k3 = self.crear_tabla(4, 4)
        self.tabla_k3.grid(row=7, column=2, columnspan=2, pady=5)

        # Sección: Matriz de Adyacencia
        tk.Label(self.frame, text="Matriz de Adyacencia").grid(row=8, column=0, sticky="w")
        self.tabla_adyacencia = self.crear_tabla(4, 4)
        self.tabla_adyacencia.grid(row=9, column=0, pady=5, columnspan=2)

        # Cargar y agregar la imagen en la esquina inferior derecha
        self.agregar_imagen()

    def agregar_imagen(self):
        # Ruta de la imagen
        ruta_imagen = "C:/Users/Alejo/PycharmProjects/PythonProject/logo_eafit_blanco.png"  # Cambia esta ruta a la de tu imagen
        # Cargar la imagen
        self.imagen = Image.open(ruta_imagen)
        self.imagen = self.imagen.resize((100, 100), Image.LANCZOS)  # Redimensionar la imagen si es necesario
        self.imagen_tk = ImageTk.PhotoImage(self.imagen)
        # Crear un Label para la imagen
        label_imagen = tk.Label(self.master, image=self.imagen_tk)
        label_imagen.image = self.imagen_tk  # Mantener una referencia a la imagen
        # Posicionar el Label en la esquina inferior derecha
        label_imagen.place(relx=1.0, rely=1.0, anchor='se')  # Ajusta relx y rely según sea necesario

    def crear_tabla(self, filas, columnas):
        tabla = ttk.Treeview(self.frame, columns=list(range(columnas)), show="headings", height=filas)
        for i in range(columnas):
            tabla.heading(i, text=str(i + 1))
            tabla.column(i, width=50, anchor="center")
        return tabla

    def actualizar_tabla(self, tabla, matriz, num_nodos):
        # Limpiar la tabla
        tabla.delete(*tabla.get_children())
        # Insertar los valores en la tabla
        for fila in matriz:
            fila.extend([''] * (num_nodos - len(fila)))  # Rellenar filas cortas con cadenas vacías
            tabla.insert("", "end", values=fila)
        # Rellenar filas vacías si hay menos filas que num_nodos
        for _ in range(num_nodos - len(matriz)):
            tabla.insert("", "end", values=[''] * num_nodos)

    def actualizar_adyacencia(self, matriz):
        # Crear la matriz de adyacencia a partir de la matriz de pesos
        matriz_adyacencia = [[1 if cell != 0 else 0 for cell in row] for row in matriz]
        self.actualizar_tabla(self.tabla_adyacencia, matriz_adyacencia, len(matriz))

    def generar_matriz_inicial(self, n):
        return [[0 for _ in range(n)] for _ in range(n)]

    def dibujar_grafo(self):
        self.grafo_visual.matriz_pesos = self.matriz_pesos
        self.grafo_visual.dibujar()
        self.actualizar_adyacencia(self.matriz_pesos)

    def generar_grafo_aleatorio(self):
        n = self.num_nodos.get()  # Obtener número de nodos del Spinbox
        self.matriz_pesos = [[random.randint(0, 10) if i != j else 0 for j in range(n)] for i in range(n)]

        self.contador_grafos += 1

        # Si el contador es múltiplo de 5, desconectar un nodo aleatoriamente
        if (self.contador_grafos % 5) == 0:
            nodo_desconectado = random.randint(0, n - 1)
            for i in range(n):
                self.matriz_pesos[nodo_desconectado][i] = 0
                self.matriz_pesos[i][nodo_desconectado] = 0

        self.actualizar_tabla(self.tabla_pesos, self.matriz_pesos, n)
        self.dibujar_grafo()

        # Actualizar las tablas K2 y K3 basado en el nuevo tamaño dejando filas adicionales vacías
        self.actualizar_tabla(self.tabla_k2, self.generar_matriz_inicial(n), n)
        self.actualizar_tabla(self.tabla_k3, self.generar_matriz_inicial(n), n)
        self.actualizar_adyacencia(self.matriz_pesos)

    def calcular_k2(self):
        matriz_k2 = generar_matriz_k2(self.matriz_pesos)
        self.actualizar_tabla(self.tabla_k2, matriz_k2, self.num_nodos.get())

    def calcular_k3(self):
        matriz_k3 = generar_matriz_k3(self.matriz_pesos)
        self.actualizar_tabla(self.tabla_k3, matriz_k3, self.num_nodos.get())

    def generar_grafo_3d(self):
        matriz_pesos = self.matriz_pesos  # Usar matriz_pesos de la instancia
        n = len(matriz_pesos)

        # Posicionar nodos en una esfera 3D
        theta = np.linspace(0, 2 * np.pi, n, endpoint=False)
        z = np.linspace(-1, 1, n)
        x = np.cos(theta)
        y = np.sin(theta)

        # Crear nodos en la esfera
        import plotly.graph_objects as go
        fig = go.Figure()
        fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='markers+text',
                                   marker=dict(size=10, color='skyblue'),
                                   text=[f"Nodo {i + 1}" for i in range(n)],
                                   textposition="top center"))

        # Dibujar aristas con pesos
        for i in range(n):
            for j in range(n):
                if matriz_pesos[i][j] != 0:  # Si hay una arista
                    # Calcular las posiciones con un pequeño desplazamiento para las aristas bidireccionales
                    dx = 0.1 * (x[j] - x[i])
                    dy = 0.1 * (y[j] - y[i])
                    dz = 0.1 * (z[j] - z[i])

                    # Dibujar la arista i --> j (desplazada en una dirección)
                    fig.add_trace(go.Scatter3d(
                        x=[x[i] + dx, x[j] + dx], y=[y[i] + dy, y[j] + dy], z=[z[i] + dz, z[j] + dz],
                        mode='lines',
                        line=dict(color='black', width=2),
                        name=f"Arista {i + 1} → {j + 1}"
                    ))

                    # Calcular la posición media para el peso
                    peso_x = (x[i] + x[j]) / 2 + dx
                    peso_y = (y[i] + y[j]) / 2 + dy
                    peso_z = (z[i] + z[j]) / 2 + dz

                    # Agregar el peso de la arista (i --> j)
                    fig.add_trace(go.Scatter3d(
                        x=[peso_x], y=[peso_y], z=[peso_z],
                        mode='text',
                        text=[str(matriz_pesos[i][j])],
                        textfont=dict(color="red", size=12)
                    ))

                    # Si hay una arista j --> i, dibujar la línea separada (desplazada en la dirección opuesta)
                    if (matriz_pesos[j][i] != 0) and (i != j):
                        fig.add_trace(go.Scatter3d(
                            x=[x[j] - dx, x[i] - dx], y=[y[j] - dy, y[i] - dy], z=[z[j] - dz, z[i] - dz],
                            mode='lines',
                            line=dict(color='blue', width=2, dash="dot"),
                            name=f"Arista {j + 1} → {i + 1}"
                        ))

                        # Calcular la posición media para el peso
                        peso_x = (x[j] + x[i]) / 2 - dx
                        peso_y = (y[j] + y[i]) / 2 - dy
                        peso_z = (z[j] + z[i]) / 2 - dz

                        # Agregar el peso de la arista (j --> i)
                        fig.add_trace(go.Scatter3d(
                            x=[peso_x], y=[peso_y], z=[peso_z],
                            mode='text',
                            text=[str(matriz_pesos[j][i])],
                            textfont=dict(color="red", size=12)
                        ))

        # Configurar diseño del gráfico
        fig.update_layout(scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z',
            xaxis=dict(showbackground=True),
            yaxis=dict(showbackground=True),
            zaxis=dict(showbackground=True)
        ))

        # Convertir a HTML y guardar en un archivo temporal
        html_content = fig.to_html(full_html=False)
        with open("grafo_3d.html", "w") as f:
            f.write(html_content)

        # Abrir el archivo HTML en el navegador
        webbrowser.open("grafo_3d.html")


# Configuración de la ventana principal de Tkinter
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Interfaz de Gráficos")
    app = Interfaz(root)
    root.mainloop()
