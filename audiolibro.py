class Audio_libro():
    def __init__(self):
        self.seleccionado = False

    def seleccionar_archivo(self):
        if not self.seleccionado:
            self.seleccionado = True
            return 'Seleccionando...'
        return 'debe seleccionar archivo'
    
    def cerrar_archivo(self):
        if self.seleccionado:
            self.seleccionado = False
            return 'Cerrando audiolibro...'
        return 'Ya estaba cerrado'
    
    def reproducir(self):
        if self.seleccionado:
            return 'Reproduciendo'
        return 'Debe seleccionarlo para poder reproducirlo'