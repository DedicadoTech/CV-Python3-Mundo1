#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
# mostre quantos dólares ela pode comprar
# Considere US$1,00 = R$5,27

carteira = float(input('Digite o valor que você tem na carteira:\n R$ '))
dolar = carteira / 5.29
#troca ponto por virgula
#converte de float para string
carteira = str(carteira).replace('.',',')

print('Valor em Dolar US$ {:.2f}\nValor em Reais R$ {}'.format(dolar, carteira))
#fim do programa