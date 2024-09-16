# -------------#[ DESAFIO 034 ]#------------- #
# Crie um programa que pergunte o salário de  #
# um funcionário e calcule o valor do seu     #
# aumento.                                    #
#                                             #
# Para salários superiores a R$1.250,00,      #
# calcule um aumento de 10%.                  #
#                                             #
# Para salários inferiores ou iguais, o au-   #
# mento é de 15%.                             #
# ------------------------------------------- #

salário = float(input('Digite o salário do funcionário: '))
if salário <= 1250:
    aumento = 15
else:
    aumento = 10

novo_salário = salário + (salário * aumento / 100)
print(
    'O novo salário do funcionário que ganhava R${:.2f} com aumento de {}% é R${:.2f}'.format(
        salário, aumento, novo_salário
    )
)
