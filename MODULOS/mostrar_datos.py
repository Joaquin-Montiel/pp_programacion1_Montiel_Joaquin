
def mostrar_menu_principal() -> None:
    """
    Muestra en la consola un menú de opciones para la gestión de un set de datos
    de personajes. El menú está diseñado para que el usuario pueda seleccionar
    diferentes acciones como crear, agregar, consultar, filtrar, ordenar y salir.
    El formato del menú está predefinido en una cadena de texto.
    :returns: La función no retorna ningún valor, simplemente imprime el menú en la consola.
    """
    menu_opciones =\
        f"""
            ****MENU DE HÉROES Y VILLANOS****
            ---------------------------------
            1. CREAR MATRIZ.
            2. AGREGAR PERSONAJE.
            3. CANTIDAD DE PERSONAJES QUE HAY EN EL SET DE DATOS.
            4. CANTIDAD DE PERSONAJES QUE SEAN DE RAZA HUMAN O RAZA COMUPESTA.
            5. CANTIDAD DE PERSONAJES CUYA RAZA NO SEA HUMAN O NO TENGAN HUMAN EN SU PARTE COMPUESTA.
            6. INFO DE TODOS LOS PERSONAJES FORMATO: [NOMBRE, ALIAS, RAZA, GENERO, INTELIGENCIA, PODER, VELOCIDAD].
            7. INFO DE LOS SAIYAN FORMATO: [NOMBRE, ALIAS, RAZA, GENERO, INTELIGENCIA, PODER, VELOCIDAD].
            8. INFO DE/LOS PERSONAJES MAS PODEROSOS.
            9. INFO DE/LOS PERSONAJES MAS INTELIGENTES.
            10. INFO DE/LOS PERSONAJES QUE NO SUPEREN EL PROMEDIO DE VELOCIDAD.
            11. TODOS LOS PERSONAJES CUYO PODER NO SUPERE EL PODER DE PERSONAJES LA RAZA SAIYAN.
            12. TODOS LOS PERSONAJES DEL GENERO NO-BINARIO QUE POSEEN LA VELOCIDAD MAS ALTA.
            13. PROMEDIO DE INTELIGENCIA Y PODER DE LOS PERSONAJES DE LA RAZA ANDROID.
            14. PERSONAJES QUE NO SON DE LA RAZA KRIPTONIAN QUE NO SUPERAN O IGUALAN EL PROMEDIO DE PODER DE LA RAZA KRIPTONIA.
            15. INFO DE LOS PERSONAJES QUE NO SEAN SAIYAN CUYO STATS ESTE POR DEBAJO DEL INDICE DE ATAQUE SAIYAN.
            16. MATRIZ ORDENADA SEGUN INTELIGENCIA EN ORDEN DES.
            17. MATRIZ ORDENADA SEGUN INTELIGENCIA EN ORDEN ASC DE PERSONAJES DE RAZA NO HUMAN.
            18. MATRIZ ORDENADA SEGUN PODER EN ORDEN DES DE PERSONAJES DE RAZA NO HUMAN.
            19. MATRIZ ORDENADA SEGUN VELOCIDAD EN ORDEN ASC.
            20. ORDEN PERSONALIZADO:    -PERSONAJES AGRUPADOS POR RAZA.
                                        -LOS PERSONAJES DE CADA RAZA ORDENADOS SEGUN PODER DE MANERA DES.
                                        -LAS RAZAS DEBEN ESTAR DE FORMA ALFABERTICA.
            21. MATRIZ TRASPUESTA, MOSTRANDO SU INFO ORDENADA POR RAZA DE MANERA ASC.
            22. SALIR.
        """
    
    print(menu_opciones)


def mostrar_cantidad_personajes(matriz: list[list]) -> None:
    """
    Muestra en la consola la cantidad de personajes que hay en una matriz. Si la matriz está vacía, informa al usuario. 
    De lo contrario, imprime el número total de personajes.

    :param: matriz: La matriz (lista de listas) que contiene los datos de los personajes.
    :returns: La función no devuelve ningún valor, solo imprime un mensaje en la consola.
    """
    cantidad_personajes = len(matriz)

    if cantidad_personajes <= 0:
        print('LA MATRIZ ESTA VACÍA.')
    else:
        print(f'LA CANTIDAD DE PERSONAJES QUE HAY EN EL SET DE DATOS ES: {cantidad_personajes}.')

#4.Existencias personajes Human: Mostrar la cantidad de personajes que sean raza Human o en caso de que tengan una raza 
# compuesta, tengan Human en su raza

def mostrar_existencias(matriz: list[list], tipo_raza: str) -> None:
    """
    Muestra en la consola la cantidad de personajes de una raza específica.
    Esta función busca personajes cuya raza coincide exactamente con el valor de búsqueda o que lo contengan si hay
    palabras compuestas.
    :param: matriz: La matriz que contiene los datos de los personajes.
            tipo_raza: La raza que se desea buscar.
    :returns: La función no devuelve ningún valor, solo imprime el resultado.
    """
    cantidad = 0
    tipo_raza = tipo_raza.lower()

    for personaje in matriz:
        raza_personaje = str(personaje[2]).lower()
        palabra_raza_limpia = raza_personaje.replace('-', ' ').replace('/', ' ')
        if raza_personaje == tipo_raza or tipo_raza in palabra_raza_limpia.split(): 
            cantidad += 1

    print(f'LA CANTIDAD DE PERONAJES {tipo_raza} O QUE CONTENGAN {tipo_raza} SON: {cantidad}.')
    return cantidad

#5. Existencias personajes que no sean Human: Mostrar la cantidad de personajes cuya raza no sea Human o no tenga Human 
# como parte de su raza compuesta
def mostrar_resto_existencias(matriz: list[list], cantidad_raza: int) -> None:
    """
    Calcula y muestra la cantidad de personajes que no pertenecen a una raza específica, basándose en el total de la
    matriz y la cantidad de personajes de la raza buscada.
    :param: matriz: La matriz (lista de listas) que contiene los datos de todos los personajes.
            cantidad_raza: La cantidad de personajes que no pertenecen a la raza que se está buscando.
    :returns: La función no devuelve un valor, solo imprime el resultado.
    """
    resto_cantidad_existencias = len(matriz) - cantidad_raza

    print(f'LA CANTIDAD DE PERSONAJES NO HUMAN O QUE NO CONTENGAN HUMAN SON: {resto_cantidad_existencias}.')

#6. Mostrar Detalle: Recorrer la matriz y mostrar la info de todos los personajes truncando los strings a 15 caracteres 
# como máximo. (con una función que acepte ese tipo de matriz) con formato:nombre,alias,raza,género,inteligencia,poder,
# velocidad


def mostrar_detalle(matriz: list[list]) -> None:
    """
    Muestra la información de todos los personajes en la matriz con formato de informe. Se asegura que la matriz no este 
    vacía, en ese caso imprime un mensaje en consola.
    La función recorre la matriz y, para cada personaje, extrae sus datos y los formatea en un informe detallado. 
    Los campos de texto (nombre, alias, raza, género) se truncan a un máximo de 15 caracteres para asegurar un formato 
    consistente.
    :params: matriz: Una matriz (lista de listas) que contiene los datos de los personajes.
    :returns: La función no devuelve un valor. Solo imprime el informe de cada personaje en la consola.
    """
    if not matriz:
        print('LA MATRIZ ESTA VACIA. NO HAY PERSONAJES PARA MOSTRAR.')
        return
    else:
        print('****** INFORME DE PERSONAJE ******')
        print('----------------------------------')
        for personaje in matriz:
            nombre = personaje[0][:15]
            alias = personaje[1][:15]
            raza = personaje[2][:15]
            genero = personaje[3][:15]
            inteligencia = personaje[4]
            poder = personaje[5]
            velocidad = personaje[6]

            print(f'{nombre}, {alias}, {raza}, {genero}, {inteligencia}, {poder}, {velocidad}')

#7. Mostrar Saiyan: Recorrer la matriz y mostrar la info (con una función que acepte ese tipo de matriz) con formato: 
# nombre,alias,raza,género,inteligencia,poder,velocidad solamente de los personajes cuya raza sea Saiyan

def mostrar_personajes(lista_personajes: list) -> None:
    """
    Muestra la información de una lista de personajes en un formato de una línea.
    :param: lista_personajes: Una lista de personajes a mostrar.
    :returns: La función no devuelve un valor, solo imprime el resultado.
    """
    if not lista_personajes:
        print("NO SE ENCONTRARON PERSONAJES QUE CUMPLAN CON EL CRITERIO.")
        return
    
    for personaje in lista_personajes:
        nombre = personaje[0]
        alias = personaje[1]
        raza = personaje[2]
        genero = personaje[3]
        inteligencia = personaje[4]
        poder = personaje[5]
        velocidad = personaje[6]
        
        print(f'{nombre}, {alias}, {raza}, {genero}, {inteligencia}, {poder}, {velocidad}')


#8.Mostrar más poderoso:Determinar cuál o cuáles son los personajes con más poder y mostrar sus datos, junto con la 
# cantidad que poseen
#9.Mostrar más inteligente: Determinar cuál o cuáles son los personajes más inteligentes y mostrar sus datos, junto con 
# la cantidad que poseen

def mostrar_personajes_filtrados(lista_filtrada: list, indice_columna, tipo_filtro: str) -> None:
    """
    Muestra los datos de los personajes que tienen el valor máximo en una columna específica.
    La función recorre una lista de personajes y, para cada uno, imprime su nombre, alias y el valor máximo de la columna 
    indicada.
    :param: lista_maximos: Una lista de listas que contiene a los personajes con el valor máximo.
            indice_columna: El índice de la columna que representa la característica a mostrar.
    :returns: La función no devuelve ningún valor, solo imprime el resultado.
    """
    if indice_columna == 4:
        nombre_valor = 'PODER'
    elif indice_columna == 5:
        nombre_valor = 'INTELIGENCIA'
    elif indice_columna == 6:
        nombre_valor = 'VELOCIDAD'

    print(f'LOS PERSONAJES CON EL {tipo_filtro} DE {nombre_valor} SON: ')
    print('------------------------------------------')
    for personaje in lista_filtrada:
        nombre = personaje[0]
        alias = personaje[1]
        valor_maximo = personaje[indice_columna]

        print(f'{nombre}, {alias}, {valor_maximo}')





