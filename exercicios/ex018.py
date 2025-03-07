from math import sin , cos, tan, radians
a = int(input('Digite um angulo qualquer e descubra seno, cosseno e tangeente: '))
seno = sin(radians(a))
cosseno = cos(radians(a))
tangente = tan(radians(a))
print('Seno: {:.2f} \n Cosseno: {:.2f} \n Tangente: {:.2f}'.format(seno, cosseno, tangente))