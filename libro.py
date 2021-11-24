class Libro:
    def __init__(self):
        self.libroEstado = False

    def abrir_libro(self):
        if not self.libroEstado:
            self.libroEstado = True
            return 'Abriendo...'
        return 'Ya estaba abierto'
    
    def cerrar_libro(self):
        if self.libroEstado:
            self.libroEstado = False
            return 'Cerrando...'
        return 'Ya estaba cerrado'
    
    def leer_libro(self):
        if self.libroEstado:
            return 'Leyendo'
        return 'Debe abrirlo para poder leerlo'