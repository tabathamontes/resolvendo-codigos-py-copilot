#Solicitar como entrada dois números e depois  realizar uma operação simples entre eles.

while True:
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))

    print("Qual operação você deseja fazer?")
    operacao = int(input("[1] Soma [2] Sulbtração [3] Multiplicação] [4] Divisão: "))


    if operacao == 1:
        print(f"O resultado é: {num1 + num2}") 
                
    elif operacao == 2:
        print("O resultado é: "f"{abs(num1 - num2)}") #abs é para dar o valor absoluto,e não me dar um número negativo,caso o 1º número seja < que o 2º número
                
    elif operacao == 3:
        print(f"O resultado é: {num1 * num2}")
                
    elif operacao == 4:
        print(f"O resultado é: {num1 / num2}")

    else:
        resultado = print("Operação inválida")        

    cont = ' '
    while cont not in 'SN':
        cont =str(input("Você deseja continuar? ")) .upper() .strip() [0]
    if cont == 'N':
            break
                
print("Até breve!!!")          
     
        