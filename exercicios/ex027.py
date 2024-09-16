# -------------#[ DESAFIO 027 ]#------------- #
# Crie um programa que leia o nome completo   #
# de uma pessoa e mostre o primeiro e o últi- #
# mo nome separadamente.                      #
#                                             #
#   Ex: Ana Maria de Souza                    #
#   primeiro = Ana                            #
#   último = Souza                            #
# ------------------------------------------- #

nome = str(input('Digite seu nome completo: ')).strip().split()

print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[-1]))
