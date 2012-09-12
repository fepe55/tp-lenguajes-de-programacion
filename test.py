#!/usr/bin/python

# -*- encoding: utf-8 -*-

from compilador.utils.gestor_de_archivos import GestorDeArchivos
from compilador.lexico import scanner
import sys

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
    if len(sys.argv) < 2 :
        sys.exit("Uso: "+sys.argv[0]+" <nombre_de_archivo>")
    else:
        nombre_fuente = sys.argv[1]
    
    fuente = GestorDeArchivos(nombre_fuente)

    if not fuente.abrir_lectura():
        sys.exit("Error al tratar de abrir el archivo "+nombre_fuente)

    listado = GestorDeArchivos("res/listado.txt")

    if not listado.abrir_escritura():
        fuente.cerrar()
        sys.exit("Error horrible, horrible")

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
