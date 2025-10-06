
def calcular_promedio(matriz: list[list], indice_columna: int) -> float:
    """
    Calcula el promedio de los valores en una columna específica de una matriz.
    Esta función recorre la matriz, suma los valores numéricos de la columna indicada y devuelve el promedio. 
    :param: matriz: La matriz con los datos de los personajes.
            indice_columna: El índice de la columna que se desea promediar.
    :returns: float: El promedio de los valores de la columna.
    """
    cantidad_personajes = len(matriz)
    suma_dato_personaje = 0

    for fila in matriz:
        valor_actual = fila[indice_columna]
        suma_dato_personaje += valor_actual

    if cantidad_personajes > 0:
        promedio = suma_dato_personaje / cantidad_personajes
        return promedio
    else:
        promedio = 0
        return promedio

    

    