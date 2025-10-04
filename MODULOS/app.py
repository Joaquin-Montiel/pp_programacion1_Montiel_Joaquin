import mostrar_datos, validaciones
import os


def gestionar_app_personajes() -> None:

    corriendo = True

    while corriendo:

        mostrar_datos.mostrar_menu_principal()

        opcion = validaciones.validar_int_entre_rangos('Ingrese un valor entre 1 - 22: ', 1, 22)

        match opcion:
            case 1:
                print('Hola mundo')
            case 1:
                pass
            case 1:
                pass
            case 1:
                pass
            case 1:
                pass
            case 1:
                pass
            case 1:
                pass
            case 1:
                pass
            case 1:
                pass
            case 1:
                pass
            case 1:
                pass
            case 1:
                pass
            case 1:
                pass
            case 1:
                pass
            case 1:
                pass
            case 1:
                pass
            case 1:
                pass
            case 1:
                pass
            case 1:
                pass
            case 1:
                pass
            case 1:
                pass
            case 22:
                corriendo = False

        os.system('pause')
        os.system('cls')

