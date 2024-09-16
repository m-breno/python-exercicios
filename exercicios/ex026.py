# -------------#[ DESAFIO 000 ]#------------- #
# Crie um programa que leia uma frase e       #
# mostre:                                     #
#                                             #
#   - Quantas vezes aparece a letra "A"       #
#   - Em que posição ela aparece pela primei- #
# ra vez                                      #
#   - Em que posição ela aparece pela última  #
# vez.                                        #
# ------------------------------------------- #

frase = str(input('Digite uma frase: ')).strip().lower()

print('Sua frase tem {} letras "a"'.format(frase.count('a')))
print('Ela aparece pela primeira vez na posição {}'.format(frase.find('a') + 1))
print('Ela aparece pela última vez na posição {}'.format(frase.rfind('a') + 1))
