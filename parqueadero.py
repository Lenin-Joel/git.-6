# SISTEMA DE PARQUEADERO UTC.....yoooo
capacidad_maxima = int(input("Ingrese la capacidad máxima del parqueadero: "))
vehiculos = 0
while True:
    print("\n========== PARQUEADERO UTC ==========")
    print("1. Registrar ingreso de vehículo")
    print("2. Registrar salida de vehículo")
    print("3. Mostrar vehículos estacionados")
    print("4. Consultar espacios disponibles")
    print("5. Salir")
    print("=====================================")

    opcion = int(input("Seleccione una opción: "))

    match opcion:

        case 1:
            if vehiculos < capacidad_maxima:
                vehiculos += 1
                print("Ingreso registrado correctamente.")
            else:
                print("Parqueadero lleno. No hay espacios disponibles.")

        case 2:
            if vehiculos > 0:
                vehiculos -= 1
                print("Salida registrada correctamente.")
            else:
                print("No hay vehículos en el parqueadero.")

        case 3:
            print("Vehículos estacionados:", vehiculos)

        case 4:
            disponibles = capacidad_maxima - vehiculos
            print("Capacidad máxima:", capacidad_maxima)
            print("Vehículos estacionados:", vehiculos)
            print("Espacios disponibles:", disponibles)

        case 5:
            print("Gracias por utilizar el parqueadero UTC.")
            break

        case _:
            print("Opción incorrecta. Intente nuevamente.")
