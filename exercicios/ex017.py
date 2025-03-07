import math
n1 = float(input('Digite ciomprimento do cateto oposto: '))
n2 = float(input('Digite o comprimento do cateto adjacente: ')) 
h = math.hypot(n1**2 + n2**2)
print(h)