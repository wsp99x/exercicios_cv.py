du = int(input('Digite quantos dias o carro foi utilizado: '))
km = float(input('Digite quantos quilometros o carro percorreu: '))
vsp = (du * 60) + (km * 0.15)
print('O valor toal a ser pago pela utilização do carro é de R${}'.format(vsp))