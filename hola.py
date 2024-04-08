def calculadora(num1,num2,operatation):
    if operatation == '+':
        print(num1 + num2)
    elif operatation == "-":
        print (num1 - num2)
    elif operatation == "*":
        print (num1 * num2)
    else:
        print (num1 / num2 )  




numero1 = int(input("digita el numero 1 => "))
numero2 = int(input("digita el numero 2 => "))
operacion = input("digite que operacion deseas realiza, +,-,*,/ => ")
calculadora(numero1,numero2,operacion)
