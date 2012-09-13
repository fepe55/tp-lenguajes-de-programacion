# -*- encoding: utf-8 -*-

from compilador.lexico.scanner import Scanner
from compilador.sintactico import auxiliares
from compilador.utils import errores

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
    '_writeln','_write','_readln',
]

def parser (fuente,listado):

    restante = fuente.leer_linea_sin_nl()

    scanner = Scanner(fuente,listado,terminal)

    auxiliares.bloque (scanner)

    (S,cadena,numero_de_linea) = scanner.leer()

    if S is not "punto":
        errores.error_sintactico(errores.SE_ESPERABA_PUNTO,numero_de_linea)

