# Producto representa un producto que se vende en la tienda
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def actualizar_stock(self, cantidad):
        self.stock += cantidad

    def __str__(self):
        return f"{self.nombre} - ${self.precio} - Stock: {self.stock}"


# Clase Cliente representa al usuario que puede hacer compras
class Cliente:
    def __init__(self, nombre):  # Cambié el punto por coma
        self.nombre = nombre
        self.carrito = []

    def agregar_al_carrito(self, producto, cantidad):
        if producto.stock >= cantidad:
            self.carrito.append((producto, cantidad))
            producto.actualizar_stock(-cantidad)
            print(f"{cantidad} x {producto.nombre} añadido al carrito.")
        else:
            print(f"No hay suficiente stock de {producto.nombre}.")

    def ver_carrito(self):
        print(f"\nCarrito de {self.nombre}:")
        total = 0
        for producto, cantidad in self.carrito:
            subtotal = producto.precio * cantidad
            print(f"{cantidad} x {producto.nombre} - ${subtotal}")
            total += subtotal
        print(f"Total a pagar: ${total}")


# Clase Tienda representa la tienda en sí
class Tienda:
    def __init__(self, nombre):  # Usar __init__ correcto
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print(f"\nProductos disponibles en {self.nombre}:")
        for producto in self.productos:
            print(producto)


# --- Ejemplo de uso del programa ---

# Crear productos
producto1 = Producto("Lip Gloss", 7, 5)
producto2 = Producto("BB Cream", 30, 20)

# Crear tienda y añadir productos
mi_tienda = Tienda("True Beauty")
mi_tienda.agregar_producto(producto1)
mi_tienda.agregar_producto(producto2)

# Mostrar productos disponibles
mi_tienda.mostrar_productos()

# Crear cliente y simular la compra
cliente = Cliente("Ana")
cliente.agregar_al_carrito(producto1, 1)
cliente.agregar_al_carrito(producto2, 2)

# Ver el carrito del cliente
cliente.ver_carrito()




       

