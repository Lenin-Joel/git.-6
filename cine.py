asientos = 50
adulto = 5.00
niño = 3.00
tercera_edad = 2.50
entradas_vendidas = 0
recaudacion_total = 0
while True:
    print("================ CINE UTC ======================")
    print("      1. Comprar entradas")
    print("      2. Consultar asientos disponibles")
    print("      3. Consultar entradas vendidas")
    print("      4. Consultar recaudacion total")
    print("      5. Salir")
    print("===========================================")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        print("======== COMPRAR ENTRADAS ==========")
        print("1. Adulto - $5.00")
        print("2. Niño - $3.00")
        print("3. Tercera Edad - $2.50")
        tipo_entrada = int(input("Ingrese el tipo de entrada (1, 2 o 3): "))
        cantidad = int(input("Ingrese la cantidad de entradas: "))
        if tipo_entrada < 1 or tipo_entrada > 3:
            print("Tipo de entrada invalido.")
        elif cantidad <= 0:
            print("La cantidad debe ser mayor que cero.")
        elif cantidad > asientos:
            print("No hay suficientes asientos disponibles.")
        else:
            if tipo_entrada == 1:
                total = cantidad * adulto
            elif tipo_entrada == 2:
                total = cantidad * niño

            elif tipo_entrada == 3:
                total = cantidad * tercera_edad
            asientos -= cantidad
            entradas_vendidas += cantidad
            recaudacion_total += total

            print(f"Compra exitosa.")
            print(f"Total a pagar: ${total:.2f}")
    elif opcion == 2:
        print("=========== ASIENTOS DISPONIBLES ===========")
        print(f"Asientos disponibles: {asientos}")
    elif opcion == 3:

        print("======= ENTRADAS VENDIDAS ======")
        print(f"Entradas vendidas: {entradas_vendidas}")
    elif opcion == 4:

        print("======== RECAUDACION TOTAL =========")
        print(f"Recaudacion total: ${recaudacion_total:.2f}")
    elif opcion == 5:

        print("Gracias por utilizar el sistema de entradas de Cine UTC.")
        break
    else:
        print("Opcion invalida intente nuevamente.")