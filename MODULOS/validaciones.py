
def validar_str(texto: str) -> str:
    """
    Solicita al usuario una cadena de texto y la valida de forma recursiva.
    Esta función se asegura de que el valor ingresado por el usuario sea una cadena que contenga solo caracteres 
    alfabéticos. Si el valor es inválido, llama a la misma función de nuevo para solicitar el input hasta que sea correcto.
    :param: texto: Un mensaje de tipo string que se muestra al usuario para solicitar la entrada.
    :returns: Una cadena de texto que ha sido validada y contiene solo caracteres alfabéticos.
    """
    input_usuario = input(texto)
    if input_usuario.isalpha():
        return input_usuario
    else:
        print('El dato ingresado por el usuario no es valido. Intente nuevamente.')
        return validar_str(texto)


def validar_int(texto: str) -> int:
    """
    Solicita al usuario un número y lo valida de forma recursiva. Esta función se asegura de que el valor ingresado por 
    el usuario sea una cadena que solo contenga dígitos. Si el valor es inválido, llama a la misma función de nuevo para 
    solicitar el input hasta que sea correcto.
    :param: texto: Un mensaje de tipo string que se muestra al usuario para solicitar la entrada.
    :returns: Un número entero que ha sido validado como un número.
    """
    input_usuario = input(texto)
    if input_usuario.isdigit():
        input_usuario = int(input_usuario)
        return input_usuario
    else:
        print('ERROR. El dato ingresado no es un número. Vuelva a intentarlo.')
        return validar_int(texto)



def validar_int_entre_rangos(texto: str, minimo: int, maximo: int) -> int:
    """
    Solicita un número al usuario y lo valida de forma recursiva, asegurándose de que sea un número entero y que se 
    encuentre dentro de un rango específico.
    Esta función reutiliza la función 'validar_input' para manejar la validación de que el dato ingresado sea un número.
    :param:
        texto: Un mensaje de tipo string que se muestra al usuario para solicitar la entrada.
        minimo: Un número entero, que representa el valor mínimo permitido en el rango de validación.
        maximo: Un número entero, que representa el valor máximo permitido en el rango de validación.
    :Returns:
        Un número entero que ha sido validado para ser un número y para estar dentro del rango.
    """
    input_usuario = validar_int(texto)

    if minimo <= input_usuario <= maximo:
        return input_usuario
    else:
        print(f'ERROR. El numero {input_usuario} está fuera del rango [{minimo} - {maximo}]. Vuelva a intentarlo.')
        return validar_int_entre_rangos(texto, minimo, maximo)

