
def mostrar_menu_principal():
    """
    Muestra en la consola un menú de opciones para la gestión de un set de datos
    de personajes. El menú está diseñado para que el usuario pueda seleccionar
    diferentes acciones como crear, agregar, consultar, filtrar, ordenar y salir.
    El formato del menú está predefinido en una cadena de texto.
    :returns:
        None: La función no retorna ningún valor, simplemente imprime el menú en la consola.
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