# -*- encoding: utf-8 -*-

# Errores léxicos
SE_ESPERABA_IGUAL = "Se esperaba un igual"
FIN_INESPERADO_LITERAL = "Fin inesperado de un literal"
ENTERO_DEMASIADO_LARGO = "Entero demasiado largo"
LITERAL_DEMASIADO_LARGO = "Literal demasiado largo"
IDENTIFICADOR_DEMASIADO_LARGO = "Identificado demasiado largo"

# Errores sintácticos

# Errores semánticos

def error_lexico(mensaje,numero_de_linea):
    print "Error léxico:",mensaje,"en",numero_de_linea

def error_sintactico(mensaje,numero_de_linea):
    print "Error sintáctico:",mensaje,"en",numero_de_linea

def error_semantico(mensaje,numero_de_linea):
    print "Error semántico:",mensaje,"en",numero_de_linea

