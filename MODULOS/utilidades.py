import validaciones, filtros, mostrar_datos, calculos

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
    Orquesta el proceso para filtrar y mostrar personajes que no superan un promedio.
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

    lista_android = filtros.filtrar_personaje(matriz, 2, tipo_buscado)

    promedio_inteligencia_android = calculos.calcular_promedio(lista_android, 5)

    promedio_poder_android = calculos.calcular_promedio(lista_android, 4)

    print(f"EL PROMEDIO DE INTELIGENCIA DE LOS ANDROID ES: {promedio_inteligencia_android}")
    print(f"EL PROMEDIO DE PODER DE LOS ANDROID ES: {promedio_poder_android}")

#12.Filtrar No-Binario Veloces:  Filtrar/buscar en la matriz todos los personajes de género No-Binario que posean la más 
# alta velocidad.
def procesar_no_binario(matriz: list[list], tipo_buscado: str) -> None:

    lista_no_binario = filtros.filtrar_personaje(matriz, 3, tipo_buscado)

    velocidad_maxima_no_binario = filtros.filtrar_maximo(lista_no_binario, 6)

    personajes_velocidad_maxima = filtros.filtrar_maximos_repetidos(lista_no_binario, 6, velocidad_maxima_no_binario)

    print('LOS PERSONAJES MAS VELOCES DEL GÉNERO NO-BINARIO SON: ')
    mostrar_datos.mostrar_personajes(personajes_velocidad_maxima)

#14.Filtrar Kryptonian: Solamente de los personajes que NO sean raza Kryptonian, mostrar la info completa de los que 
# superen o igualen el promedio de poder de personajes de raza Kryptonian.

def procesar_kryptonian(matriz: list[list]) -> int:
    lista_kryptonian = filtros.filtrar_personaje(matriz, 2, 'Kryptonian')

    promedio_poder_kryptonian = calculos.calcular_promedio(lista_kryptonian, 4)

    return promedio_poder_kryptonian

def procesar_no_personaje(matriz: list[list], indice_columna: int, raza_a_comparar) -> list:

    no_personaje = []
    for personaje in matriz:
        if personaje[indice_columna] != raza_a_comparar:
            no_personaje.append(personaje)

    return no_personaje

def obtener_filtro_kryptonian(matriz: list[list]) -> None:

    promedio_kryptonian = procesar_kryptonian(matriz)

    lista_no_kryptonian = procesar_no_personaje(matriz, 2, 'Kryptonian')

    personajes_superen_promedio = filtros.filtrar_superen_promedio(lista_no_kryptonian, 4, promedio_kryptonian)

    print('LOS PERSONAJES NO KRYPTONIAN QUE SUPERAN/IGUALAN EL PODER DE LOS KRIPTONIAN SON: ')
    mostrar_datos.mostrar_personajes(personajes_superen_promedio)


#15.Filtrar Saiyan Power: Mostrar la info de los personajes (que no sean raza Saiyan) cuyos stats estén por debajo del 
# índice de ataque Saiyan, obtenido de la ecuación (promedio poder + promedio inteligencia + promedio velocidad) / 3. 
# Para saber esto, primero deberás calcular el promedio de esos stats de los personajes cuya raza sea Saiyan.

def procesar_saiyan_power(matriz: list[list]) -> float:

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
    
    no_saiyan = procesar_no_personaje(matriz, 2, 'Saiyan')

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
    indice_ataque = procesar_saiyan_power(matriz)

    if indice_ataque > 0:
        procesar_no_saiyan(matriz, indice_ataque)





