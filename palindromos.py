# Testar se uma palavra é um palíndromo. Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.   #Ame o poema

while True:

    palavra = str(input("Qual é a palavra que você deseja saber se é um Palíndromo? ")) 
    
    p = palavra .strip() .replace(' ', '') .lower() 
      
    if p[:] == p[::-1]:
        print (f"A palavra {palavra} é um Palíndromo, ao contrário ela fica: {p[::-1]}.")
    else:
        print (f"A palavra {palavra} não é um Palíndromo, ao contrário ela fica: {p[::-1]}.")

    cont = ' '
    while cont not in 'SN':
        cont = str(input("Você deseja saber de mais alguma palavra? ")) .upper() .strip() [0]
    if cont == 'N':
        break

print("Tchau!!!")

