import random
print ('Vamos decibir o primeiro batedor da disputa de pênaltis! ')
j1 =  input ('Digite o primeiro jogador: ')
j2 =  input ('Digite o segundo jogador: ')
j3 =  input ('Digite o terceiro jogador: ')
j4 =  input ('Digite o quarto jogador: ')
lista = [j1,j2,j3,j4]
primeiro_batedor = random.choice(lista) 
print('O primeiro batedor será o: {}'.format(primeiro_batedor))