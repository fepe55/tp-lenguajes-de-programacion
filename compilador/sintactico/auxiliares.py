# -*- encoding: utf-8 -*-

from compilador.utils import errores

def constante (scanner):
    (S,cadena,numero_de_linea) = scanner.leer()
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
            constante(scanner)
        else:
            errores.error_sintactico(errores.SE_ESPERABA_COMA_PUNTOYCOMA,numero_de_linea)
    return


def variable(scanner):
    (S,cadena,numero_de_linea) = scanner.leer()
    if S is not "identificador":
        errores.error_sintactico(errores.SE_ESPERABA_IDENTIFICADOR,numero_de_linea)
        return

    (S,cadena,numero_de_linea) = scanner.leer()
    if S is not "puntoycoma":
        if S is "coma":
            variable(scanner)
        else:
            errores.error_sintactico(errores.SE_ESPERABA_COMA_PUNTOYCOMA,numero_de_linea)
    return


def procedimiento(scanner):
    (S,cadena,numero_de_linea) = scanner.leer()
    if S is not "identificador":
        errores.error_sintactico(errores.SE_ESPERABA_IDENTIFICADOR,numero_de_linea)
        return

    (S,cadena,numero_de_linea) = scanner.leer()
    if S is not "puntoycoma":
        errores.error_sintactico(errores.SE_ESPERABA_PUNTOYCOMA,numero_de_linea)
 
    bloque(scanner) 

    (S,cadena,numero_de_linea) = scanner.leer()
    if S is not "puntoycoma":
        errores.error_sintactico(errores.SE_ESPERABA_PUNTOYCOMA,numero_de_linea)

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

def condicion(scanner):
    (S,cadena,numero_de_linea) = scanner.leer()
    if S is "_odd":
        expresion(scanner)
        return

    #No es ODD, debe ser una expresión 
    expresion(scanner)
    (S,cadena,numero_de_linea) = scanner.leer()
    if es_operador_relacional(S):
       expresion(scanner)
    else:
        errores.error_sintactico(errores.SE_ESPERABA_OPERADOR_RELACIONAL)

    return


def expresion(scanner):
    return True


def termino(scanner):
    return True


def factor(scanner):
    (S,cadena,numero_de_linea) = scanner.leer()
    if S is "identificador":
        return
  
    if S is "numero":
        return

    if S is "parentesisapertura":
        expresion(scanner)
        (S,cadena,numero_de_linea) = scanner.leer()
        if S is not "parentesiscierre":
            errores.error_sintactico(errores.SE_ESPERABA_PARENTESISCIERRE,numero_de_linea)
        return

    # No entró por ningún IF
    errores.error_sintactico(errores.SE_ESPERABA_IDENTIFICADOR_NUMERO_PARENTESISAPERTURA)
    return


def readln(scanner):
    return True


def write(scanner):
    return True


def writeln(scanner):
    return True


def proposicion(scanner):
    (S,cadena,numero_de_linea) = scanner.leer()
    if S is "identificador":
        (S,cadena,numero_de_linea) = scanner.leer()
        if S is "asignacion":
            expresion()
        else:
            errores.error_sintactico(errores.SE_ESPERABA_ASIGNACION,numero_de_linea)

        return

    if S is "_call":
        (S,cadena,numero_de_linea) = scanner.leer()
        if S is not "identificador":
            errores.error_sintactico(errores.SE_ESPERABA_IDENTIFICADOR,numero_de_linea)
        return

    if S is "_begin":
        while S is not "_end":
            proposicion(scanner)
            (S,cadena,numero_de_linea) = scanner.leer()
            if S is not "puntoycoma":
                errores.error_sintactico(errores.SE_ESPERABA_PUNTOYCOMA,numero_de_linea)
            (S,cadena,numero_de_linea) = scanner.leer()
            if S is "_FIN":
                errores.error_sintactico(errores.SE_ESPERABA_END_PUNTOYCOMA,numero_de_linea)
                break
        return

    if S is "_if":
        condicion(scanner)
        (S,cadena,numero_de_linea) = scanner.leer()
        if S is "_then":
            proposicion(scanner)
        else:
            errores.error_sintactico(errores.SE_ESPERABA_THEN,numero_de_linea)
        return

    if S is "_while":
        condicion(scanner)
        (S,cadena,numero_de_linea) = scanner.leer()
        if S is "_do":
            proposicion(scanner)
        else:
            errores.error_sintactico(errores.SE_ESPERABA_DO,numero_de_linea)
        return

    if S is "_writeln":
        #TODO

    if S is "_write":
        #TODO

    if S is "_readln":
        #TODO


    #Proposición vacía
    return
           

def bloque (scanner):

    (S,cadena,numero_de_linea) = scanner.leer()
    if S is "_const":
        # Hay declaración de constantes
        constante(scanner)
        (S,cadena,numero_de_linea) = scanner.leer()
 
    if S is "_var":
        # Hay declaración de variables
        variable(scanner)
        (S,cadena,numero_de_linea) = scanner.leer()
 
    while S is "_procedure":
        # Hay declaración de procedimientos
        procedimiento(scanner)
        (S,cadena,numero_de_linea) = scanner.leer()

    proposicion(scanner)

    return
