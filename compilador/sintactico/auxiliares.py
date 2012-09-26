# -*- encoding: utf-8 -*-

#from compilador.utils import errores

# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def constante (scanner,errores):
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is not "identificador":
        errores.error_sintactico(errores.SE_ESPERABA_IDENTIFICADOR,numero_de_linea)
        return

    (S,cadena,numero_de_linea) = scanner.leer(errores)
    if S is not "igual":
        errores.error_sintactico(errores.SE_ESPERABA_IGUAL,numero_de_linea)
        return

    (S,cadena,numero_de_linea) = scanner.leer(errores)
    if S is not "numero":
        errores.error_sintactico(errores.SE_ESPERABA_NUMERO,numero_de_linea)
        return

    (S,cadena,numero_de_linea) = scanner.leer(errores)
    if S is not "puntoycoma":
        if S is "coma":
            (S,cadena,numero_de_linea) = scanner.leer(errores)
            constante(scanner,errores)
            return
        else:
            errores.error_sintactico(errores.SE_ESPERABA_COMA_PUNTOYCOMA,numero_de_linea)
            return

    (S,cadena,numero_de_linea) = scanner.leer(errores)
    return


# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def variable(scanner,errores):
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is not "identificador":
        errores.error_sintactico(errores.SE_ESPERABA_IDENTIFICADOR,numero_de_linea)
        return

    (S,cadena,numero_de_linea) = scanner.leer(errores)
    if S is not "puntoycoma":
        if S is "coma":
            (S,cadena,numero_de_linea) = scanner.leer(errores)
            variable(scanner,errores)
            return
        else:
            errores.error_sintactico(errores.SE_ESPERABA_COMA_PUNTOYCOMA,numero_de_linea)
            return

    (S,cadena,numero_de_linea) = scanner.leer(errores)
    return


# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def procedimiento(scanner,errores):
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is not "identificador":
        errores.error_sintactico(errores.SE_ESPERABA_IDENTIFICADOR,numero_de_linea)
        return

    (S,cadena,numero_de_linea) = scanner.leer(errores)
    if S is not "puntoycoma":
        errores.error_sintactico(errores.SE_ESPERABA_PUNTOYCOMA,numero_de_linea)
        return

    (S,cadena,numero_de_linea) = scanner.leer(errores)
    bloque(scanner,errores) 

    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is not "puntoycoma":
        errores.error_sintactico(errores.SE_ESPERABA_PUNTOYCOMA,numero_de_linea)
        return

    (S,cadena,numero_de_linea) = scanner.leer(errores)
    return


def es_operador_relacional(S):
    if S is "igual":
        return True
    if S is "distinto":
        return True
    if S is "menor":
        return True
    if S is "mayor":
        return True
    if S is "menoroigual":
        return True
    if S is "mayoroigual":
        return True
    return False

# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def condicion(scanner,errores):
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is "_odd":
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        expresion(scanner,errores)
        return

    #No es ODD, debe ser una expresión 
    expresion(scanner,errores)
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if es_operador_relacional(S):
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        expresion(scanner,errores)
        return
    else:
        errores.error_sintactico(errores.SE_ESPERABA_OPERADOR_RELACIONAL)
        return


# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def expresion(scanner,errores):
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is "suma" or S is "resta":
        (S,cadena,numero_de_linea) = scanner.leer(errores)

    termino(scanner,errores)
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()

    while S is "suma" or S is "resta":
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        termino(scanner,errores)
        (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()

    return


# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def termino(scanner,errores):

    factor(scanner,errores)
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is "multiplicacion" or S is "division" :
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        termino(scanner,errores)
        return

    return


# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def factor(scanner,errores):
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is "identificador":
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        return
  
    if S is "numero":
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        return

    if S is "parentesisapertura":
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        expresion(scanner,errores)
        (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
        if S is not "parentesiscierre":
            errores.error_sintactico(errores.SE_ESPERABA_PARENTESISCIERRE,numero_de_linea)
            return
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        return

    # No entró por ningún IF
    errores.error_sintactico(errores.SE_ESPERABA_IDENTIFICADOR_NUMERO_PARENTESISAPERTURA,numero_de_linea)
    return


# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def readln(scanner,errores):
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is not "parentesisapertura":
       errores.error_sintactico(errores.SE_ESPERABA_PARENTESISAPERTURA,numero_de_linea) 
       return

    (S,cadena,numero_de_linea) = scanner.leer(errores)
    if S is not "identificador":
       errores.error_sintactico(errores.SE_ESPERABA_IDENTIFICADOR,numero_de_linea) 
       return

    (S,cadena,numero_de_linea) = scanner.leer(errores)
    while S is "coma" :
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        if S is not "identificador":
            errores.error_sintactico(errores.SE_ESPERABA_IDENTIFICADOR,numero_de_linea)
            return
        (S,cadena,numero_de_linea) = scanner.leer(errores)

    if S is not "parentesiscierre":
        errores.error_sintactico(errores.SE_ESPERABA_PARENTESISCIERRE,numero_de_linea)
        return

    (S,cadena,numero_de_linea) = scanner.leer(errores)
    return


# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def writeaux(scanner,errores):
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is not "literal":
        expresion(scanner,errores)
    else:
        #Como es literal, leo uno más, que no tuve que leer en el caso de expresión
        (S,cadena,numero_de_linea) = scanner.leer(errores)

    while S is "coma" :
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        if S is not "literal":
            expresion(scanner,errores)
        else:
            #Como es literal, leo uno más, que no tuve que leer en el caso de expresión
            (S,cadena,numero_de_linea) = scanner.leer(errores)

    # Cuando dejaron de aparecer comas, pregunto por el paréntesis de cierre
    if S is not "parentesiscierre":
        errores.error_sintactico(errores.SE_ESPERABA_COMA_PARENTESISCIERRE,numero_de_linea)
        return

    (S,cadena,numero_de_linea) = scanner.leer(errores)
    return

# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def write(scanner,errores):
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is not "parentesisapertura":
       errores.error_sintactico(errores.SE_ESPERABA_PARENTESISAPERTURA,numero_de_linea) 
       return
    
    # Es paréntesis de apertura, llamo a writeaux
    (S,cadena,numero_de_linea) = scanner.leer(errores)
    writeaux(scanner,errores)
    return


# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def writeln(scanner,errores):
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is not "parentesisapertura":
        return

    # Es paréntesis de apertura, llamo a writeaux
    (S,cadena,numero_de_linea) = scanner.leer(errores)
    writeaux(scanner,errores)
    return    

# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def proposicion(scanner,errores):

    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()

    if S is "identificador":
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        if S is "asignacion":
            (S,cadena,numero_de_linea) = scanner.leer(errores)
            expresion(scanner,errores)
        else:
            errores.error_sintactico(errores.SE_ESPERABA_ASIGNACION,numero_de_linea)
            return

        return

    if S is "_call":
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        if S is not "identificador":
            errores.error_sintactico(errores.SE_ESPERABA_IDENTIFICADOR,numero_de_linea)
            return
        #Leo para cumplir la poscondición
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        return

    if S is "_begin":
        (S,cadena,numero_de_linea) = scanner.leer(errores)

        proposicion(scanner,errores)
        (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()

        while S is "puntoycoma":
            (S,cadena,numero_de_linea) = scanner.leer(errores)
            proposicion(scanner,errores)
            (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()

        # Salgo del ciclo de proposiciones, debe ser END
        if S is not "_end":
            errores.error_sintactico(errores.SE_ESPERABA_END_PUNTOYCOMA,numero_de_linea)
            return
        #Leo para cumplir la poscondición
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        return

    if S is "_if":
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        condicion(scanner,errores)
        (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
        if S is "_then":
            (S,cadena,numero_de_linea) = scanner.leer(errores)
            proposicion(scanner,errores)
            (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
        else:
            errores.error_sintactico(errores.SE_ESPERABA_THEN,numero_de_linea)
            return
        return

    if S is "_while":
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        condicion(scanner,errores)
        (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
        if S is "_do":
            (S,cadena,numero_de_linea) = scanner.leer(errores)
            proposicion(scanner,errores)
        else:
            errores.error_sintactico(errores.SE_ESPERABA_DO,numero_de_linea)
            return

        return

    if S is "_writeln":
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        writeln(scanner,errores)
        return

    if S is "_write": 
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        write(scanner,errores)
        return

    if S is "_readln": 
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        readln(scanner,errores)
        return

    #Proposición vacía, retorno con una lectura más hecha
    return


# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def bloque (scanner,errores):
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is "_const":
        # Hay declaración de constantes
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        constante(scanner,errores)
        (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()

    if S is "_var":
        # Hay declaración de variables
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        variable(scanner,errores)
        (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()

    while S is "_procedure":
        # Hay declaración de procedimientos
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        procedimiento(scanner,errores)
        (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()

    proposicion(scanner,errores)

    return
