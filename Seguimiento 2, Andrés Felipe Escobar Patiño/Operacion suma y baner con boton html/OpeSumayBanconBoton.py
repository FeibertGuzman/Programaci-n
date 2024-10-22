def mostrar_banner():
    print("=" * 30)
    print("    CALCULADORA DE SUMA")
    print("=" * 30)

def realizar_suma():
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 + num2
        print(f"El resultado de {num1} + {num2} es: {resultado}")
    except ValueError:
        print("Error: Por favor, ingresa números válidos.")

def menu():
    mostrar_banner()
    while True:
        print("\nPresiona [1] para realizar una suma")
        print("Presiona [0] para salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            realizar_suma()
        elif opcion == "0":
            print("¡Gracias por usar la calculadora!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Iniciar la aplicación
if __name__ == "__main__":
    menu()