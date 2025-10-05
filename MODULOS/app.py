import os
import mostrar_datos, validaciones, funciones_standar
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

    corriendo = True
    matriz_personajes = None

    while corriendo:

        mostrar_datos.mostrar_menu_principal()

        opcion = validaciones.validar_int_entre_rangos('Ingrese un valor entre 1 - 22: ', 1, 22)

        match opcion:
            case 1:
                matriz_personajes = funciones_standar.crear_matriz(nombres,alias, razas, 
                                                                    generos, poderes, 
                                                                    inteligencias, velocidades)
                print('La matriz ha sido creada correctamente.')
            case 2:
                funciones_standar.agregar_personaje(matriz_personajes)
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
                mostrar_datos.mostrar_saiyan(matriz_personajes)
            case 8:
                mostrar_datos.procesar_personaje_maximo(matriz_personajes, 4)
            case 9:
                mostrar_datos.procesar_personaje_maximo(matriz_personajes, 5)
            case 10:
                pass
            case 11:
                pass
            case 12:
                pass
            case 13:
                pass
            case 14:
                pass
            case 15:
                pass
            case 16:
                pass
            case 17:
                pass
            case 18:
                pass
            case 19:
                pass
            case 20:
                pass
            case 21:
                pass
            case 22:
                corriendo = False

        os.system('pause')
        os.system('cls')

