# -*- encoding: utf-8 -*-
import string

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


def leer (archivo):
    f = open(archivo)
    c = f.read(1)
    if c :
        return c
    else:
        return 'EOF'

def parser (elemento):

    if entra_en_32_bits(elemento):
        if elemento.lower() in terminos:
            return terminos[elemento.lower()]
        if elemento.isdigit():
            return 'numero'
        if elemento.isalpha():
            return 'identificador'
        if elemento.isspace():
            return 'espacio'
    return '_nulo'

def scanner (linea):

    palabras_reservadas = ['begin', 'end', 'call', 'const', 'var', 
    'while', 'do', 'if', 'then', 'procedure', 'odd']
    simbolos_dos_caracteres = ['<=','>=','<>',':=' ]
    simbolos_un_caracter = ['>','<','=',',','.',';','(',')','+','-','*','/' ]

    if linea[:2] in simbolos_dos_caracteres:
        return (linea[:2],linea[2:])
    if linea[0] in simbolos_un_caracter:
        return (linea[0],linea[1:])
    
    index = 0
    char = linea[index]

    if char.isalpha():
        while char.isalnum():
            index += 1
            char = linea[index]
        return (linea[:index],linea[index:])

    if char.isdigit():
        while char.isdigit():
            index += 1
            char = linea[index]
        return (linea[:index],linea[index:])

    if char.isspace():
        return (char,linea[1:])

    print ('toastie!')

    return ('','')
