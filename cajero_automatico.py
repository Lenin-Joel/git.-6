
saldo = 100.0  # Saldo inicial

while True:
    print("""
==================== CAJERO AUTOMÁTICO UTC ====================
    1. Consultar saldo
    2. Depositar
    3. Retirar
    4. Salir
===============================================================
""")

    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            print(f"\nSu saldo actual es: ${saldo:.2f}")

        case "2":
            monto = float(input("Ingrese la cantidad a depositar: $"))

            if monto > 0:
                saldo += monto
                print(f"Depósito exitoso. Nuevo saldo: ${saldo:.2f}")
            else:
                print("El monto debe ser mayor a 0.")

        case "3":
            monto = float(input("Ingrese la cantidad a retirar: $"))

            if monto <= 0:
                print("El monto debe ser mayor a 0.")
            elif monto > saldo:
                print("Saldo insuficiente.")
            else:
                saldo -= monto
                print(f"Retiro exitoso. Nuevo saldo: ${saldo:.2f}")

        case "4":
            print("Gracias por utilizar nuestro cajero UTC.")
            break

        case _:
            print("Opción inválida. Intente de nuevo.")
