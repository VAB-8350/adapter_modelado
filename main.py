from audiolibro import Audio_libro    
from libro import Libro

class Revista(Libro):
    pass

class Diario(Libro):
    pass

class Adapter_audiolibro(Audio_libro):
    def __init__(self):
        self.audiolibro = Audio_libro()
        
    def abrir_libro(self):
        return self.audiolibro.seleccionar_archivo()
    
    def cerrar_libro(self):
        return self.audiolibro.cerrar_archivo()
        
    def leer_libro(self):
        return self.audiolibro.reproducir()

for i in range(3):
    if i == 0:
        libro = Adapter_audiolibro()
    elif i == 1:
        libro = Revista()
    elif i == 2:
        libro = Diario()

    print(libro.abrir_libro())
    print(libro.leer_libro())
    print(libro.cerrar_libro())
    print("===============")
