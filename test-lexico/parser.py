# -*- encoding: utf-8 -*-

terminos = {
    'const' : '_const',
    'var' : '_var',
    'begin' : '_begin',
    'end' : '_end',
    'call': '_call',
    'procedure' : '_procedure',
    'while' : '_while',
    'odd' : '_odd',
    'then': '_then',
    'if': '_if',
    'do': '_do',
    'odd' :'_odd',
    '<=':'menoroigual',
    '>=':'mayoroigual',
    '<>' : 'distinto',
    ':=' : 'asignacion',
    '<' : 'menor',
    '>' : 'mayor',
    '=' : 'igual',
    '.' : 'punto',
    ',' : 'coma',
    ';' : 'puntoycoma',
    '(' : 'parentesisapertura',
    ')' : 'parentesiscierre',
    '+' : 'suma',
    '-' : 'resta',
    '*' : 'multiplicacion',
    '/' : 'division',
}


def entra_en_32_bits(elemento):
    return True

def palabra_reservada(palabra):
    palabras_reservadas = ['begin', 'end', 'call', 'const', 'var', 
        'while', 'do', 'if', 'then', 'procedure', 'odd',
    ]
 
    if palabra.lower() in palabras_reservadas:
        return terminos[palabra.lower()]
    else :
        return 'identificador'

def parser (linea):

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
        if entra_en_32_bits(cad):
            S = 'numero'
        else:
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
        if entra_en_32_bits(cad):
            S = palabra_reservada(cad)
        else:
            S = '_nulo'
        return (S,cad,restante)

    # Si no entró en ningún otro if, es nulo
    cad = caracter
    restante = linea[1:]
    S = '_nulo'
    return (S,cad,restante)

