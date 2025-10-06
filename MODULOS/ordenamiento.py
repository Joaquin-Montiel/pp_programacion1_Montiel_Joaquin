
#16. Ordenar por Más Inteligente: Ordenar la matriz según inteligencia DES
#19. Ordenar por Más Velocidad: Ordenar la matriz según velocidad ASC
def encontrar_elemento_intercambio(matriz: list[list], indice_actual: int, indice_columna: int, modo: str = 'DESC') -> int:
    """
    Busca el índice del elemento más extremo (mínimo o máximo) en la sub-lista no ordenada.
    Esta función implementa el bucle interno del Selection Sort. Itera sobre los elementos desde 'indice_actual + 1' hasta
    el final de la matriz, buscando el valor que debe ser colocado en la posición 'indice_actual'.
    :param: matriz: La matriz de personajes que está siendo ordenada.
            indice_actual: El índice de la posición a partir de la cual debe comenzar la búsqueda (la parte ya ordenada 
            se ignora).
            indice_columna: El índice de la columna que contiene el valor numérico a comparar (ej: 4 para Inteligencia).
            modo: Define el criterio de búsqueda: 'DESC' (busca el mayor) o 'ASC' (busca el menor). Por defecto es 'DESC'.
    :returns: El índice (posición) del elemento más extremo encontrado en la sub-lista.
    """
    largo_matriz = len(matriz)
    indice_extremo = indice_actual

    for siguiente_indice in range(indice_actual + 1, largo_matriz):

            elemento_extremo = matriz[indice_extremo][indice_columna]
            siguiente_elemento = matriz[siguiente_indice][indice_columna]

            if (elemento_extremo > siguiente_elemento and modo == 'ASC') or\
                (elemento_extremo < siguiente_elemento and modo == 'DESC'):
                indice_extremo = siguiente_indice
    
    return indice_extremo

#20.Ordenar personalizado: Ordenar la matriz según lo siguiente:
#Todos los personajes deben estar agrupados por Raza
#Cada personaje de cada raza, debe estar ordenado según poder DES en su raza.
#Las Razas en la matriz deben aparecer de forma Alfabética

def ordenar_selection_sort(matriz: list[list], indice_columna: int, modo: str = 'DESC') ->  list[list]:
    """
    Ordena la matriz de personajes utilizando el algoritmo Selection Sort.
    Esta función implementa el bucle externo del Selection Sort. En cada iteración, llama a 'encontrar_elemento_intercambio' 
    para localizar el elemento más extremo en la porción no ordenada de la matriz y lo coloca en la posición correcta 
    mediante un intercambio.
    :param: matriz: La matriz de personajes a ordenar. La matriz se modifica.
            indice_columna: El índice de la columna que se usará como clave para el ordenamiento.
            modo: El sentido del ordenamiento: 'DESC' (Descendente) o 'ASC' (Ascendente). Por defecto es 'DESC'.
    :returns: La matriz ordenada.
    """
    largo_matriz = len(matriz)

    for indice_actual in range(largo_matriz - 1):
        
        indice_extremo = encontrar_elemento_intercambio(matriz, indice_actual, indice_columna, modo)
        
        if indice_extremo != indice_actual:
            auxiliar = matriz[indice_actual]
            matriz[indice_actual] = matriz[indice_extremo]
            matriz[indice_extremo] = auxiliar

    return matriz






