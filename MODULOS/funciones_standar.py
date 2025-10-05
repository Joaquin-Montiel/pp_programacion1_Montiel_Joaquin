import validaciones

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
