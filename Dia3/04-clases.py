class Mueble:
    tipo = "",
    valor = 00.00
    colores = []
    especificaciones = []
    def indicar_tipo(self):
        return self.tipo

    def mostrar_especificaciones(self):
        self.indicar_tipo()
        return self.especificaciones
objeto_mueble = Mueble()
otro_mueble = Mueble()

objeto_mueble.tipo = "SOFA"
otro_mueble.tipo = "FUTON"

