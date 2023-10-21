class Inventario:
    def __init__(self):
        self.productos = {}

    def registrar_producto(self, producto, callback):
        producto.registrar_precio_venta(callback)
        self.productos[producto.id] = producto

    def imprimir_inventario(self):
        for id, producto in self.productos.items():
            print(f"ID: {producto.id}, Nombre: {producto.nombre}, Descripción: {producto.descripcion}, Costo: {producto.costo}, Cantidad: {producto.cantidad}, Precio de Venta: {producto.precio_de_venta}")
