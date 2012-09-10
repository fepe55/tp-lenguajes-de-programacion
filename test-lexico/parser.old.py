# -*- encoding: utf-8 -*-
import string

terminal = [
    '_nulo','_begin','_end',
    '_call','_const','_var',
    '_while','_odd','_then',
    '_procedure','_if','_do',
    'menoroigual','mayoroigual',
    'distinto','asignacion',
    'menor','igual','mayor',
    'punto','coma','puntoycoma',
    'parentesisapertura','suma',
    'parentesiscierre','resta',
    'multiplicacion','division',
    'identificador','numero',
]

# palabras reservadas (11)
# begin, end, call, const, var, while, do, if, then, procedure, odd

# símbolos de dos caracteres (4)
# '<=', '>=', '<>', ':='

# símbolos de un caracter (12)
# '<', '>', '=', ',', '.', ';', '(', ')', '+', '-', '*', '/' 

# no entran en ninguna categoría
# identificador, numero, nulo

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


def old_main():
    for linea in f:
        print linea,
        nueva_linea=''
        while linea:
            (elemento,linea) = parser.scanner(linea)
            elemento = parser.parser(elemento)
            if elemento != 'espacio':
                print elemento,
        print 
        numero_de_linea+=1
    f.close()

