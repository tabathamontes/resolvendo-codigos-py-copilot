#Calcular a média de três notas fornecidas na entrada do usuário. Uma dica é: Utilize operadores aritméticos para realizar o cálculo da média.

while True:
    nota1 = float(input("Qual foi a 1º nota que o aluno tirou? "))
    nota2 = float(input("Qual foi a 2º nota que o aluno tirou? "))
    nota3 = float(input("Qual foi a 3º nota que o aluno tirou? "))

    media = (nota1 + nota2 + nota3) / 3

    print(f"O aluno ficou com a média: {media:.2f}")

    cont = ' '
    while cont not in 'SN':
        cont = str(input("Você deseja saber a média de mais algum aluno? ")) .upper() .strip() [0]
    if cont == 'N':
        break

print("Até logo!!!")