def calcular_suma(num1, num2):
    return num1 + num2

def main():
    while True:
        print("Calculadora de Suma")
        print("1. Sumar")
        print("2. Borrar")
        print("3. Salir")
        
        opcion = input("Selecciona una opción (1-3): ")

        if opcion == '1':
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
                resultado = calcular_suma(num1, num2)
                print(f"Resultado: {resultado}")
            except ValueError:
                print("Por favor, ingresa números válidos.")
        
        elif opcion == '2':
            print("Entradas borradas. Puedes empezar de nuevo.")

        elif opcion == '3':
            print("Saliendo de la calculadora.")
            break
        
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
