##Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros
#Saida
#A medida de 3.0m corresponde a
#0.003km
#0.03hm
#0.3dam
#30dm
#300cm
#3000mm
##
valor = float(input('Digite uma distância em metros: '))
print('A medida de {}m corresponde a\n'
      '{:.3f}km (quilômetro)\n'
      '{:.2f}hm (hectômetro)\n'
      '{:.1f}dam (decâmetro)\n'
      '{:.0f}dm (decímetro)\n'
      '{:.0f}cm (centímetro)\n'
      '{:.0f}mm (milímetro)'.format(valor,valor * 0.001,valor * 0.01, valor * 0.1, valor * 10, valor * 100, valor * 1000))