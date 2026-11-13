# Programa para ingresar, ordenar y analizar 10 números
numeros = []
print("=== INGRESO DE 10 NUMEROS ===")
for i in range(10):
    numero = float(input(f"Ingrese el numero {i + 1}: "))
    numeros.append(numero)
numeros.sort(reverse=True)
mayor = max(numeros)
menor = min(numeros)
print("\n=== RESULTADOS ===")
print("Numeros ordenados de mayor a menor:")
print(numeros)
print("El numero mas alto es:", mayor)
print("El numero mas bajo es:", menor)
print("\nAnalisis completado correctamente.")