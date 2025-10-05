
def filtrar_maximo(matriz: list[list], indice_columna: int) -> int:
    """
    Filtra y devuelve el valor máximo de una columna numérica en una matriz.
    Recorre la matriz y compara los valores de una columna específica para encontrar el valor numérico más alto.
    :param: matriz: La matriz con los datos a analizar.
            indice_columna: El índice de la columna que se desea analizar.
    :returns: int | None: Retorna el valor máximo de la columna o None si la matriz está vacía.
    """
    valor_maximo = None

    if not matriz:
        print("La matriz está vacía. No se puede determinar un valor máximo.")
        return None

    for fila in matriz:
        valor_actual = fila[indice_columna]
        if valor_maximo == None or valor_actual > valor_maximo:
            valor_maximo = valor_actual
    print(f'El valor maximo es: {valor_maximo}')
    
    return valor_maximo

def filtrar_maximos_repetidos(matriz: list[list], indice_columna: int, maximo_obtenido: int) -> list:
    """
    Filtra y devuelve una lista de personajes que tienen un valor máximo en una columna específica.
    La función recorre la matriz y compara el valor de una columna en cada fila con el valor máximo proporcionado.
    Agrega a una lista todos los personajes que coincidan con ese valor.
    :param: matriz: La matriz con los datos de los personajes.
            indice_columna: El índice de la columna a filtrar.
            maximo_obtenido: El valor máximo que se busca en la columna.
    :returns: Devuelve una lista de listas que contiene a todos los personajes que cumplen con la condición del valor 
    máximo.
    """
    personajes_maximo = []
    for fila in matriz:
        if fila[indice_columna] == maximo_obtenido:
            personajes_maximo.append(fila)

    return personajes_maximo






