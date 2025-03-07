nome = input ('Digite o nome do aluno: ')
disciplina = input('Digite a disciplina: ')
p1 = float(input('Digite a nota da P1: '))
p2 = float(input('Digite a nota da P2: '))
t = float(input('Digite a nota do trabalho: '))
média = (p1 + p2 + t) / 3
print ('A média do aluno {} na disciplina de {} é {}'.format(nome, disciplina, média))