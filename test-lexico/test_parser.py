#!/usr/bin/python

# -*- encoding: utf-8 -*-

from gestor_de_archivos import GestorDeArchivos
import scanner

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

def main():
    fuente = GestorDeArchivos("res/test.txt")
    listado = GestorDeArchivos("res/listado.txt")
    fuente.abrir_lectura()
    listado.abrir_escritura()

    cad = ""
    S = ""

    restante = fuente.leer_linea_sin_nl()
    numero_de_linea = 1
    listado.escribir(str(numero_de_linea)+': '+restante)

    while S is not "_FIN" :
        (listado,S,cad,restante,numero_de_linea) = \
            scanner.scanner(fuente, listado, terminal, S, cad, restante, numero_de_linea)

    listado.cerrar()
    fuente.cerrar()

if __name__ == '__main__':
    main()
