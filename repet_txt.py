#Solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetindo o número de vezes informado.

algo = str(input("Digite algo: "))
vezes =int(input("Quantas vezes você quer repetir o que você digitou? "))

cont = 0
while cont < vezes:
    print(f"{algo}",end=" ")
    cont += 1



#for _ in range(vezes):
 #print(f"{algo}")


#resultado = (algo + " ") * vezes
#print(resultado)