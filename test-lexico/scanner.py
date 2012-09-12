# -*- encoding: utf-8 -*-

import lexico

def scanner (fuente, listado, terminal, S, cad, restante, numero_de_linea):
    if restante is "EOF":
        S = "_FIN"
        return (listado,S,cad,restante,numero_de_linea) 
    else:
        if not restante:
            numero_de_linea+=1
            restante = fuente.leer_linea_sin_nl()
            listado.escribir("\n")
            listado.escribir(str(numero_de_linea)+': '+restante)
            (S,cad,restante) = lexico.obtener_simbolo (restante,numero_de_linea)
        else:
            (S,cad,restante) = lexico.obtener_simbolo (restante,numero_de_linea)

        return (listado,S,cad,restante,numero_de_linea)

