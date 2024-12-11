# Clase principal para representar una habitación en un hotel
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.ocupada = False

    def reservar(self):
        if not self.ocupada:
            self.ocupada = True
            print(f"La habitación {self.numero} ha sido reservada.")
        else:
            print(f"La habitación {self.numero} ya está ocupada.")

    def liberar(self):
        if self.ocupada:
            self.ocupada = False
            print(f"La habitación {self.numero} ha sido liberada.")
        else:
            print(f"La habitación {self.numero} ya está disponible.")


# Clase para gestionar las reservas del hotel
class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones(self):
        print(f"Habitaciones en el hotel {self.nombre}:")
        for habitacion in self.habitaciones:
            estado = "Ocupada" if habitacion.ocupada else "Disponible"
            print(f" - Habitación {habitacion.numero} ({habitacion.tipo}): {estado}")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear un hotel
    hotel = Hotel("Hotel Paraíso")

    # Agregar habitaciones
    hotel.agregar_habitacion(Habitacion(101, "Simple", 50))
    hotel.agregar_habitacion(Habitacion(102, "Doble", 80))
    hotel.agregar_habitacion(Habitacion(103, "Suite", 120))

    # Mostrar estado inicial de las habitaciones
    hotel.mostrar_habitaciones()

    # Reservar y liberar habitaciones
    hotel.habitaciones[0].reservar()
    hotel.habitaciones[1].reservar()
    hotel.habitaciones[0].liberar()

    # Mostrar estado final de las habitaciones
    hotel.mostrar_habitaciones()
