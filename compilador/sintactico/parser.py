# -*- encoding: utf-8 -*-

from compilador.lexico.scanner import Scanner
from compilador.sintactico import auxiliares
from compilador.utils.errores import GestorDeErrores

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
    'literal', '_FIN'
]

def parser (fuente,listado):

    errores = GestorDeErrores()
    scanner = Scanner(fuente,listado,terminal)

    scanner.leer(errores)

    auxiliares.bloque (scanner,errores,0)

    (S,cadena,numero_de_linea) = scanner.obtener_sin_leer()

    if S is not "punto":
        errores.error_sintactico(errores.SE_ESPERABA_PUNTO,S,cadena,numero_de_linea)

    errores.resumen()
