# -*- encoding: utf-8 -*-

from operator import itemgetter

class GestorDeErrores:

    # Errores léxicos
    IDENTIFICADOR_DEMASIADO_LARGO = "Identificador demasiado largo"
    ENTERO_DEMASIADO_LARGO = "Entero demasiado largo"
    FIN_INESPERADO_LITERAL = "Fin inesperado de un literal"
    LITERAL_DEMASIADO_LARGO = "Literal demasiado largo"
    SE_ESPERABA_IGUAL = "Se esperaba un igual"
    COMILLAS_EN_LUGAR_DE_APOSTROFO = "El literal se debe delimitar por apóstrofos en lugar de comillas"

    # Errores sintácticos
    SE_ESPERABA_PUNTO = "Se esperaba un punto"
    SE_ESPERABA_IDENTIFICADOR = "Se esperaba un identificador"
    SE_ESPERABA_IGUAL = "Se esperaba un igual"
    SE_ESPERABA_NUMERO = "Se esperaba un número"
    SE_ESPERABA_COMA_PUNTOYCOMA = "Se esperaba un coma o un punto y coma"
    SE_ESPERABA_PUNTOYCOMA = "Se esperaba un punto y coma"
    SE_ESPERABA_ASIGNACION = "Se esperaba una asignación"
    SE_ESPERABA_END_PUNTOYCOMA = "Se esperaba un END o un punto y coma"
    SE_ESPERABA_THEN = "Se esperaba THEN"
    SE_ESPERABA_DO = "Se esperaba DO"
    SE_ESPERABA_OPERADOR_RELACIONAL = "Se esperaba operador relacional"
    SE_ESPERABA_IDENTIFICADOR_NUMERO_PARENTESISAPERTURA = "Se esperaba un \
identificador, un número, o un paréntesis de apertura"
    SE_ESPERABA_PARENTESISCIERRE = "Se esperaba un paréntesis de cierre"
    SE_ESPERABA_COMA_PARENTESISCIERRE = "Se esperaba una coma o un paréntesis de cierre"
    SE_ESPERABA_PARENTESISAPERTURA = "Se esperaba un paréntesis de apertura"

    FIN_INESPERADO_PROGRAMA = "Fin inesperado de programa"

    # Errores semánticos
    VARIABLE_YA_DEFINIDA = "En este ámbito ya fue definida la variable"
    CONSTANTE_YA_DEFINIDA = "En este ámbito ya fue definida la constante"
    PROCEDURE_YA_DEFINIDO = "En este ámbito ya fue definido el procedimiento"
    TIPO_INCORRECTO = "Tipo incorrecto"
    NO_DECLARADO = "No declarado"
    DEMASIADAS_DECLARACIONES = "Demasiadas declaraciones"

    def __init__(self):
        self.errores_lexicos = []
        self.errores_sintacticos = []
        self.errores_semanticos = []

    def error_lexico(self,mensaje,numero_de_linea):
        #print "Error léxico:",mensaje,"en la línea",numero_de_linea
        a = {
            "tipo"      :   "lexico",
            "linea"     :   numero_de_linea,
            "mensaje"   :   mensaje,
        }
        self.errores_lexicos.append(a)

    def error_sintactico(self,mensaje,S,cadena,numero_de_linea):
        #print "Error sintáctico:",mensaje,"en la línea",numero_de_linea
        a = {
            "tipo"      :   "sintactico",
            "linea"     :   numero_de_linea,
            "mensaje"   :   mensaje,
            "S"         :   S,
            "cadena"    :   cadena,
        }
        self.errores_sintacticos.append(a)

    def error_semantico(self,mensaje,cadena,numero_de_linea):
        #print "Error semántico:",mensaje,"en la línea",numero_de_linea
        a = {
            "tipo"      :   "semantico",
            "linea"     :   numero_de_linea,
            "mensaje"   :   mensaje,
            "cadena"    :   cadena,
        }
        self.errores_semanticos.append(a)

    def resumen(self):
        errores = sorted(self.errores_lexicos + self.errores_sintacticos \
        + self.errores_semanticos,key=itemgetter('linea'))
        if errores:
            if len(errores) == 1:
                print "Hubo",len(errores),"error"
            else: 
                print "Hubo",len(errores),"errores"
            for error in errores:
                if (error["tipo"] == "lexico"):
                    print "Error",error["tipo"]+":",error["mensaje"],"en la línea",error["linea"]
                if (error["tipo"] == "sintactico"):
                    print "Error",error["tipo"]+":",error["mensaje"],"y se recibio un",error["S"],"(\""+error["cadena"]+"\")","en la línea",error["linea"]
                if (error["tipo"] == "semantico"):
                    print "Error",error["tipo"]+":",error["mensaje"],error["cadena"],"en la línea",error["linea"]
            return len(errores)
        else:
            print "No hubo errores"
            return 0
