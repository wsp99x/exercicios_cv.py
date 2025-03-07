p = input('Digite o produto que entrará em promoção: ')
pa = float(input('Digite o preço atual do produto: '))
d = float(input('Digite o desconto que será aplicado sobre o produto: '))

dt = (d / 100) * pa

print('O {} estava R${} mas somente no dia de hoje ou até durar os estoqeus você pagará apenas R${} aproveite!'.format(p, pa, dt))