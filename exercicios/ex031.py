# -------------#[ DESAFIO 000 ]#------------- #
# Crie um programa que pergunte a distância   #
# de uma viagem em Km.                        #
#                                             #
# Calcule o preço da passagem, cobrando       #
# R$0,50 para viagens de até 200Km e R$0,45   #
# para viagens mais longas.                   #
# ------------------------------------------- #

distância = int(input('Qual é a distância da sua viagem? '))

if distância <= 200:
    valor_passagem = distância * 0.50
else:
    valor_passagem = distância * 0.45

print('Sua passagem sai por R${:.2f}'.format(valor_passagem))
