# -*- encoding: utf-8 -*-

from compilador.lexico import auxiliares

class Scanner:
    def __init__ (self,fuente,listado,terminal):
        self.fuente = fuente
        self.listado = listado
        self.terminal = terminal
        self.S = ''
        self.cad = ''
        self.numero_de_linea = 1
        self.restante = fuente.leer_linea_sin_nl() 
        self.listado.escribir(str(self.numero_de_linea)+': '+self.restante) 


    def obtener_sin_leer(self):
        return (self.S, self.cad, self.numero_de_linea)


    def leer (self):
        if self.restante is "EOF":
            self.S = "_FIN"
            self.cad = ""
            return (self.S, self.cad, self.numero_de_linea)
        else:
            if not self.restante:
                self.numero_de_linea+=1
                self.restante = self.fuente.leer_linea_sin_nl()
                if self.restante:
                    self.listado.escribir("\n")
                    self.listado.escribir(str(self.numero_de_linea)+': '+self.restante)
                    #(self.S,self.cad,self.restante) = \
                    #    auxiliares.obtener_simbolo(self.restante, self.numero_de_linea)
                    (self.S,self.cad,self.numero_de_linea) = self.leer()
            else:
                (self.S,self.cad,self.restante) = \
                  auxiliares.obtener_simbolo(self.restante,self.numero_de_linea)

            #self.debugimprimir()
            return (self.S, self.cad, self.numero_de_linea)


    def debugimprimir(self):
        print self.numero_de_linea
        print "cad:",self.cad
        print "S:",self.S
        print

