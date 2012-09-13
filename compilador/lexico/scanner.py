# -*- encoding: utf-8 -*-

from compilador.lexico import auxiliares

def scanner (fuente, listado, terminal, S, cad, restante, numero_de_linea):
    if restante is "EOF":
        S = "_FIN"
        return (listado,S,cad,restante,numero_de_linea)
    else:
        if not restante:
            numero_de_linea+=1
            restante = fuente.leer_linea_sin_nl()
            if restante:
                listado.escribir("\n")
                listado.escribir(str(numero_de_linea)+': '+restante)
                (S,cad,restante) = auxiliares.obtener_simbolo(restante,numero_de_linea)
        else:
            (S,cad,restante) = auxiliares.obtener_simbolo(restante,numero_de_linea)

        return (listado,S,cad,restante,numero_de_linea)

