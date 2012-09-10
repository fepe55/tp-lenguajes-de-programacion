# -*- encoding: utf-8 -*-
import parser

def scanner (fuente, listado, terminal, S, cad, restante, numero_de_linea):
    if restante is "EOF":
        S = "_FIN"
        return (listado,S,cad,restante,numero_de_linea) 
    else:
        if not restante:
            numero_de_linea+=1
            S = '_FINLINEA'
        else:
            (S,cad,restante) = parser.parser (restante)

        return (listado,S,cad,restante,numero_de_linea)

