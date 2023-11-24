def calculadora():
    while True:
        print("\nEscolha a operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        escolha = input("Digite o número da operação desejada: ")

        if escolha == '0':
            print("Saindo da calculadora.")
            break
        elif escolha in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida. Certifique-se de inserir números.")
                continue

            if escolha == '1':
                resultado = num1 + num2
            elif escolha == '2':
                resultado = num1 - num2
            elif escolha == '3':
                resultado = num1 * num2
            elif escolha == '4':
                if num2 != 0:
                    resultado = num1 / num2
                else:
                    print("Erro: Divisão por zero.")
                    continue

            print("Resultado:", resultado)
        else:
            print("Essa opção não existe. Tente novamente.")

# Chamada da função calculadora
calculadora()
