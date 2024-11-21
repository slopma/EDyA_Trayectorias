def generar_matriz_k2(matriz_pesos):
    """
    Calcula la matriz K^2 
    """
    n = len(matriz_pesos)
    k2 = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            # trayectorias de longitud 2
            for k in range(n):
                k2[i][j] += matriz_pesos[i][k] * matriz_pesos[k][j]

    return k2


def generar_matriz_k3(matriz_pesos):
    """
    Calcula la matriz K^3 
    """
    n = len(matriz_pesos)
    k3 = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            # trayectorias de longitud 3
            for k in range(n):
                for l in range(n):
                    k3[i][j] += matriz_pesos[i][k] * matriz_pesos[k][l] * matriz_pesos[l][j]

    return k3
