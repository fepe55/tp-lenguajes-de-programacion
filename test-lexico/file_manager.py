# -*- encoding: utf-8 -*-

class FileManager:

    def __init__(self,filename):
        self.filename = filename
        
    def open(self):
        self.f = open(self.filename)

    def close (self):
        self.f.close()

    def read (self):
        c = self.f.read(1)
        if c :
            if c == '\n':
                return 'EOL'
            else : 
                return c
        else:
            return 'EOF'

