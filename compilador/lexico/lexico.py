# -*- encoding: utf-8 -*-

MAXIMO_TAMANIO_IDENTIFICADOR = 25

from compilador.utils import errores

terminos = {
    'const'     : '_const',
    'var'       : '_var',
    'begin'     : '_begin',
    'end'       : '_end',
    'call'      : '_call',
    'procedure' : '_procedure',
    'while'     : '_while',
    'odd'       : '_odd',
    'then'      : '_then',
    'if'        : '_if',
    'do'        : '_do',
    'odd'       : '_odd',
    'write'     : '_write',
    'writeln'   : '_writeln',
    'readln'    : '_readln',
    'eof'       : '_FIN',
    '<='        : 'menoroigual',
    '>='        : 'mayoroigual',
    '<>'        : 'distinto',
    ':='        : 'asignacion',
    '<'         : 'menor',
    '>'         : 'mayor',
    '='         : 'igual',
    '.'         : 'punto',
    ','         : 'coma',
    ';'         : 'puntoycoma',
    '('         : 'parentesisapertura',
    ')'         : 'parentesiscierre',
    '+'         : 'suma',
    '-'         : 'resta',
    '*'         : 'multiplicacion',
    '/'         : 'division',
}

def longitud_correcta(cadena):
    return len(cadena) < MAXIMO_TAMANIO_IDENTIFICADOR

def numero_longitud_correcta(numero):
    return longitud_correcta(str(numero))

def palabra_reservada(palabra):
    palabras_reservadas = ['begin', 'end', 'call', 'const', 'var', 
        'while', 'do', 'if', 'then', 'procedure', 'odd', 'eof',
    ]
 
    if palabra.lower() in palabras_reservadas:
        return terminos[palabra.lower()]
    else :
        return 'identificador'

def obtener_simbolo (linea,numero_de_linea):

    simbolos_de_un_caracter_unicos = ['=',',','.',';','(',')','+','-','*','/']

    caracter = linea[0] 
    cad = ""

    while caracter is ' ':
        linea = linea[1:]
        caracter = linea[0]

    if caracter in simbolos_de_un_caracter_unicos:
        cad = caracter
        S = terminos[caracter]
        restante = linea[1:]
        return (S,cad,restante)

    if caracter is ':':
        try:
            c = linea[1]
        except IndexError:
            cad = caracter
            S = '_nulo'
            restante = linea[1:]
            errores.error_lexico(errores.SE_ESPERABA_IGUAL,numero_de_linea)
        else:
            if c == '=':
                cad = linea[:2]
                S = terminos[cad]
                restante = linea[2:]
            else:
                cad = caracter 
                S = '_nulo'
                restante = linea[1:]
                errores.error_lexico(errores.SE_ESPERABA_IGUAL,numero_de_linea)

        return (S,cad,restante)

    if caracter is '>':
        try:
            c = linea[1]
        except IndexError:
            cad = caracter
            S = terminos[cad]
            restante = linea[1:]
        else:
            if c is '=':
                cad = linea[:2]
                S = terminos[cad]
                restante = linea[2:]
            else:
                cad = caracter
                S = terminos[cad]
                restante = linea[1:]

        return (S,cad,restante)

    if caracter is '<':
        try:
            c = linea[1]
        except IndexError:
            cad = caracter
            S = terminos[cad]
            restante = linea[1:]
        else:
            if c is '=':
                cad = linea[:2]
                S = terminos[cad]
                restante = linea[2:]
            else :
                if c is '>':
                    cad = linea[:2]
                    S = terminos[cad]
                    restante = linea[2:]
                else :
                    cad = caracter
                    S = terminos[cad]
                    restante = linea[1:]
        return (S,cad,restante)

    #Literal
    if caracter == '\'':
        restante = linea
        cad = '\''
        restante = restante[1:]
        caracter = linea[1]
        while caracter is not '\'':
            try:
                cad += caracter
                restante = restante[1:]
                caracter = restante[0]
            except IndexError:
                errores.error_lexico(errores.FIN_INESPERADO_LITERAL,numero_de_linea)
                break
        cad = cad + '\''
        if longitud_correcta(cad):
            S = '_literal'
        else:
            errores.error_lexico(errores.LITERAL_DEMASIADO_LARGO,numero_de_linea)
            S = '_nulo'
        return (S,cad,restante)

    #Número
    if caracter.isdigit():
        restante = linea
        while caracter.isdigit():
            try:
                #Agrego el número a la cadena
                cad += caracter
                #Y lo quito del restante
                restante=restante[1:]
                #Leo de nuevo
                caracter = restante[0]
            except IndexError:
                break
        if numero_longitud_correcta(cad):
            S = 'numero'
        else:
            errores.error_lexico(errores.ENTERO_DEMASIADO_LARGO,numero_de_linea)
            S = '_nulo'
        return (S,cad,restante)

    #Identificador o palabra clave
    if caracter.isalpha():
        restante = linea
        while caracter.isalnum():
            try:
                cad += caracter
                restante=restante[1:]
                caracter = restante[0]
            except IndexError:
                break
        if longitud_correcta(cad):
            S = palabra_reservada(cad)
        else:
            errores.error_lexico(errores.IDENTIFICADOR_DEMASIADO_LARGO,numero_de_linea)
            S = '_nulo'
        return (S,cad,restante)

    # Si no entró en ningún otro if, es nulo
    cad = caracter
    restante = linea[1:]
    S = '_nulo'
    return (S,cad,restante)

