#Desenvolva um programa que leia as duas notas de um aluno calcule e mostre a sua média.
#saida:
#A média entre 5.5 e 2.0 é igual a 3.8

num1 = float(input('Digite a primeira nota do aluno: '))
num2 = float(input('Digite a segunda nota do aluno: '))
print('A média entre {} e {} é igual a {:.1f}'.format(num1,num2,(num1+num2)/2))