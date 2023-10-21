from producto import Producto
from inventario import Inventario

def calcular_precio_venta_margen(costo):
    margen_de_venta = 0.1  # Ejemplo de margen de venta del 10%
    return costo / (1 - margen_de_venta)

if __name__ == "__main__":
    inventario = Inventario()

    producto1 = Producto(1, "Producto A", "Descripción del Producto A", 10, 50)
    inventario.registrar_producto(producto1, calcular_precio_venta_margen)

    producto2 = Producto(2, "Producto B", "Descripción del Producto B", 15, 30)
    inventario.registrar_producto(producto2, calcular_precio_venta_margen)

    inventario.imprimir_inventario()
