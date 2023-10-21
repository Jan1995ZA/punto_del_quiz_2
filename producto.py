class Producto:
    def __init__(self, id, nombre, descripcion, costo, cantidad):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.cantidad = cantidad
        self.precio_de_venta = None

    def registrar_precio_venta(self, callback):
        if callable(callback):
            self.precio_de_venta = callback(self.costo)
        else:
            raise ValueError("El callback debe ser una función")

