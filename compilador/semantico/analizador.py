# -*- encoding: utf-8 -*- 

CANT_MAX_IDENT = 128
SIZE_OF_INT = 4

class AnalizadorSemantico:
    def __init__ (self):
        self.tabla = [None]*(CANT_MAX_IDENT-1)
        self.cant_variables = 0

    def cargar (self,posicion,nombre,tipo,valor,errores):
        if posicion < CANT_MAX_IDENT:
            elemento = {
                "nombre" : nombre,
                "tipo" : tipo,
            }

            if tipo is "_const":
                elemento ['valor'] = valor

            if tipo is "_var":
                elemento ['valor'] = self.cant_variables*SIZE_OF_INT
                self.cant_variables += 1

            if tipo is "_procedure":
                elemento ['valor'] = 0

            self.tabla[posicion] = elemento

        #else:
            # Error semántico
            # error_semantico(

        return

    def debug_imprimir_tabla (self):
        print "posicion","\t","tipo","\t\t","valor","\t\t","nombre"
        for el in self.tabla:
            if el:
                if el["tipo"] is "_procedure":
                    print self.tabla.index(el),"\t\t",el["tipo"],"\t",el["valor"],"\t\t",el["nombre"]
                else:
                    print self.tabla.index(el),"\t\t",el["tipo"],"\t\t",el["valor"],"\t\t",el["nombre"]
