# -*- encoding: utf-8 -*-

from compilador.lexico import auxiliares

class Scanner:
    def __init__ (self,fuente,listado,terminal,S,cad,restante,numero_de_linea):
        self.fuente = fuente
        self.listado = listado
        self.terminal = terminal
        self.S = S
        self.cad = cad
        self.restante = restante
        self.numero_de_linea = numero_de_linea

    def leer (self):
        if self.restante is "EOF":
            self.S = "_FIN"
            return self.S
        else:
            if not self.restante:
                self.numero_de_linea+=1
                self.restante = self.fuente.leer_linea_sin_nl()
                if self.restante:
                    self.listado.escribir("\n")
                    self.listado.escribir(str(self.numero_de_linea)+': '+self.restante)
                    (self.S,self.cad,self.restante) = \
                        auxiliares.obtener_simbolo(self.restante, self.numero_de_linea)
            else:
                (self.S,self.cad,self.restante) = \
                  auxiliares.obtener_simbolo(self.restante,self.numero_de_linea)

            return self.S

