class ffOut:
    def __init__(self, field_frame):
        self.field_frame = field_frame
        self.valores_guardados = {}

    def guardar_valores(self):
        self.valores_guardados = self.field_frame.obtener_valores()
        

    def obtener_valor_por_criterio(self, criterio):
        if criterio in self.valores_guardados:
            return self.valores_guardados[criterio]
        else:
            return None