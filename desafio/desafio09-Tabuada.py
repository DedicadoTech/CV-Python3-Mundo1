##Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
#Saída:
#----------------------
#6 x 1 = 6
#6 x 2 = 12
#6 x 3 = 18
#....
#6 x 10 = 60
#---------------------
##
num = int(input('Digite um número para ver sua tabuada: '))
mult = int(input('Digite quantos multiplos desse número deseja visualizar: '))
print('-' * 52)
i = 0 #índice iniciando com 0
while i <= mult:
    print('|'+' {} x {} = {}'.format(num,i,num * i).center(50)+'|') ##usa o valor do índice como contador
    i = i+1
print('-' * 52)