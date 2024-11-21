# Generador de Grafos y Trayectorias

Este proyecto fue desarrollado en Python y permite generar grafos ponderados, calcular trayectorias \(K2\) y \(K3\) basadas en una matriz de pesos y visualizar los resultados en una interfaz gráfica. 

_Integrantes:_ 
- Luis Alejandro Castrillón Pulgarín
- Sara López Marín

## Características del programa

- Genera grafos de 2 a 4 nodos, con pesos aleatorios entre 0 y 10.
- Permite calcular las trayectorias de longitud \(K_2\) y \(K_3\) basadas en la matriz de pesos del grafo.
- Muestra el grafo generado, la matriz de adyacencia correspondiente y sus trayectorias en una interfaz gráfica.
- Permite generar grafos aleatorios.
- Visualización clara de los nodos y aristas para entender mejor la estructura del grafo.
- Permite ver el grado de forma 3D y hacer la comparación entre el 2D y este último.

![image](https://github.com/user-attachments/assets/2654efe0-055a-4553-b72f-89af15284344)
![image](https://github.com/user-attachments/assets/404fa0e4-8ecc-43a3-93f1-45b8635d5f7a)

## Instrucciones para ejecutar el programa

### Requisitos previos
Instalar las siguientes librerías necesarias:
- `tkinter` (para la interfaz gráfica)
- `networkx` (para la generación y visualización de grafos)
- `matplotlib` (para graficar los grafos)

```bash
pip install networkx matplotlib
