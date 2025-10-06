import validaciones, filtros, mostrar_datos, calculos, ordenamiento

#1.Crear Matriz: para ello deberá crear una función que en base a las listas, cree una matriz con los datos para trabajar.

def crear_matriz(lista_nombres: list, lista_alias: list, lista_razas: list, lista_generos: list, lista_poderes: list, 
                lista_inteligencias: list, lista_velocidades: list) -> list[list]:
    """
    Esta función recorre todas las listas de entrada, tomando un elemento de cada una para crear una nueva fila. 
    Este proceso se repite hasta que todos los elementos hayan sido procesados, construyendo una matriz organizada y 
    completa.
    :param:
        lista_nombres: Lista de nombres de los personajes.
        lista_alias: Lista de alias de los personajes.
        lista_razas: Lista de razas de los personajes.
        lista_generos: Lista de géneros de los personajes.
        lista_poderes: Lista de poderes de los personajes.
        lista_inteligencias: Lista de niveles de inteligencia.
        lista_velocidades: Lista de niveles de velocidad.
    :returns: Devuelve una matriz donde cada sublista representa una fila de datos de un personaje con todos sus atributos.
    """
    matriz = []
    nombres = len(lista_nombres)

    for indice_nombre in range(nombres):
        nombre = lista_nombres[indice_nombre]
        alias = lista_alias[indice_nombre]
        raza = lista_razas[indice_nombre]
        genero = lista_generos[indice_nombre]
        poder = lista_poderes[indice_nombre]
        inteligencia = lista_inteligencias[indice_nombre]
        velocidad = lista_velocidades[indice_nombre]

        matriz.append([nombre, alias, raza, genero, poder, inteligencia, velocidad])

    return matriz

#2.Agregar personaje: Debes poder agregar un personaje a la matriz, los datos a incluir son: Nombre, Alias, Raza, Género, 
# Inteligencia, Poder, Velocidad. 

def agregar_personaje(matriz: list[list]) -> list[list]:
    """
    Solicita al usuario los datos de un nuevo personaje y lo agrega a la matriz.
    Esta función guía al usuario a través de un proceso de entrada de datos,asegurándose de que cada dato cumpla con la
    validación correspondiente. Una vez que todos los datos son válidos, los agrupa en una nueva fila y la añade al final 
    de la matriz principal.
    :param: matriz: La matriz a la que se desea agregar el nuevo personaje.
    :returns: La matriz actualizada con el nuevo personaje ya agregado.
    """
    nuevo_personaje = [ 
        validaciones.validar_str('Ingrese el nombre del personaje: '),
        validaciones.validar_str('Ingrese el alias del personaje: '),
        validaciones.validar_str('Ingrese el raza del personaje: '),
        validaciones.validar_str('Ingrese el genero del personaje: '),
        validaciones.validar_int('Ingrese la cantidad de inteligencia del personaje: '),
        validaciones.validar_int('Ingrese la cantidad de poder del personaje: '),
        validaciones.validar_int('Ingrese la cantidad de velocidad del personaje: ')
        ]
    
    matriz.append(nuevo_personaje)
    print(f'El personaje {nuevo_personaje}, ha sido agregado correctamente.')
    return matriz

def procesar_saiyanes(matriz: list[list]) -> None:
    """
    Coordina el proceso para filtrar y mostrar la información de los personajes Saiyan.
    Esta función utiliza el módulo de filtros para obtener una lista con todos los personajes cuya raza es 'Saiyan' y 
    luego usa el módulo de mostrar datos para imprimir la información completa en la consola.
    :param: matriz: La matriz con todos los datos de los personajes.
    :returns: La función no devuelve un valor, solo imprime el resultado.
    """

    saiyanes_filtrados = filtros.filtrar_personaje(matriz, 2, 'Saiyan')

    print('LOS PERSONAJES SAIYAN SON: ')
    mostrar_datos.mostrar_personajes(saiyanes_filtrados)


def procesar_personaje_maximo(matriz: list[list], indice_columna: int, tipo_filtro: str) -> None:
    """
    Procesa y muestra los personajes con el valor máximo en una columna específica.
    Esta función orquesta la lógica para encontrar y mostrar a los personajes más destacados de la matriz. Primero, 
    determina el valor máximo en una columna dada. Luego, filtra a todos los personajes que poseen ese valor y, 
    finalmente, los imprime en la consola.
    :param: matriz: La matriz con todos los datos de los personajes.
            indice_columna: El índice de la columna que se desea analizar(ej. 5 para inteligencia, 4 para poder).
    :returns: La función no devuelve un valor, solo imprime el resultado.
    """

    poder_maximo = filtros.filtrar_maximo(matriz, indice_columna)

    personajes_maximos = filtros.filtrar_maximos_repetidos(matriz,indice_columna, poder_maximo)

    mostrar_datos.mostrar_personajes_filtrados(personajes_maximos, indice_columna, tipo_filtro)

def procesar_personajes_por_pormedio(matriz: list[list], indice_columna: int, tipo_filtro: str) -> None:
    """
    Maneja el proceso para filtrar y mostrar personajes que no superan un promedio.
    Esta función coordina tres tareas principales:
    1. Calcula el promedio de una característica numérica de la matriz.
    2. Filtra a los personajes cuyo valor para esa característica es igual o menor al promedio.
    3. Muestra los datos de los personajes que cumplen con el filtro.
    :param: matriz: La matriz con todos los datos de los personajes.
            indice_columna: El índice de la columna que se desea analizar.
            tipo_filtro (str): Una cadena de texto que describe el filtro aplicado para usar en el mensaje de salida.
    :returns: La función no devuelve un valor, solo imprime el resultado.
    """
    promedio_minimo = calculos.calcular_promedio(matriz, indice_columna)

    personajes_minimo_promedio = filtros.filtrar_por_promedio(matriz, indice_columna, promedio_minimo)

    mostrar_datos.mostrar_personajes_filtrados(personajes_minimo_promedio, indice_columna, tipo_filtro)

def procesar_personajes_debiles(matriz: list[list], tipo_buscado: str) -> None:
    """
    Coordina el proceso para filtrar y mostrar los personajes cuyo poder no supera el poder mínimo de una raza específica.
    La función realiza los siguientes pasos:
    1. Filtra la matriz para obtener solo los personajes de la raza especificada.
    2. Calcula el valor de poder más bajo ('mínimo') entre esa raza.
    3. Filtra la matriz COMPLETA para encontrar a todos los personajes cuyo poder es menor o igual al mínimo de la raza 
    de referencia.
    4. Muestra la información de los personajes resultantes.
    :param: matriz: La matriz con todos los datos de los personajes.
            tipo_buscado: El nombre de la raza que se usará como referencia para el mínimo de poder (ej: 'Saiyan').
    :returns: La función no devuelve un valor, solo imprime el resultado.
    """
    lista_saiyan = filtros.filtrar_personaje(matriz, 2, tipo_buscado)

    poder_minimo_saiyan = filtros.filtrar_minimo(lista_saiyan, 5)

    personajes_debiles = []
    for personaje in matriz:
        if personaje[5] <= poder_minimo_saiyan:
            personajes_debiles.append(personaje)

    if personajes_debiles:
        print(f'LOS PERSONAJES DE PODERQUE NO SUPERAN EL MINIMO SAIYAN SON: ')
        mostrar_datos.mostrar_personajes(personajes_debiles)

def procesar_android_por_promedio(matriz: list[list], tipo_buscado: str) -> None:
    """
    Coordina el proceso para calcular y mostrar el promedio de inteligencia y poder de una raza específica.
    La función realiza los siguientes pasos:
    1. Filtra la matriz para obtener una lista que contenga solo a los personajes de la raza buscada.
    2. Calcula el promedio de la característica 'inteligencia' de esa lista filtrada.
    3. Calcula el promedio de la característica 'poder' de esa lista filtrada.
    4. Imprime ambos promedios calculados.
    :param: matriz: La matriz con todos los datos de los personajes.
            tipo_buscado: El nombre de la raza que se desea analizar (ej: 'Android').
    :returns: La función no devuelve ningún valor, solo imprime los promedios calculados.
    """
    lista_android = filtros.filtrar_personaje(matriz, 2, tipo_buscado)

    promedio_inteligencia_android = calculos.calcular_promedio(lista_android, 5)

    promedio_poder_android = calculos.calcular_promedio(lista_android, 4)

    print(f"EL PROMEDIO DE INTELIGENCIA DE LOS ANDROID ES: {promedio_inteligencia_android}")
    print(f"EL PROMEDIO DE PODER DE LOS ANDROID ES: {promedio_poder_android}")

#12.Filtrar No-Binario Veloces:  Filtrar/buscar en la matriz todos los personajes de género No-Binario que posean la más 
# alta velocidad.
def procesar_no_binario(matriz: list[list], tipo_buscado: str) -> None:
    """
    Coordina el proceso para filtrar y mostrar los personajes de un género específico que poseen la velocidad más alta.
    La función realiza tres pasos de filtrado:
    1. Filtra la matriz para obtener solo los personajes del género especificado.
    2. Determina el valor máximo de 'velocidad' entre esos personajes.
    3. Filtra la lista de ese género nuevamente para incluir a todos los personajes que tienen exactamente esa velocidad 
    máxima.
    4. Muestra la información de los personajes resultantes.
    :param: matriz: La matriz con todos los datos de los personajes.
            tipo_buscado: El nombre del género que se desea filtrar.
    :returns: La función no devuelve ningún valor, solo imprime los resultados.
    """
    lista_no_binario = filtros.filtrar_personaje(matriz, 3, tipo_buscado)

    velocidad_maxima_no_binario = filtros.filtrar_maximo(lista_no_binario, 6)

    personajes_velocidad_maxima = filtros.filtrar_maximos_repetidos(lista_no_binario, 6, velocidad_maxima_no_binario)

    print('LOS PERSONAJES MAS VELOCES DEL GÉNERO NO-BINARIO SON: ')
    mostrar_datos.mostrar_personajes(personajes_velocidad_maxima)

#14.Filtrar Kryptonian: Solamente de los personajes que NO sean raza Kryptonian, mostrar la info completa de los que 
# superen o igualen el promedio de poder de personajes de raza Kryptonian.

def procesar_kryptonian(matriz: list[list]) -> int:
    """
    Coordina el proceso para filtrar a los personajes de raza 'Kryptonian' y calcular su promedio de poder.
    Esta función de procesamiento realiza dos pasos esenciales:
    1. Filtra la matriz completa para obtener solo los personajes de la raza 'Kryptonian'.
    2. Calcula el promedio del valor de 'poder'para esos personajes.
    :param: matriz: La matriz con todos los datos de los personajes.
    :returns: El promedio de poder calculado para los personajes Kryptonian.
    """
    lista_kryptonian = filtros.filtrar_personaje(matriz, 2, 'Kryptonian')

    promedio_poder_kryptonian = calculos.calcular_promedio(lista_kryptonian, 4)

    return promedio_poder_kryptonian


def obtener_filtro_kryptonian(matriz: list[list]) -> None:
    """
    Coordina el proceso para filtrar y mostrar los personajes NO-Kryptonian cuyo poder supera o iguala el promedio de 
    poder de los Kryptonian.
    Esta función realiza la solución completa en cuatro pasos:
    1. Calcula el promedio de poder de los personajes de raza 'Kryptonian'.
    2. Filtra la matriz para obtener una lista con todos los personajes que NO son 'Kryptonian'.
    3. Filtra la lista de NO-Kryptonian para encontrar aquellos cuyo valor de poder es mayor o igual al promedio calculado.
    4. Muestra la información de los personajes resultantes.
    :param: matriz: La matriz con todos los datos de los personajes.
    :returns: La función no devuelve ningún valor, solo imprime los resultados.
    """

    promedio_kryptonian = procesar_kryptonian(matriz)

    lista_no_kryptonian = filtros.filtrar_no_personaje(matriz, 2, 'Kryptonian')

    personajes_superen_promedio = filtros.filtrar_superen_promedio(lista_no_kryptonian, 4, promedio_kryptonian)

    print('LOS PERSONAJES NO KRYPTONIAN QUE SUPERAN/IGUALAN EL PODER DE LOS KRIPTONIAN SON: ')
    mostrar_datos.mostrar_personajes(personajes_superen_promedio)


#15.Filtrar Saiyan Power: Mostrar la info de los personajes (que no sean raza Saiyan) cuyos stats estén por debajo del 
# índice de ataque Saiyan, obtenido de la ecuación (promedio poder + promedio inteligencia + promedio velocidad) / 3. 
# Para saber esto, primero deberás calcular el promedio de esos stats de los personajes cuya raza sea Saiyan.

def procesar_saiyan_power(matriz: list[list]) -> float:
    """
    Calcula el 'Índice de Ataque Saiyan', que es el promedio de los tres stats principales (Poder, Inteligencia y 
    Velocidad) de todos los personajes Saiyan.
    La función realiza los siguientes pasos:
    1. Filtra la matriz para obtener solo los personajes de raza 'Saiyan'.
    2. Calcula el promedio individual de Poder, Inteligencia y Velocidad para ese grupo.
    3. Suma los tres promedios y divide por tres para obtener el Índice de Ataque Saiyan.
    :param: matriz: La matriz con todos los datos de los personajes.
    :returns: El valor numérico del Índice de Ataque Saiyan. Retorna None si no se encuentran personajes Saiyan.
    """
    personajes_saiyan = filtros.filtrar_personaje(matriz, 2, 'Saiyan')

    if not personajes_saiyan:
        print("No se encontraron personajes Saiyan para calcular el índice de ataque.")
        return
    
    promedio_poder = calculos.calcular_promedio(personajes_saiyan, 4)
    promedio_inteligencia = calculos.calcular_promedio(personajes_saiyan, 5)
    promedio_velocidad = calculos.calcular_promedio(personajes_saiyan, 6)

    indice_ataque_saiyan = (promedio_poder + promedio_inteligencia + promedio_velocidad) / 3

    print(f'EL INDICE DE ATAQUE SAIYAN ES: {indice_ataque_saiyan}.')
    return indice_ataque_saiyan

def procesar_no_saiyan(matriz: list[list], ataque_saiyan: float) -> None:
    """
    Filtra y muestra la información de los personajes que NO son de raza Saiyan cuyos TRES stats principales 
    (Poder, Inteligencia y Velocidad) son estrictamente menores que el Índice de Ataque Saiyan proporcionado.
    La función realiza los siguientes pasos:
    1. Filtra la matriz para obtener la lista de personajes que NO son de raza 'Saiyan'.
    2. Itera sobre esa lista, comparando individualmente el Poder, la Inteligencia y la Velocidad de cada personaje 
    contra el 'ataque_saiyan' (el umbral de debilidad).
    3. Si los tres stats son menores al umbral, el personaje se considera "débil" y se añade a la lista de resultados.
    4. Muestra la información de los personajes resultantes.
    :param: matriz: La matriz con todos los datos de los personajes.
            ataque_saiyan: El umbral de debilidad (Índice de Ataque Saiyan, obtenido en la funcion anterior) contra el 
            que se comparan los stats.
    :returns: La función no devuelve ningún valor, solo imprime los resultados.
    """
    no_saiyan = filtros.filtrar_no_personaje(matriz, 2, 'Saiyan')

    personaje_debajo_del_ataque_saiyan = []
    for personaje in no_saiyan:
        poder = personaje[4]
        inteligencia = personaje[5]
        velocidad = personaje[6]

        if (poder < ataque_saiyan and inteligencia < ataque_saiyan and velocidad < ataque_saiyan):
            personaje_debajo_del_ataque_saiyan.append(personaje)

    print(f"LOS PERSONAJES NO SAIYAN CON TODOS LOS STATS POR DEBAJO DEL ATAQUE SAIYAN SON:")
    mostrar_datos.mostrar_personajes(personaje_debajo_del_ataque_saiyan) 

def obtener_personajes_debajo_indice_ataque(matriz: list[list]) -> None:
    """
    Coordina y maneja el proceso completo para resolver el problema de 'Filtrar Saiyan Power'.
    Esta función se encarga de:
    1. Calcular el Índice de Ataque Saiyan (umbral de debilidad).
    2. Verificar que el índice calculado sea válido (mayor que 0).
    3. Llamar a la función de filtrado para encontrar y mostrar a los personajes NO-Saiyan cuyos tres stats principales 
    (Poder, Inteligencia y Velocidad) estén por debajo de ese índice.
    :param: matriz: La matriz con todos los datos de los personajes.
    :returns: La función no devuelve ningún valor, ya que las funciones que llama se encargan de la impresión del 
    resultado final.
    """

    indice_ataque = procesar_saiyan_power(matriz)

    if indice_ataque > 0:
        procesar_no_saiyan(matriz, indice_ataque)

#17.Ordenar por Menos Inteligente [not Human]: Ordenar la matriz según inteligencia ASC de personajes cuya raza no sea 
# Human
#18.Ordenar por Más Poder [not Human]: Ordenar la matriz según poder DES de los personajes cuya raza no sea Human

def manejar_ordenamiento_filtro_inteligencia_no_human(matriz: list[list]) -> None:
    """
    Coordina el proceso para filtrar, ordenar y mostrar los personajes que NO son de raza 'Human', ordenados de forma 
    Ascendente (ASC) por su Inteligencia.
    La función realiza los siguientes pasos:
    1. Filtra la matriz para obtener una lista con todos los personajes que NO son 'Human'.
    2. Ordena esa lista filtrada utilizando el algoritmo Selection Sort, basándose en la columna de Inteligencia y 
    en modo Ascendente (de menor a mayor).
    3. Muestra la información completa de los personajes en el orden resultante.
    :param: matriz): La matriz con todos los datos de los personajes.
    ;returns:La función no devuelve ningún valor, solo imprime los resultados.
    """

    personajes_no_human = filtros.filtrar_no_personaje(matriz, 2, 'Human')

    matriz_no_human_ordenada = ordenamiento.ordenar_selection_sort(personajes_no_human, 5, 'ASC')

    mostrar_datos.mostrar_personajes_filtrados(matriz_no_human_ordenada, 5, 'menos')


def manejar_ordenamiento_filtro_poder_no_human(matriz: list[list]) -> None:
    """
    Coordina el proceso para filtrar, ordenar y mostrar los personajes que NO son de raza 'Human', ordenados de forma 
    Descendente (DESC) por su Poder.
    La función realiza los siguientes pasos:
    1. Filtra la matriz para obtener una lista con todos los personajes que NO son 'Human'.
    2. Ordena esa lista filtrada utilizando el algoritmo Selection Sort, basándose en la columna de Poder y en modo 
    Descendente (de mayor a menor, que es el valor por defecto de la función ordenar_selection_sort).
    3. Muestra la información completa de los personajes en el orden resultante.
    :param: matriz: La matriz con todos los datos de los personajes.
    :returns: La función no devuelve ningún valor, solo imprime los resultados.
    """
    personajes_no_human = filtros.filtrar_no_personaje(matriz, 2, 'Human')

    matriz_no_human_ordenada = ordenamiento.ordenar_selection_sort(personajes_no_human, 4)

    mostrar_datos.mostrar_personajes_filtrados(matriz_no_human_ordenada, 4, 'mas')





