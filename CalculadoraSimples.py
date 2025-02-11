while True:
    numero1 = input("Digite um número: ")
    numero2 = input("Digite outro número: ")
    operacao = input("Digite o operador (+-/*): ")

    numerosvalidos = None
    operadoresvalidos = '+-/*'

    try:
        numero1 = float(numero1)
        numero2 = float(numero2)
        numerosvalidos = True
    except:
        print("Digite um número válido")
        numerosvalidos = None
    if numerosvalidos is None:
        print ('Um ou ambos os números são inválidos')
        continue 
    if operacao not in operadoresvalidos:
        print ('Operador inválido')
        continue 
    if operacao == '+':
        print(numero1 + numero2)
    elif operacao == '-':
        print(numero1 - numero2) 
    elif operacao == '/':
        print(numero1 / numero2)
    elif operacao == '*':
        print(numero1 * numero2)

    if input("Deseja sair? (s/n): ") == 's':
        break
