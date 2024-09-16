# -------------#[ DESAFIO 023 ]#--RESOLVIDO-- #
# Faça um programa que leia um número de 0    #
# a 9999 e mostre na tela cada um dos dígitos #
# separados.                                  #
#                                             #
#  Ex:                                        #
#    Digite um número: 1234                   #
#      unidade: 4                             #
#      dezena: 3                              #
#      centena: 2                             #
#      milhar: 1                              #
# ------------------------------------------- #

num = int((input("Digite um número: ")))

uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10

print(
    """Número: {}
    unidade:   {}
    dezena:    {}
    centena:   {}
    milhar:    {}
    """.format(num, uni, dez, cen, mil)
)
