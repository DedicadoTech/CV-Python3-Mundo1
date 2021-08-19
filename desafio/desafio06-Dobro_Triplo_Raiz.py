#Faça Um programa que leia um número, e mostre:
#saida:
#o dobro de 85 vale 170.
#o triplo de 85 vale 255.
#a raiz quadrada de 85 é igual a 9.22.

num = int(input("Digite um número"))
print("O dobro de {} vale {}.\n"
      "O triplo de {} vale {}.\n"
      "A raiz quadrada de {} é igual a {}".format(num,num*2,
                                                  num,num*3,
                                                  num,float(num) ** 0.5))