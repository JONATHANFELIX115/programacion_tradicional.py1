# Programa POO: Cálculo del promedio semanal de temperaturas

class ClimaSemanal:
    def __init__(self):
        """Inicializa la clase con una lista vacía de temperaturas."""
        self.temperaturas = []

    def ingresar_temperaturas(self):
        """Método para ingresar las temperaturas diarias."""
        print("Ingrese las temperaturas diarias (7 días):")
        for dia in range(7):
            temp = float(input(f"Día {dia + 1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        """Método para calcular el promedio semanal."""
        return sum(self.temperaturas) / len(self.temperaturas)

def main():
    """Función principal para organizar el flujo del programa."""
    print("Programa de Cálculo del Promedio Semanal de Temperaturas (POO)")
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"\nEl promedio semanal de las temperaturas es: {promedio:.2f} °C")

# Ejecutar el programa
if __name__ == "__main__":
    main()
