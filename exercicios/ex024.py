# -------------#[ DESAFIO 024 ]#--RESOLVIDO-- #
# Crie um programa que leia o nome de uma ci- #
# dade e diga se ela começa ou não com o nome #
# 'Santo'.                                    #
# ------------------------------------------- #

cidade = str(input('Digite o nome da cidade: ')).strip() #.split()
print('Começa com "Santo"?')

#print('santo' in cidade[0].lower)
print(cidade[:5].lower == 'santo')
