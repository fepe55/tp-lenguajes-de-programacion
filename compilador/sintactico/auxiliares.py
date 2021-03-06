# -*- encoding: utf-8 -*-

comienzo_de_proposicion = [ 
    '_call', '_begin', '_if', '_while', '_writeln',
    '_write', '_readln', 
]

# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def constante (scanner,errores,semantico,base,desplazamiento):
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is not "identificador":
        errores.error_sintactico(errores.SE_ESPERABA_IDENTIFICADOR,S,cadena,numero_de_linea)
        return desplazamiento

    nombre_constante = cadena

    (S,cadena,numero_de_linea) = scanner.leer(errores)
    if S is not "igual":
        errores.error_sintactico(errores.SE_ESPERABA_IGUAL,S,cadena,numero_de_linea)
        return desplazamiento

    (S,cadena,numero_de_linea) = scanner.leer(errores)
    if S is not "numero":
        errores.error_sintactico(errores.SE_ESPERABA_NUMERO,S,cadena,numero_de_linea)
        valor = 0
        #return desplazamiento
    else :
        valor = cadena
        (S,cadena,numero_de_linea) = scanner.leer(errores)

    semantico.cargar (base,desplazamiento,nombre_constante,"_const",valor,errores,numero_de_linea)
    desplazamiento += 1

    if S is not "puntoycoma":
        if S is "coma":
            (S,cadena,numero_de_linea) = scanner.leer(errores)
            desplazamiento = constante(scanner,errores,semantico,base,desplazamiento)
            return desplazamiento
        else:
            errores.error_sintactico(errores.SE_ESPERABA_COMA_PUNTOYCOMA,S,cadena,numero_de_linea)
            return desplazamiento

    (S,cadena,numero_de_linea) = scanner.leer(errores)
    return desplazamiento


# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def variable(scanner,errores,semantico,base,desplazamiento):

    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is not "identificador":
        errores.error_sintactico(errores.SE_ESPERABA_IDENTIFICADOR,S,cadena,numero_de_linea)
    else:
        semantico.cargar (base,desplazamiento,cadena,"_var",0,errores,numero_de_linea)
        desplazamiento += 1

    (S,cadena,numero_de_linea) = scanner.leer(errores)
    if S is not "puntoycoma":
        if S is "coma":
            (S,cadena,numero_de_linea) = scanner.leer(errores)
            desplazamiento = variable(scanner,errores,semantico,base,desplazamiento)
            return desplazamiento
        else:
            errores.error_sintactico(errores.SE_ESPERABA_COMA_PUNTOYCOMA,S,cadena,numero_de_linea)
            #Manejo de errores. Si S es un identificador no declarado, inserción de coma
            if S is "identificador":
                (codigo,valor) = semantico.validar_sin_errores(base,desplazamiento,cadena,("_var",))
                if codigo == -2 or codigo == -1:
                    desplazamiento = variable(scanner,errores,semantico,base,desplazamiento)
                    return desplazamiento

            scanner.panico(errores) 

    (S,cadena,numero_de_linea) = scanner.leer(errores)
    return desplazamiento


# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def procedimiento(scanner,errores,semantico,base,desplazamiento):
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is not "identificador":
        errores.error_sintactico(errores.SE_ESPERABA_IDENTIFICADOR,S,cadena,numero_de_linea)
        return desplazamiento
    nombre_procedimiento = cadena

    (S,cadena,numero_de_linea) = scanner.leer(errores)
    if S is not "puntoycoma":
        errores.error_sintactico(errores.SE_ESPERABA_PUNTOYCOMA,S,cadena,numero_de_linea)
    # Manejo de errores, si no es puntoycoma, inserción
    else:
        (S,cadena,numero_de_linea) = scanner.leer(errores)

    semantico.cargar (base,desplazamiento,nombre_procedimiento,"_procedure",0,errores,numero_de_linea)
    desplazamiento += 1

    bloque(scanner,errores,semantico,base+desplazamiento) 

    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is not "puntoycoma":
        errores.error_sintactico(errores.SE_ESPERABA_PUNTOYCOMA,S,cadena,numero_de_linea)
        return desplazamiento

    (S,cadena,numero_de_linea) = scanner.leer(errores)
    return desplazamiento


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
def condicion(scanner,semantico,base,desplazamiento,errores):
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is "_odd":
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        expresion(scanner,semantico,base,desplazamiento,errores)
        return

    #No es ODD, debe ser una expresión 
    expresion(scanner,semantico,base,desplazamiento,errores)
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if es_operador_relacional(S):
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        expresion(scanner,semantico,base,desplazamiento,errores)
        return
    else:
        errores.error_sintactico(errores.SE_ESPERABA_OPERADOR_RELACIONAL,S,cadena,numero_de_linea)
        #Manejo de errores, asumo error. Sustitución por operador relacional
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        expresion(scanner,semantico,base,desplazamiento,errores)
        return


# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def expresion(scanner,semantico,base,desplazamiento,errores):
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is "suma" or S is "resta":
        (S,cadena,numero_de_linea) = scanner.leer(errores)

    termino(scanner,semantico,base,desplazamiento,errores)
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()

    while S is "suma" or S is "resta":
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        termino(scanner,semantico,base,desplazamiento,errores)
        (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()

    return


# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def termino(scanner,semantico,base,desplazamiento,errores):

    factor(scanner,semantico,base,desplazamiento,errores)
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is "multiplicacion" or S is "division" :
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        termino(scanner,semantico,base,desplazamiento,errores)
        return

    return


# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def factor(scanner,semantico,base,desplazamiento,errores):
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is "identificador":
        semantico.validar(base,desplazamiento,cadena,("_var","_const"),errores,numero_de_linea) 
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        return

    if S is "numero":
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        return

    if S is "parentesisapertura":
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        expresion(scanner,semantico,base,desplazamiento,errores)
        (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
        if S is not "parentesiscierre":
            errores.error_sintactico(errores.SE_ESPERABA_PARENTESISCIERRE,S,cadena,numero_de_linea)
            return
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        return

    # No entró por ningún IF
    errores.error_sintactico(errores.SE_ESPERABA_IDENTIFICADOR_NUMERO_PARENTESISAPERTURA,S,cadena,numero_de_linea)
    return


# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def readln(scanner,semantico,base,desplazamiento,errores):
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is not "parentesisapertura":
       errores.error_sintactico(errores.SE_ESPERABA_PARENTESISAPERTURA,S,cadena,numero_de_linea) 
        #Manejo de errores, si no es paréntesis de apertura, inserción.
    else:
        (S,cadena,numero_de_linea) = scanner.leer(errores)

    if S is not "identificador":
       errores.error_sintactico(errores.SE_ESPERABA_IDENTIFICADOR,S,cadena,numero_de_linea) 
       scanner.panico(errores)
       return

    (S,cadena,numero_de_linea) = scanner.leer(errores)
    while S is "coma" :
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        if S is not "identificador":
            errores.error_sintactico(errores.SE_ESPERABA_IDENTIFICADOR,S,cadena,numero_de_linea)
            return
        semantico.validar(base,desplazamiento,cadena,("_var",),errores,numero_de_linea)
        (S,cadena,numero_de_linea) = scanner.leer(errores)

    if S is not "parentesiscierre":
        errores.error_sintactico(errores.SE_ESPERABA_PARENTESISCIERRE,S,cadena,numero_de_linea)
        #Manejo de errores, si no es paréntesis de cierre, inserción.
    else:
        (S,cadena,numero_de_linea) = scanner.leer(errores)

    return


# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def writeaux(scanner,semantico,base,desplazamiento,errores):
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is not "literal":
        #Manejo de errores
        if S is '_nulo' and cadena is '_panico':
            scanner.panico(errores)
            return
        else:
            expresion(scanner,semantico,base,desplazamiento,errores)
            (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    else:
        #Como es literal, leo uno más, que no tuve que leer en el caso de expresión
        (S,cadena,numero_de_linea) = scanner.leer(errores)

    while S is "coma":
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        if S is not "literal":
            #Manejo de errores
            if S is '_nulo' and cadena is '_panico':
                scanner.panico(errores)
                return
            else:
                expresion(scanner,semantico,base,desplazamiento,errores)
                (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
        else:
            #Como es literal, leo uno más, que no tuve que leer en el caso de expresión
            (S,cadena,numero_de_linea) = scanner.leer(errores)

    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    # Cuando dejaron de aparecer comas, pregunto por el paréntesis de cierre
    if S is not "parentesiscierre":
        errores.error_sintactico(errores.SE_ESPERABA_COMA_PARENTESISCIERRE,S,cadena,numero_de_linea)
        return

    (S,cadena,numero_de_linea) = scanner.leer(errores)
    return

# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def write(scanner,semantico,base,desplazamiento,errores):
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is not "parentesisapertura":
       errores.error_sintactico(errores.SE_ESPERABA_PARENTESISAPERTURA,S,cadena,numero_de_linea) 
    else :
        # Es paréntesis de apertura, llamo a writeaux
        (S,cadena,numero_de_linea) = scanner.leer(errores)
    writeaux(scanner,semantico,base,desplazamiento,errores)
    return


# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def writeln(scanner,semantico,base,desplazamiento,errores):
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is not "parentesisapertura":
        return

    # Es paréntesis de apertura, llamo a writeaux
    (S,cadena,numero_de_linea) = scanner.leer(errores)
    writeaux(scanner,semantico,base,desplazamiento,errores)
    return

# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def proposicion(scanner,semantico,base,desplazamiento,errores):

    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()

    if S is "identificador":
        (codigo,valor) = semantico.validar(base,desplazamiento,cadena,("_var",),errores,numero_de_linea) 
        if codigo == -1:
            tipo = valor
            if tipo is "_procedure":
                # Faltó el call, el error lo tiró el semántico
                (S,cadena,numero_de_linea) = scanner.leer(errores)
                return
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        if S is "asignacion":
            (S,cadena,numero_de_linea) = scanner.leer(errores)
            expresion(scanner,semantico,base,desplazamiento,errores)
        else:
            errores.error_sintactico(errores.SE_ESPERABA_ASIGNACION,S,cadena,numero_de_linea)
            # Si bien siempre reporto el error, si en vez de la asignación es un igual
            # sigo procesando, por sustitución
            if S is "igual":
                (S,cadena,numero_de_linea) = scanner.leer(errores)
                expresion(scanner,semantico,base,desplazamiento,errores)
            else:
                scanner.panico(errores)
            return

        return

    if S is "_call":
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        if S is not "identificador":
            errores.error_sintactico(errores.SE_ESPERABA_IDENTIFICADOR,S,cadena,numero_de_linea)
            return
        semantico.validar(base,desplazamiento,cadena,("_procedure",),errores,numero_de_linea) 

        #Leo para cumplir la poscondición
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        return

    if S is "_begin":
        (S,cadena,numero_de_linea) = scanner.leer(errores)

        proposicion(scanner,semantico,base,desplazamiento,errores)
        (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()

        Saux = None
        if S is not "puntoycoma" and S is not "_end":
            errores.error_sintactico(errores.SE_ESPERABA_END_PUNTOYCOMA,S,cadena,numero_de_linea)
            if S in comienzo_de_proposicion:
                Saux = S
                S = "puntoycoma"
            else:
                scanner.panico(errores)
                proposicion(scanner,semantico,base,desplazamiento,errores)
                (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()

        while S is "puntoycoma":
            if Saux:
                S = Saux
            else:
                (S,cadena,numero_de_linea) = scanner.leer(errores)
            proposicion(scanner,semantico,base,desplazamiento,errores)
            Saux = None
            (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
            if S is not "puntoycoma" and S is not "_end":
                errores.error_sintactico(errores.SE_ESPERABA_END_PUNTOYCOMA,S,cadena,numero_de_linea)
                if S in comienzo_de_proposicion:
                    Saux = S
                    S = "puntoycoma"

        # Salgo del ciclo de proposiciones, debe ser END
        if S is not "_end":
            errores.error_sintactico(errores.SE_ESPERABA_END_PUNTOYCOMA,S,cadena,numero_de_linea)
            scanner.panico(errores) #mmm, acá ya salí, no me gusta, debería hacerlo antes
            return
        #Leo para cumplir la poscondición
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        return

    if S is "_if":
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        condicion(scanner,semantico,base,desplazamiento,errores)
        (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
        if S is "_then":
            (S,cadena,numero_de_linea) = scanner.leer(errores)
            proposicion(scanner,semantico,base,desplazamiento,errores)
            (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
        else:
            errores.error_sintactico(errores.SE_ESPERABA_THEN,S,cadena,numero_de_linea)
            return
        return

    if S is "_while":
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        condicion(scanner,semantico,base,desplazamiento,errores)
        (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
        if S is "_do":
            (S,cadena,numero_de_linea) = scanner.leer(errores)
            proposicion(scanner,semantico,base,desplazamiento,errores)
        else:
            errores.error_sintactico(errores.SE_ESPERABA_DO,S,cadena,numero_de_linea)
            #Manejo de errores, si en vez de "_do" es "_then", supongo error. Sustitución.
            if S is "_then":
                (S,cadena,numero_de_linea) = scanner.leer(errores)
                proposicion(scanner,semantico,base,desplazamiento,errores)
            else:
                scanner.panico(errores)

            return

        return

    if S is "_writeln":
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        writeln(scanner,semantico,base,desplazamiento,errores)
        return

    if S is "_write":
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        write(scanner,semantico,base,desplazamiento,errores)
        return

    if S is "_readln":
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        readln(scanner,semantico,base,desplazamiento,errores)
        return

    #Proposición vacía, retorno con una lectura más hecha
    return


# Precondición: Entro con una lectura hecha en el parser
# Poscondición: Devuelvo una lectura más.
def bloque (scanner,errores,semantico,base):
    desplazamiento = 0
    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()
    if S is "_const":
        # Hay declaración de constantes
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        desplazamiento = constante(scanner,errores,semantico,base,desplazamiento)
        (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()

    if S is "_var":
        # Hay declaración de variables
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        desplazamiento = variable(scanner,errores,semantico,base,desplazamiento)
        (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()

    while S is "_procedure":
        # Hay declaración de procedimientos
        (S,cadena,numero_de_linea) = scanner.leer(errores)
        desplazamiento = procedimiento(scanner,errores,semantico,base,desplazamiento)
        (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()

    proposicion(scanner,semantico,base,desplazamiento,errores)

    return
