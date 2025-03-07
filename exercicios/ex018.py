import math
a = int(input('Digite um angulo qualquer e descubra seno cosseno e tangeente: '))
seno = math.sin(math.radians(a))
cosseno = math.cos(math.radians(a))
tangente = math.tan(math.radians(a))
print('Seno: {}, \n Cosseno: {} \n Tangente: {}'.format(seno, cosseno, tangente))