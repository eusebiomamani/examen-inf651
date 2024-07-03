def tabla_multiplicacion(numero):
    if numero < 10:
        print(f"la multiplicación del {numero}:")
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")
    else:
        print("El número ingresado debe ser menor a 10.")


if __name__ == "__main__":
    num = int(input("Ingrese un número menor a 10: "))
    tabla_multiplicacion(num)
