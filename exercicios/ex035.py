# -------------#[ DESAFIO 035 ]#------------- #
# Crie um programa que leia o comprimento de  #
# três retas e diga se elas podem ou não for- #
# mar um triângulo.                           #
# ------------------------------------------- #

a = int(input('Digite o comprimento da reta a: '))
b = int(input('Digite o comprimento da reta b: '))
c = int(input('Digite o comprimento da reta c: '))

if a < b + c and b < a + c and c < a + b:
    print('Um triângulo PODE ser formado.')
else:
    print('Um triângulo NÃO PODE ser formado.')
