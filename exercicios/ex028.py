# -------------#[ DESAFIO 028 ]#--RESOLVIDO-- #
# Crie um programa que faça o computador pen- #
# sar em um número inteiro entre 0 e 5 e peça #
# para o usuário tentar descobrir que número  #
# o computador escolheu.                      #
#                                             #
# O programa deverá escrever na tela se o     #
# usuário venceu ou perdeu.                   #
# ------------------------------------------- #

from random import randint
# from time import sleep

num_aleatorio = randint(0, 5)
num_chute = int(input('Chute um número de 0 a 5: '))

# print('Processando...')
# sleep(2)

if num_chute == num_aleatorio:
    print('PARABÉNS! Você venceu!')
else:
    print('Você perdeu! Mais sorte na próxima')
    print(f'O número escolhido era {num_aleatorio}')
