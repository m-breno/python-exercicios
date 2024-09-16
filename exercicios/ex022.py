# -------------#[ DESAFIO 022 ]#--RESOLVIDO-- #
#  Crie um programa que leia o nome completo  #
#  de uma pessoa e mostre:                    #
#                                             #
#  - O nome com todas as letras maiúsculas;   #
#  - O nome com todas minúsculas;             #
#  - Quantas letras ao todo                   #
#    (sem considerar espaços);                #
#  - Quantas letras tem o primeiro nome;      #
# ------------------------------------------- #

# nome = str(input('Digite seu nome completo: '))
nome = str(input('Digite seu nome completo: ')).strip()

print('Seu nome com letras maiúsculas é {}\n'.format(nome.upper()))
#print(nome.upper(), '\n')

print('Seu nome com letras minúsculas é {}\n'.format(nome.lower()))
#print(nome.lower(), '\n')

print('Seu nome tem {} letras ao todo\n'.format(len(nome) - nome.count(' ')))
#print('Seu nome tem {} letras ao todo\n'.format(''.join(nome.split())))
#print(len(''.join(nome.split())), '\n')

print('Seu primeiro nome é {} e tem {} letras\n'.format(nome.split()[0], len(nome.split()[0])))
#print('Seu primeiro nome tem {} letras\n'.format(nome.find(' ')))
#print(len(nome.split()[0]))
