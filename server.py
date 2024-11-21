from flask import Flask, render_template
import plotly.graph_objects as go
import numpy as np
import pickle

app = Flask(__name__)

def generar_grafo_3d(matriz_pesos):
    n = len(matriz_pesos)

    # Posicionar nodos en una esfera 3D
    theta = np.linspace(0, 2 * np.pi, n, endpoint=False)
    z = np.linspace(-1, 1, n)
    x = np.cos(theta)
    y = np.sin(theta)

    # Crear nodos en la esfera
    fig = go.Figure()
    fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='markers+text',
                               marker=dict(size=10, color='skyblue'),
                               text=[f"Nodo {i + 1}" for i in range(n)],
                               textposition="top center"))

    # Dibujar aristas
    for i in range(n):
        for j in range(n):
            if matriz_pesos[i][j] != 0:
                fig.add_trace(go.Scatter3d(
                    x=[x[i], x[j]], y=[y[i], y[j]], z=[z[i], z[j]],
                    mode='lines',
                    line=dict(color='black', width=2)
                ))

    # Configurar diseño del gráfico
    fig.update_layout(scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z'
    ))

    # Convertir a HTML
    return fig.to_html(full_html=False)

@app.route("/")
def index():
    # Cargar la matriz de pesos guardada
    with open("matriz_pesos.pkl", "rb") as f:
        matriz_pesos = pickle.load(f)

    # Generar grafo 3D
    grafo_html = generar_grafo_3d(matriz_pesos)
    return render_template("index.html", grafo=grafo_html)

if __name__ == "__main__":
    app.run(debug=True)
