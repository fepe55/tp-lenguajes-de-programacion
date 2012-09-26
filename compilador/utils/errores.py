# -*- encoding: utf-8 -*-

from operator import itemgetter

class GestorDeErrores:

    # Errores léxicos
    IDENTIFICADOR_DEMASIADO_LARGO = "Identificador demasiado largo"
    ENTERO_DEMASIADO_LARGO = "Entero demasiado largo"
    FIN_INESPERADO_LITERAL = "Fin inesperado de un literal"
    LITERAL_DEMASIADO_LARGO = "Literal demasiado largo"
    SE_ESPERABA_IGUAL = "Se esperaba un igual"

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

    def __init__(self):
        self.errores_lexicos = []
        self.errores_sintacticos = []
        self.errores_semanticos = []

    def error_lexico(self,mensaje,numero_de_linea):
        #print "Error léxico:",mensaje,"en la línea",numero_de_linea
        a = {
            "linea" : numero_de_linea,
            "mensaje" : mensaje,
        }
        self.errores_lexicos.append(a)

    def error_sintactico(self,mensaje,numero_de_linea):
        #print "Error sintáctico:",mensaje,"en la línea",numero_de_linea
        a = {
            "linea" : numero_de_linea,
            "mensaje" : mensaje,
        }
        self.errores_sintacticos.append(a)

    def error_semantico(self,mensaje,numero_de_linea):
        #print "Error semántico:",mensaje,"en la línea",numero_de_linea
        a = {
            "linea" : numero_de_linea,
            "mensaje" : mensaje,
        }
        self.errores_semanticos.append(a)

    def resumen(self):
        errores = sorted(self.errores_lexicos + self.errores_sintacticos \
        + self.errores_semanticos,key=itemgetter('linea'))
        if errores:
            for error in errores:
                print "Error sintáctico:",error["mensaje"],"en la línea",error["linea"]
