#peça ao usuário que digite um valor, mostre seu antecessor e o seu sucessor
# saída: Analisando o valor 2, seu antecessor é 1 e o seu sucessor é 3

num = int(input("Digite um número: "))
print('analisando o valor {}, seu antecessor é {} e o seu sucessor é {}' .format(num,num-1,num+1))
