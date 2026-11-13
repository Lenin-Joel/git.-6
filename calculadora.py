num1= float(input("Ingrese el primer numero  "))
num2 = float(input("Ingrese el segundo numero  "))
operacion = input("Ingrese la operacion a realizar (+, -, *, /): ")
if operacion == "+":
    print(num1 + num2)
elif operacion == "-":
    print(num1 - num2)
elif operacion == "*":
    print(num1 * num2)
elif operacion == "/" and num2 != 0:
    print(num1 / num2)
else:
    print("Error: No se puede dividir entre cero")
