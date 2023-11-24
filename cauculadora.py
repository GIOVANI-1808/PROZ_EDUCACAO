def calculadora(num1, num2, operacao):
    try:
        if operacao == 1:
            return num1 + num2
        elif operacao == 2:
            return num1 - num2
        elif operacao == 3:
            return num1 * num2
        elif operacao == 4:
            return num1 / num2
        else:
            print("Operação inválida.")
            return 0
    except ZeroDivisionError:
        print("Erro: Divisão por zero.")
        return 0

# Exemplo de uso
numero1 = 10
numero2 = 0
operacao = 4  # Por exemplo, 4 representa divisão

resultado = calculadora(numero1, numero2, operacao)
print("Resultado:", resultado)

