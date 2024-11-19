import tkinter as tk
from gui import Interfaz

def main():
    root = tk.Tk()
    root.title("Análisis de Grafos - Proyecto Final")
    app = Interfaz(root)
    root.mainloop()

if __name__ == "__main__":
    main()
