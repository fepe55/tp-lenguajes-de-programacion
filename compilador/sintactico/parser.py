# -*- encoding: utf-8 -*-

from compilador.lexico.scanner import scanner
from compilador.sintactico import auxiliares

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

def parser (fuente,listado):

    cad = ""
    S = ""

    restante = fuente.leer_linea_sin_nl()
    numero_de_linea = 1
    listado.escribir(str(numero_de_linea)+': '+restante)

    while S is not "punto" :
        (listado,S,cad,restante,numero_de_linea) = \
            scanner(fuente, listado, terminal, S, cad, restante, numero_de_linea)

#        if S is "_const":
#            helpers.const(



