nome = input('Digite o nome do funcionário que ganhará o aumento: ')
sa = float(input('Digite o salário atual: '))
pa = float(input('Digite a porcentagem de aumento: '))
a = (pa / 100) * sa + sa
print('O novo salário do funcionário {} será de R${}!'.format(nome, a))
