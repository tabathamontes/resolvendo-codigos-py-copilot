#Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. Uma dica é: Utilize condicionais para realizar a verificação e, se possível, faça uso do Github Copilot(ou outra IA) para otimizar a estrutura do código.

while True:
    num = int(input("Digite um número inteiro: "))

    if num % 2 == 0:
        print(f"O número {num} é Par!!!")
    else:
        print(f"O número {num} é Ímpar!!!")
    
    cont = ' '
    while cont not in 'SN':
        cont = str(input("Você deseja consultar outro número? ")) .upper() .strip() [0]
    if cont == 'N':    
            break

print("Até mais!!!")

