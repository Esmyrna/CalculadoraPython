def add(x, y):
    return(x + y)

def subtract(x, y):
    return(x - y)

def multiply(x, y):
    return(x * y)

def divide(x, y):
    return(x / y)

print("Selecione uma das opções: ")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

escolha = input("Digite um dos números informados:  ")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if escolha == '1':
    print("\n")
    print(num1, "+", num2, "=", add(num1, num2))

if escolha == '2':
    print("\n")
    print(num1, "-", num2, "=", subtract(num1, num2))
    print("\n")

if escolha == '3':
    print("\n")
    print(num1, "*", num2, "=", multiply(num1, num2))
    print("\n")

if escolha == '4':
    print("\n")
    print(num1, "/", num2, "=", divide(num1, num2))
    print("\n")
