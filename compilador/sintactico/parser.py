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
]

def parser (fuente,listado):

    cad = ""
    S = ""

    restante = fuente.leer_linea_sin_nl()
    numero_de_linea = 1
    listado.escribir(str(numero_de_linea)+': '+restante)

    scanner = Scanner(fuente,listado,terminal,S,cad,restante,numero_de_linea)

    auxiliares.bloque (scanner)

    # (listado,S,cad,restante,numero_de_linea) = \
    #     scanner(fuente, listado, terminal, S, cad, restante, numero_de_linea)
    # 
    # if S is not "punto":
    #     errores.error_sintactico(errores.SE_ESPERA_PUNTO,numero_de_linea)

