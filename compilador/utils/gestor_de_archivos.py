# -*- encoding: utf-8 -*-

class GestorDeArchivos:

    def __init__(self,filename):
        self.filename = filename
        
    def abrir_lectura(self):
        return self.abrir ('rU')

    def abrir_escritura(self):
        return self.abrir ('w+')

    def abrir(self,modo):
        try:
            self.f = open(self.filename,modo)
            return True
        except IOError:
            return False
            

    def cerrar (self):
        self.f.close()

    def leer_linea(self):
        linea = self.f.readline()
        if linea:
            return linea
        else:
            return 'EOF'

    def leer_linea_sin_nl(self):
        linea = self.leer_linea()
        return linea.rstrip()

    def leer (self):
        c = self.f.read(1)
        if c :
            if c == '\n':
                return 'EOL'
            else : 
                return c
        else:
            return 'EOF'

    def escribir(self,linea):
        self.f.write(linea)

