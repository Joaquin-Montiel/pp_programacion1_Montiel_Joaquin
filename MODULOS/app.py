import os
import mostrar_datos, validaciones, utilidades, filtros, ordenamiento
from utn_fra.datasets import (
        lista_nombre_heroes_pp as nombres, 
        lista_alias_pp as alias,
    	lista_razas_pp as razas, 
        lista_generos_pp as generos,
    	lista_poderes_pp as poderes, 
        lista_inteligencias_pp as inteligencias,
        lista_velocidades_pp as velocidades
)



def gestionar_app_personajes() -> None:
    """
    Función principal de la aplicación.
    Controla el flujo del programa mediante un menú interactivo. Inicializa la aplicación, maneja la creación y el estado 
    de la matriz de personajes, y llama a las funciones específicas de los módulos (utilidades, mostrar_datos, 
    ordenamiento) para ejecutar las diferentes opciones solicitadas por el usuario.
    El bucle principal sigue esta estructura:
    1. Muestra el menú de opciones.
    2. Valida la entrada del usuario.
    3. Usa una sentencia 'match' para ejecutar la acción correspondiente.
    4. Maneja la persistencia del menú hasta que el usuario selecciona la opción de salida (22).

    :returns: La función no devuelve un valor, solo maneja la lógica y la interfaz de la aplicación.
    """

    corriendo = True
    matriz_personajes = None

    while corriendo:

        mostrar_datos.mostrar_menu_principal()

        opcion = validaciones.validar_int_entre_rangos('Ingrese un valor entre 1 - 22: ', 1, 22)

        match opcion:
            case 1:
                matriz_personajes = utilidades.crear_matriz(nombres, alias, razas, 
                                                            generos, poderes, 
                                                            inteligencias, velocidades)
                print('La matriz ha sido creada correctamente.')
            case 2:
                utilidades.agregar_personaje(matriz_personajes)
                print(matriz_personajes)
            case 3:
                if matriz_personajes == None:
                    print("Error: La matriz no ha sido creada. Por favor, seleccione la opción 1 primero.")
                else:
                    mostrar_datos.mostrar_cantidad_personajes(matriz_personajes)
            case 4:
                cantidad_raza_human = mostrar_datos.mostrar_existencias(matriz_personajes, 'Human')
            case 5:
                mostrar_datos.mostrar_resto_existencias(matriz_personajes, cantidad_raza_human)
            case 6:
                mostrar_datos.mostrar_detalle(matriz_personajes)
            case 7:
                utilidades.procesar_saiyanes(matriz_personajes)
            case 8:
                utilidades.procesar_personaje_maximo(matriz_personajes, 4, 'maximo')
            case 9:
                utilidades.procesar_personaje_maximo(matriz_personajes, 5, 'maximo')
            case 10:
                utilidades.procesar_personajes_por_pormedio(matriz_personajes, 6, 'minimo')
            case 11:
                utilidades.procesar_personajes_debiles(matriz_personajes, 'Saiyan')
            case 12:
                utilidades.procesar_no_binario(matriz_personajes, 'No-Binario')
            case 13:
                utilidades.procesar_android_por_promedio(matriz_personajes, 'Android')
            case 14:
                utilidades.obtener_filtro_kryptonian(matriz_personajes)
            case 15:
                utilidades.obtener_personajes_debajo_indice_ataque(matriz_personajes)
            case 16:
                matriz_ordenada_inteligencia = ordenamiento.ordenar_selection_sort(matriz_personajes, 5)
                mostrar_datos.mostrar_personajes_filtrados(matriz_ordenada_inteligencia, 5, 'maximo')
            case 17:
                utilidades.manejar_ordenamiento_filtro_inteligencia_no_human(matriz_personajes)
            case 18:
                utilidades.manejar_ordenamiento_filtro_poder_no_human(matriz_personajes)
            case 19:
                matriz_ordenada_velocidad = ordenamiento.ordenar_selection_sort(matriz_personajes, 6, 'ASC')
                mostrar_datos.mostrar_personajes_filtrados(matriz_ordenada_velocidad, 6, 'menos')
            case 20:
                utilidades.manejar_ordenamiento_personalizado(matriz_personajes)
            case 21:
                utilidades.procesar_ordenamiento_matriz_transpuesta(matriz_personajes)
            case 22:
                corriendo = False

        os.system('pause')
        os.system('cls')

