def filtrar_personaje(matriz: list[list], indice_columna: int, valor_buscado: str) -> list:
    """
    Filtra la matriz y devuelve una lista de personajes que coinciden con un valor en una columna específica.
    Esta función recorre la matriz, evalúa cada personaje y si el valor de una de sus características coincide con el 
    'valor_buscado', lo añade a una nueva lista.
    :param: matriz: La matriz con los datos de los personajes.
            indice_columna: El índice de la columna por la cual se desea filtrar.
            valor_buscado: El valor que se busca en la columna (por ejemplo, 'Saiyan').
    :returns: Una lista de listas (matriz) que contiene a todos los personajes que cumplen con la condición.
    """
    lista_filtrada = []

    for personaje in matriz:
        raza_actual = personaje[indice_columna]
        if raza_actual == valor_buscado:
            lista_filtrada.append(personaje)
    
    return lista_filtrada


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
        print("LA MATRIZ ESTÁ VACÍA. NO SE PUEDE DETERMINAR UN VALOR MAXIMO.")
        return None

    for fila in matriz:
        valor_actual = fila[indice_columna]
        if valor_maximo == None or valor_actual > valor_maximo:
            valor_maximo = valor_actual
    print(f'EL VALOR MAXIMO ES: {valor_maximo}.')
    
    return valor_maximo

#11.Filtrar Débiles: Filtrar/buscar en la matriz todos los personajes cuyo poder no superen el poder de personajes de 
# raza Saiyan.
def filtrar_minimo(lista_personajes: list, indice_columna: int) -> int:
    """
    Filtra y devuelve el valor mínimo de una columna numérica en una lista de personajes.
    Esta función recorre la lista de personajes y compara los valores en una columna específica para encontrar el valor 
    numérico más bajo.
    :param: lista_personajes: Una lista de listas que contiene a los personajes a analizar.
            indice_columna: El índice de la columna que se desea analizar.
    :returns: Retorna el valor mínimo de la columna o None si la lista está vacía.
    """
    if not lista_personajes:
        return None
    
    valor_minimo = None
    for personaje in lista_personajes:
        valor_actual = personaje[indice_columna]
        if valor_minimo == None or valor_actual < valor_minimo:
            valor_minimo = valor_actual
    print(f'EL VALOR MINIMO ES: {valor_minimo}.')

    return valor_minimo


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

#10. Filtrar Menor velocidad: Filtrar/Buscar y mostrar la info de los personajes que no superen el promedio de velocidad.

def filtrar_por_promedio(matriz: list[list], indice_columna: int, promedio_obtenido: float) -> list:
    """
    Filtra y devuelve una lista de personajes que no superan un promedio dado.
    La función recorre la matriz y evalúa cada personaje. Si el valor de su característica es menor o igual al promedio 
    proporcionado, el personaje es incluido en una nueva lista.
    :param:
        matriz (list[list]): La matriz con todos los datos de los personajes.
        indice_columna: El índice de la columna que contiene el dato a comparar.
        promedio_obtenido: El valor del promedio que se usa como referencia para el filtro.
    :returns: Una lista de listas que contiene a todos los personajes que cumplen con la condición.
    """
    personajes_filtrados_promedio = []

    for fila in matriz:
        valor_actual = fila[indice_columna]

        if valor_actual <= promedio_obtenido:
            personajes_filtrados_promedio.append(fila)

    return personajes_filtrados_promedio


#14.Filtrar Kryptonian: Solamente de los personajes que NO sean raza Kryptonian, mostrar la info completa de los que 
# superen o igualen el promedio de poder de personajes de raza Kryptonian.
def filtrar_superen_promedio(lista_procesada: list, indice_columna: int, promedio_a_comparar: float):
    """
    Filtra y devuelve una lista de personajes que superan o igualan un valor promedio dado.
    La función recorre una lista de personajes y compara el valor de una columna específica con el promedio proporcionado.
    Se incluyen en la lista resultante a todos los personajes cuyo valor sea mayor o igual (>=) al promedio.
    :param: lista_procesada: Una lista de listas que contiene a los personajes a filtrar.
            indice_columna: El índice de la columna que contiene el dato a comparar.
            promedio_a_comparar: El valor del promedio que se usa como umbral para el filtro.
    :returns: Una lista de listas (matriz) que contiene a los personajes que superan o igualan el promedio.
    """
    personajes_superen_promedio = []

    for personaje in lista_procesada:
        if personaje[indice_columna] >= promedio_a_comparar:
            personajes_superen_promedio.append(personaje)

    return personajes_superen_promedio


    









