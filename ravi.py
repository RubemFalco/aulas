# Calculadora simples em Python

print("=== Calculadora Simples ===")
print("Operações disponíveis:")
print("1 - Adição (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)\n")

# solicita os números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# solicita a operação desejada
operacao = input("Escolha a operação (+, -, *, /): ")

# verifica qual operação o usuário escolheu
if operacao == '+':
    resultado = num1 + num2
    print(f"\nResultado: {num1} + {num2} = {resultado}")

elif operacao == '-':
    resultado = num1 - num2
    print(f"\nResultado: {num1} - {num2} = {resultado}")

elif operacao == '*':
    resultado = num1 * num2
    print(f"\nResultado: {num1} * {num2} = {resultado}")

elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
        print(f"\nResultado: {num1} / {num2} = {resultado:.2f}")
    else:
        print("\nErro: divisão por zero não é permitida!")

else:
    print("\nOperação inválida. Tente novamente.")
