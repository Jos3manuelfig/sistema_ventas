from abc import ABC, abstractmethod


class IProducto(ABC):
    @abstractmethod
    def obtener_precio(self) -> float:
        pass

    @abstractmethod
    def obtener_descripcion(self) -> str:
        pass


class Producto(IProducto):
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio

    def obtener_precio(self) -> float:
        return self.precio

    def obtener_descripcion(self) -> str:
        return self.nombre


class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto: IProducto):
        self.productos.append(producto)
        print(f"{producto.obtener_descripcion()} ha sido agregado al carrito.")

    def eliminar_producto(self, producto: IProducto):
        if producto in self.productos:
            self.productos.remove(producto)
            print(f"{producto.obtener_descripcion()} ha sido eliminado del carrito.")
        else:
            print(f"{producto.obtener_descripcion()} no está en el carrito.")

    def calcular_total(self) -> float:
        return sum([producto.obtener_precio() for producto in self.productos])

    def mostrar_productos(self):
        if not self.productos:
            print("El carrito está vacío.")
        else:
            print("Productos en el carrito:")
            for producto in self.productos:
                print(
                    f"- {producto.obtener_descripcion()} - ${producto.obtener_precio():.2f}"
                )


class ICalculadoraDeImpuestos(ABC):
    @abstractmethod
    def calcular(self, monto: float) -> float:
        pass


class CalculadoraImpuestoEstandar(ICalculadoraDeImpuestos):
    def calcular(self, monto: float) -> float:
        return monto * 0.15  # 15% de impuesto


class IDescuento(ABC):
    @abstractmethod
    def aplicar(self, monto: float) -> float:
        pass


class DescuentoPorcentaje(IDescuento):
    def __init__(self, porcentaje: float):
        self.porcentaje = porcentaje

    def aplicar(self, monto: float) -> float:
        return monto * (1 - self.porcentaje / 100)


class Usuario:
    def __init__(self, nombre: str, carrito: Carrito):
        self.nombre = nombre
        self.carrito = carrito

    def realizar_compra(
        self, descuento: IDescuento, calculadora_impuestos: ICalculadoraDeImpuestos
    ):
        if not self.carrito.productos:
            print(f"{self.nombre}, tu carrito está vacío.")
        else:
            total = self.carrito.calcular_total()
            print(f"Total antes de descuento e impuestos: ${total:.2f}")

            # Aplicar descuento
            total_con_descuento = descuento.aplicar(total)
            print(f"Total con descuento: ${total_con_descuento:.2f}")

            # Aplicar impuestos
            total_final = total_con_descuento + calculadora_impuestos.calcular(
                total_con_descuento
            )
            print(f"Total con impuestos: ${total_final:.2f}")

            # Completar compra
            self.carrito.productos.clear()
            print("Gracias por tu compra!")


# Crear productos
producto1 = Producto("Laptop", 1000)
producto2 = Producto("Mouse", 50)

# Crear carrito y agregar productos
carrito = Carrito()
carrito.agregar_producto(producto1)
carrito.agregar_producto(producto2)

# Mostrar productos
carrito.mostrar_productos()

# Crear usuario
usuario = Usuario("Carlos", carrito)

# Crear servicios de descuento e impuestos
descuento = DescuentoPorcentaje(10)  # 10% de descuento
impuestos = CalculadoraImpuestoEstandar()

# Realizar compra
usuario.realizar_compra(descuento, impuestos)
