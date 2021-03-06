#!/usr/bin/python

# -*- encoding: utf-8 -*-

from compilador.utils.gestor_de_archivos import GestorDeArchivos
from compilador.sintactico.parser import parser
import sys

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

    parser(fuente,listado)

    listado.cerrar()
    fuente.cerrar()

if __name__ == '__main__':
    main()

