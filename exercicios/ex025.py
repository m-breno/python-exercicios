# -------------#[ DESAFIO 025 ]#------------- #
# Crie um programa que leia o nome de uma     #
# pessoa e diga se ela tem "Silva" no nome.   #
# ------------------------------------------- #

nome = str(input("Digite seu nome completo: ")).split()
print('Tem "Silva" no nome? {}'.format('silva' in nome.lower()))
#print("Silva" in nome)
