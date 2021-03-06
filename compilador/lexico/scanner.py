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


    def leer (self,errores):
        if self.restante is "EOF":
            self.S = "_FIN"
            self.cad = ""
            if errores:
                errores.error_lexico(errores.FIN_INESPERADO_PROGRAMA,self.numero_de_linea)
            return (self.S, self.cad, self.numero_de_linea)
        else:
            if not self.restante:
                while not self.restante:
                    self.numero_de_linea+=1
                    #self.listado.escribir("\n")
                    self.restante = self.fuente.leer_linea_sin_nl()

                self.listado.escribir("\n")
                self.listado.escribir(str(self.numero_de_linea)+': '+self.restante)
                #(self.S,self.cad,self.restante) = \
                #    auxiliares.obtener_simbolo(self.restante, self.numero_de_linea)
                (self.S,self.cad,self.numero_de_linea) = self.leer(errores)
            else:
                (self.S,self.cad,self.restante) = \
                  auxiliares.obtener_simbolo(self.restante,self.numero_de_linea,errores)

            #self.debug_imprimir()
            return (self.S, self.cad, self.numero_de_linea)


    # Precondición: Entro con una lectura hecha en el parser
    # Poscondición: Devuelvo una lectura más.
    def panico (self,errores):
        simbolos_de_sincronizacion = [
            'puntoycoma','_end','_call','_begin','_if',
            '_while', '_writeln', '_write', '_readln', '_FIN',
        ]
        (S,cadena,numero_de_linea) = self.obtener_sin_leer()
        while S not in simbolos_de_sincronizacion:
            (S,cadena,numero_de_linea) = self.leer(None)

        return


    def debug_imprimir(self):
        print self.numero_de_linea
        print "cad:",self.cad
        print "S:",self.S
        print
