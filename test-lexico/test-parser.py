#!/usr/bin/python
# -*- encoding: utf-8 -*-

import parser
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

def main():
    numero_de_linea = 1
    f = open('test.txt', 'rU')
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

# 0- Inicializo el número de linea en 1
# 1- Mientras no se acaba el archivo, leo una linea
# 2- Leo hasta que haya un caracter no normal y lo guardo en car
# 3- Si car es muy largo, rompo todo
# 4- Paso car al parser, que me devuelve el elemento
# 5- Voy armando la nueva linea
# 6- Devuelvo la nueva linea
# 7- Incremento el número de linea

if __name__ == '__main__':
    main()
