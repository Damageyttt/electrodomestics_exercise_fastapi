# Clase base Electrodomestico
class Electrodomestico:
    def __init__(self, marca: str, modelo: str, consumoEnergetico: float):
        self.marca = marca
        self.modelo = modelo
        self.consumoEnergetico = consumoEnergetico

    def obtenerDetalles(self) -> str:
        return f"Electrodoméstico: {self.marca} {self.modelo}, Consumo: {self.consumoEnergetico} kWh"

# Clase derivada Lavadora
class Lavadora(Electrodomestico):
    def __init__(self, marca: str, modelo: str, consumoEnergetico: float, capacidad: float):
        super().__init__(marca, modelo, consumoEnergetico)
        self.capacidad = capacidad

    def obtenerDetalles(self) -> str:
        return f"Lavadora: {self.marca} {self.modelo}, Capacidad: {self.capacidad} kg, Consumo: {self.consumoEnergetico} kWh"

# Clase derivada Refrigerador
class Refrigerador(Electrodomestico):
    def __init__(self, marca: str, modelo: str, consumoEnergetico: float, tipo: str):
        super().__init__(marca, modelo, consumoEnergetico)
        self.tipo = tipo

    def obtenerDetalles(self) -> str:
        return f"Refrigerador: {self.marca} {self.modelo}, Tipo: {self.tipo}, Consumo: {self.consumoEnergetico} kWh"

# Clase derivada Horno
class Horno(Electrodomestico):
    def __init__(self, marca: str, modelo: str, consumoEnergetico: float, capacidad: float):
        super().__init__(marca, modelo, consumoEnergetico)
        self.capacidad = capacidad

    def obtenerDetalles(self) -> str:
        return f"Horno: {self.marca} {self.modelo}, Capacidad: {self.capacidad} L, Consumo: {self.consumoEnergetico} kWh"
