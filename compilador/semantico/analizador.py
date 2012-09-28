# -*- encoding: utf-8 -*- 

CANT_MAX_IDENT = 256
CANT_MAX_VAR = 128
SIZE_OF_INT = 4

class AnalizadorSemantico:
    def __init__ (self):
        self.tabla = [None]*(CANT_MAX_IDENT-1)
        self.cant_variables = 0

    def validar (self,base,desplazamiento,nombre,tipos_esperados,errores,numero_de_linea):
        # Para el análisis semántico, los identificadores se buscarán en toda
        # la tabla, comenzando en la posición BASE+DESPLAZAMIENTO-1 y
        # retrocediendo hasta la posición 0. De esta forma, siempre se 
        # encontrará primero el identificador que haya sido declarado 
        # localmente. En caso de no encontrarse el identificador, deberá 
        # darse aviso de la falta de declaración.
        i = base+desplazamiento-1
        while i>=0 :
         if self.tabla[i]:
          if self.tabla[i]["nombre"] == nombre:
           tipo_erroneo = 0
           for tipo in tipos_esperados:
            if self.tabla[i]["tipo"] != tipo:
             tipo_erroneo += 1
           if tipo_erroneo == len(tipos_esperados):
            errores.error_semantico(errores.TIPO_INCORRECTO,nombre,numero_de_linea)
            return
           else:
            return self.tabla[i]["valor"] # Probablemente luego haga falta
         i-=1
             
             

        errores.error_semantico(errores.NO_DECLARADO,nombre,numero_de_linea)
        return

    def cargar (self,base,desplazamiento,nombre,tipo,valor,errores,numero_de_linea):

        # No debería estar cargado el mismo elemento entre 
        # base y base+deplazamiento-1

        i = base
        while i<base+desplazamiento:
         if self.tabla[i]:
          if self.tabla[i]["tipo"] == tipo:
           if self.tabla[i]["nombre"] == nombre:
            #print "Ya se definió la",tipo,nombre,"en este ámbito"
            if tipo is "_const":
             errores.error_semantico(errores.CONSTANTE_YA_DEFINIDA,nombre,numero_de_linea)
            if tipo is "_var":
             errores.error_semantico(errores.VARIABLE_YA_DEFINIDA,nombre,numero_de_linea)
            if tipo is "_procedure":
             errores.error_semantico(errores.PROCEDURE_YA_DEFINIDO,nombre,numero_de_linea)
         i+=1

        posicion = base+desplazamiento
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
                if self.cant_variables >= CANT_MAX_VAR :
                    errores.error_semantico

            if tipo is "_procedure":
                elemento ['valor'] = 0

            self.tabla[posicion] = elemento

        #else:
            # Error semántico
            # error_semantico(

        return

    def debug_imprimir_tabla (self):
        
        print "POSICIÓN","\t","TIPO","\t\t","VALOR","\t\t","NOMBRE"
        print "========================================================"
        for el in self.tabla:
            if el:
                if el["tipo"] is "_procedure":
                    print self.tabla.index(el),"\t\t",el["tipo"],"\t",el["valor"],"\t\t",el["nombre"]
                else:
                    print self.tabla.index(el),"\t\t",el["tipo"],"\t\t",el["valor"],"\t\t",el["nombre"]
