# -*- encoding: utf-8 -*-

from compilador.utils import errores

# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def constante (scanner):
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is not "identificador":
        errores.error_sintactico(errores.SE_ESPERABA_IDENTIFICADOR,numero_de_linea)
        return

    (S,cadena,numero_de_linea) = scanner.leer()
    if S is not "igual":
        errores.error_sintactico(errores.SE_ESPERABA_IGUAL,numero_de_linea)
        return

    (S,cadena,numero_de_linea) = scanner.leer()
    if S is not "numero":
        errores.error_sintactico(errores.SE_ESPERABA_NUMERO,numero_de_linea)
        return

    (S,cadena,numero_de_linea) = scanner.leer()
    if S is not "puntoycoma":
        if S is "coma":
            (S,cadena,numero_de_linea) = scanner.leer()
            constante(scanner)
            return
        else:
            errores.error_sintactico(errores.SE_ESPERABA_COMA_PUNTOYCOMA,numero_de_linea)
            return

    (S,cadena,numero_de_linea) = scanner.leer()
    return


# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def variable(scanner):
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is not "identificador":
        errores.error_sintactico(errores.SE_ESPERABA_IDENTIFICADOR,numero_de_linea)
        return

    (S,cadena,numero_de_linea) = scanner.leer()
    if S is not "puntoycoma":
        if S is "coma":
            (S,cadena,numero_de_linea) = scanner.leer()
            variable(scanner)
            return
        else:
            errores.error_sintactico(errores.SE_ESPERABA_COMA_PUNTOYCOMA,numero_de_linea)
            return

    (S,cadena,numero_de_linea) = scanner.leer()
    return


# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def procedimiento(scanner):
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is not "identificador":
        errores.error_sintactico(errores.SE_ESPERABA_IDENTIFICADOR,numero_de_linea)
        return

    (S,cadena,numero_de_linea) = scanner.leer()
    if S is not "puntoycoma":
        errores.error_sintactico(errores.SE_ESPERABA_PUNTOYCOMA,numero_de_linea)
        return

    (S,cadena,numero_de_linea) = scanner.leer()
    bloque(scanner) 

    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is not "puntoycoma":
        errores.error_sintactico(errores.SE_ESPERABA_PUNTOYCOMA,numero_de_linea)
        return

    (S,cadena,numero_de_linea) = scanner.leer()
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
def condicion(scanner):
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is "_odd":
        (S,cadena,numero_de_linea) = scanner.leer()
        expresion(scanner)
        return

    #No es ODD, debe ser una expresión 
    expresion(scanner)
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if es_operador_relacional(S):
        (S,cadena,numero_de_linea) = scanner.leer()
        expresion(scanner)
        return
    else:
        errores.error_sintactico(errores.SE_ESPERABA_OPERADOR_RELACIONAL)
        return


# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def expresion(scanner):
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is "suma" or S is "resta":
        (S,cadena,numero_de_linea) = scanner.leer()

    termino(scanner)
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()

    while S is "suma" or S is "resta":
        (S,cadena,numero_de_linea) = scanner.leer()
        termino(scanner)
        (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()

    return


# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def termino(scanner):

    factor(scanner)
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is "multiplicacion" or S is "division" :
        (S,cadena,numero_de_linea) = scanner.leer()
        termino(scanner)
        return

    return


# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def factor(scanner):
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is "identificador":
        (S,cadena,numero_de_linea) = scanner.leer()
        return
  
    if S is "numero":
        (S,cadena,numero_de_linea) = scanner.leer()
        return

    if S is "parentesisapertura":
        (S,cadena,numero_de_linea) = scanner.leer()
        expresion(scanner)
        (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
        if S is not "parentesiscierre":
            errores.error_sintactico(errores.SE_ESPERABA_PARENTESISCIERRE,numero_de_linea)
            return
        (S,cadena,numero_de_linea) = scanner.leer()
        return

    # No entró por ningún IF
    errores.error_sintactico(errores.SE_ESPERABA_IDENTIFICADOR_NUMERO_PARENTESISAPERTURA,numero_de_linea)
    return


# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def readln(scanner):
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is not "parentesisapertura":
       errores.error_sintactico(errores.SE_ESPERABA_PARENTESISAPERTURA,numero_de_linea) 
       return

    (S,cadena,numero_de_linea) = scanner.leer()
    if S is not "identificador":
       errores.error_sintactico(errores.SE_ESPERABA_IDENTIFICADOR,numero_de_linea) 
       return

    (S,cadena,numero_de_linea) = scanner.leer()
    while S is "coma" :
        (S,cadena,numero_de_linea) = scanner.leer()
        if S is not "identificador":
            errores.error_sintactico(errores.SE_ESPERABA_IDENTIFICADOR,numero_de_linea)
            return
        (S,cadena,numero_de_linea) = scanner.leer()

    if S is not "parentesiscierre":
        errores.error_sintactico(errores.SE_ESPERABA_PARENTESISCIERRE,numero_de_linea)
        return

    (S,cadena,numero_de_linea) = scanner.leer()
    return


# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def writeaux(scanner):
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is not "literal":
        expresion(scanner)
    else:
        #Como es literal, leo uno más, que no tuve que leer en el caso de expresión
        (S,cadena,numero_de_linea) = scanner.leer()

    while S is "coma" :
        (S,cadena,numero_de_linea) = scanner.leer()
        if S is not "literal":
            expresion(scanner)
        else:
            #Como es literal, leo uno más, que no tuve que leer en el caso de expresión
            (S,cadena,numero_de_linea) = scanner.leer()

    # Cuando dejaron de aparecer comas, pregunto por el paréntesis de cierre
    if S is not "parentesiscierre":
        errores.error_sintactico(errores.SE_ESPERABA_COMA_PARENTESISCIERRE,numero_de_linea)
        return

    (S,cadena,numero_de_linea) = scanner.leer()
    return

# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def write(scanner):
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is not "parentesisapertura":
       errores.error_sintactico(errores.SE_ESPERABA_PARENTESISAPERTURA,numero_de_linea) 
       return
    
    # Es paréntesis de apertura, llamo a writeaux
    (S,cadena,numero_de_linea) = scanner.leer()
    writeaux(scanner)
    return


# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def writeln(scanner):
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is not "parentesisapertura":
        return

    # Es paréntesis de apertura, llamo a writeaux
    (S,cadena,numero_de_linea) = scanner.leer()
    writeaux(scanner)
    return    

# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def proposicion(scanner):

    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()

    if S is "identificador":
        (S,cadena,numero_de_linea) = scanner.leer()
        if S is "asignacion":
            (S,cadena,numero_de_linea) = scanner.leer()
            expresion(scanner)
        else:
            errores.error_sintactico(errores.SE_ESPERABA_ASIGNACION,numero_de_linea)
            return

        return

    if S is "_call":
        (S,cadena,numero_de_linea) = scanner.leer()
        if S is not "identificador":
            errores.error_sintactico(errores.SE_ESPERABA_IDENTIFICADOR,numero_de_linea)
            return
        #Leo para cumplir la poscondición
        (S,cadena,numero_de_linea) = scanner.leer()
        return

    if S is "_begin":
        (S,cadena,numero_de_linea) = scanner.leer()

        proposicion(scanner)
        (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()

        while S is "puntoycoma":
            (S,cadena,numero_de_linea) = scanner.leer()
            proposicion(scanner)
            (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()

        # Salgo del ciclo de proposiciones, debe ser END
        if S is not "_end":
            errores.error_sintactico(errores.SE_ESPERABA_END_PUNTOYCOMA,numero_de_linea)
            return
        #Leo para cumplir la poscondición
        (S,cadena,numero_de_linea) = scanner.leer()
        return

    if S is "_if":
        (S,cadena,numero_de_linea) = scanner.leer()
        condicion(scanner)
        (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
        if S is "_then":
            (S,cadena,numero_de_linea) = scanner.leer()
            proposicion(scanner)
            (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
        else:
            errores.error_sintactico(errores.SE_ESPERABA_THEN,numero_de_linea)
            return
        return

    if S is "_while":
        (S,cadena,numero_de_linea) = scanner.leer()
        condicion(scanner)
        (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
        if S is "_do":
            (S,cadena,numero_de_linea) = scanner.leer()
            proposicion(scanner)
        else:
            errores.error_sintactico(errores.SE_ESPERABA_DO,numero_de_linea)
            return

        return

    if S is "_writeln":
        (S,cadena,numero_de_linea) = scanner.leer()
        writeln(scanner)
        return

    if S is "_write": 
        (S,cadena,numero_de_linea) = scanner.leer()
        write(scanner)
        return

    if S is "_readln": 
        (S,cadena,numero_de_linea) = scanner.leer()
        readln(scanner)
        return

    #Proposición vacía, retorno con una lectura más hecha
    return


# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def bloque (scanner):
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is "_const":
        # Hay declaración de constantes
        (S,cadena,numero_de_linea) = scanner.leer()
        constante(scanner)
        (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()

    if S is "_var":
        # Hay declaración de variables
        (S,cadena,numero_de_linea) = scanner.leer()
        variable(scanner)
        (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()

    while S is "_procedure":
        # Hay declaración de procedimientos
        (S,cadena,numero_de_linea) = scanner.leer()
        procedimiento(scanner)
        (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()

    proposicion(scanner)

    return
