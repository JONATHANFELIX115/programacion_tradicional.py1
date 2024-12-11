# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Programa Tradicional: Cálculo del promedio semanal de temperaturas

def ingresar_temperaturas():
    """Función para ingresar las temperaturas diarias."""
    temperaturas = []
    print("Ingrese las temperaturas diarias (7 días):")
    for dia in range(7):
        temp = float(input(f"Día {dia + 1}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    """Función para calcular el promedio semanal."""
    return sum(temperaturas) / len(temperaturas)

def main():
    """Función principal para organizar el flujo del programa."""
    print("Programa de Cálculo del Promedio Semanal de Temperaturas")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"\nEl promedio semanal de las temperaturas es: {promedio:.2f} °C")

# Ejecutar el programa
if __name__ == "__main__":
    main()

