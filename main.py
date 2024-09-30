# aplicando princips solid


class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio


class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)
        print(f"{producto.nombre} ha sido agregado al carrito...")

    def eliminar_producto(self, producto: Producto):
        if producto in self.productos:
            self.productos.remove(producto)
            print(f"{producto.nombre} ha sido eliminado correctamente")
        else:
            print(f"{producto.nombre} no está en el carrito")

    def calcular_total(self):
        total = sum([producto.precio for producto in self.productos])
        return total

    def calcular_descuento(self, porcentaje: float):
        total = self.calcular_total()
        descuento = total * (porcentaje / 100)
        return total - descuento

    def aplicar_impuesto(self, tasa_impuesto: float):
        total = self.calcular_total()
        impuesto = total * (tasa_impuesto / 100)
        return total + impuesto

    def mostrar_productos(self):
        if not self.productos:
            print("El carrito está vacío.")
        else:
            print("Productos en el carrito:")
            for producto in self.productos:
                print(f"- {producto.nombre}")


class Usuario:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.carrito = Carrito()

    def realizar_compra(self):
        if not self.carrito.productos:
            print(f"{self.nombre}, tu carrito está vacío.")
        else:
            total = self.carrito.calcular_total()
            print(f"{self.nombre}, el total de tu compra es: ${total:.2f}")
            self.carrito.productos.clear()
            print("Gracias por tu compra!")


# Crear productos
producto1 = Producto("Laptop", 1000)
producto2 = Producto("Mouse", 50)
producto3 = Producto("Monitor", 75)
producto4 = Producto("Cpu", 7)
producto5 = Producto("Memoria", 5)
producto6 = Producto("Procedaror", 20)
producto7 = Producto("Disco duro", 15)
producto8 = Producto("Impresora", 50)
producto9 = Producto("Scaner", 20)
producto10 = Producto("Cables ", 10)
# Crear un usuario
usuario = Usuario("Carlos")

# Agregar productos al carrito
usuario.carrito.agregar_producto(producto1)
usuario.carrito.agregar_producto(producto2)
usuario.carrito.agregar_producto(producto3)
usuario.carrito.agregar_producto(producto4)
usuario.carrito.agregar_producto(producto5)
usuario.carrito.mostrar_productos()

# Eliminar un producto
usuario.carrito.eliminar_producto(producto2)
usuario.carrito.mostrar_productos()

# Aplicar descuento e impuestos
total_con_descuento = usuario.carrito.calcular_descuento(10)  # 10% de descuento
total_con_impuesto = usuario.carrito.aplicar_impuesto(15)  # 15% de impuesto

print(f"Total con descuento: ${total_con_descuento:.2f}")
print(f"Total con impuesto: ${total_con_impuesto:.2f}")

# Realizar compra
usuario.realizar_compra()
