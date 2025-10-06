#def formatear_personaje(personaje: list) -> list:
#    """
#    Extrae los datos de un personaje de una lista y trunca los strings a 15 caracteres.
#    :param: personaje: Una lista con los datos del personaje.
#    :returns: Una nueva lista con los strings truncados.
#    """
#    nombre = personaje[0][:15]
#    alias = personaje[1][:15]
#    raza = personaje[2][:15]
#    genero = personaje[3][:15]
#    inteligencia = personaje[4]
#    poder = personaje[5]
#    velocidad = personaje[6]
#    
#    return [nombre, alias, raza, genero, inteligencia, poder, velocidad]


#def validar_genero(texto):
#    """
#    Solicita al usuario el género de un personaje y lo valida.
#    Esta función se asegurarse de que el género ingresado sea 'masculino' o 'no-binario'. Si el valor no es válido, 
#    muestra un error y vuelve a solicitar la entrada de forma recursiva hasta que sea correcta.
#    :param: texto: Un mensaje de tipo string que se muestra al usuario para solicitar el género.
#    :returns: str: La cadena de texto validada que corresponde a un género.
#    """
#    genero = validar_str(texto)
#    if genero == 'masculino' or genero == 'no-binario':
#        return genero
#    else: 
#        print('ERROR. El género ingresado no es válido. Intente nuevamente.')
#        return validar_genero(texto)
    
#def validar_raza(texto):
#    """
#    Solicita al usuario una raza de personaje y la valida. Si la raza no es válida, muestra un error y vuelve a solicitar 
#    la entrada hasta que sea correcta.
#    :param: texto: El mensaje que se le muestra al usuario para solicitar la raza del personaje.
#    :returns: La cadena de texto validada que corresponde a una raza.
#    """
#    raza = validar_str(texto)
#    if (raza == 'human' or raza == 'desconocido' or raza == 'vampire' or raza == 'god / eternal' or raza == 'saiyan' or 
#        raza == 'human / radiation' or raza == 'mutant' or raza == 'new god' or raza == 'demon' or raza == 'alpha' or
#        raza == 'kryptonian' or raza == 'human / clone' or raza == 'eternal' or raza == 'agardian' or raza == 'demi-god' or
#        raza == 'czarnian' or raza == 'inhuman' or raza == 'human-kree' or raza == 'android'or raza == 'animal' or 
#        raza == 'human / altered'):
#        return raza
#    else: 
#        print('ERROR. El raza ingresada no es válida. Intente nuevamente.')
#        return validar_raza(texto)
