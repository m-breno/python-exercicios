# -------------#[ DESAFIO 029 ]#--RESOLVIDO-- #
# Escreva um programa que leia a velocidade   #
# de um carro.                                #
#                                             #
# Se ele ultrapassar 80Km/h, mostre uma men-  #
# sagem dizendo que ele foi multado.          #
#                                             #
# A multa vai custar R$7,00 por cada Km/h     #
# acima do limite.                            #
#                                             #
#                                             #
# ------------------------------------------- #

vel_carro = int(input('Qual a velocidade do carro em Km/h? '))
limite_vel = 80
valor_multa = 7.00

if vel_carro > limite_vel:
    print(
        'O carro foi multado em R${:.2f}'.format((vel_carro - limite_vel) * valor_multa)
    )
print('Tenha um bom dia!')
