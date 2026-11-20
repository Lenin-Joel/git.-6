asientos=50
adulto=5.00
niño=3.00
tercera_edad=2.50
print("============== Cine utc==================")
print("      1.comprar entradas")
print("      2.Consultarb asientos disponibles")
print("      3.consultar entradas vendidas")
print("      4.Consultar recaudacion total")
print("      5.Salir")
opcion=int(input("Ingrese una opcion: "))
print("==========================================")
print("opcion seleccionada: ",opcion)
if opcion==1:
    print("=== COMPRAR ENTRADAS ===")
    print("Tipos de entradas disponibles:")
    print("1. Adulto - $5.00")
    print("2. Niño - $3.00")
    print("3. Tercera Edad - $2.50")
    tipo_entrada = int(input("Ingrese el tipo de entrada (1, 2 o 3): "))
    cantidad = int(input("Ingrese la cantidad de entradas: "))

    if cantidad <= asientos:
        if tipo_entrada == 1:
            total = cantidad * adulto
        elif tipo_entrada == 2:
            total = cantidad * niño
        elif tipo_entrada == 3:
            total = cantidad * tercera_edad
        else:
            print("Tipo de entrada inválido.")
            total = 0

        asientos -= cantidad
        print(f"Compra exitosa. Total a pagar: ${total:.2f}")
    else:
        print("No hay suficientes asientos disponibles.")
if opcion==2:
    print("=== CONSULTA DE ASIENTOS DISPONIBLES ===")
    print(f"Asientos disponibles: {asientos}")
    if opcion ==3:
        print("=== CONSULTA DE ENTRADAS VENDIDAS ===")
        entradas_vendidas = 50 - asientos
        print(f"Entradas vendidas: {entradas_vendidas}")
        if opcion ==4:
            print("=== CONSULTA DE RECAUDACIÓN TOTAL ===")
            recaudacion_total = (50 - asientos) * adulto + (50 - asientos) * niño + (50 - asientos) * tercera_edad
            print(f"Recaudación total: ${recaudacion_total:.2f}")
if opcion ==5:
    print("Gracias por utilizar el sistema de entradas de cine.")
