num1 = int(input("digita el numero 1"))
num2 = int(input("digita el numero 2"))
opertation = input("digite que operacion deseas realiza, +,-,*,/")

def calculadora(num1,num2,opertation):
    if opertation == "+":
        return num1 + num2
     if opertation == "-":
        return num1 - num2
    if opertation == "*":
        return num1 * num2
    else:
        return num1 / num2   