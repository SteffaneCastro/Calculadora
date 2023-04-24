# função para adição
def add(x, y):
    return x + y

# função para subtração
def subtract(x, y):
    return x - y

# função para multiplicação
def multiply(x, y):
    return x * y

# função para divisão
def divide(x, y):
    return x / y

# exibição do menu de opções
print("Selecione uma operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

# entrada do usuário
choice = input("Digite sua escolha (1/2/3/4): ")

# entrada dos números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# cálculo do resultado
if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
    print(num1,"/",num2,"=", divide(num1,num2))
else:
    print("Escolha inválida")
