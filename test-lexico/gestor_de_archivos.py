# -*- encoding: utf-8 -*-

class GestorDeArchivos:

    def __init__(self,filename):
        self.filename = filename
        
    def abrir(self):
        self.f = open(self.filename)

    def cerrar (self):
        self.f.close()

    def leer (self):
        c = self.f.read(1)
        if c :
            if c == '\n':
                return 'EOL'
            else : 
                return c
        else:
            return 'EOF'

