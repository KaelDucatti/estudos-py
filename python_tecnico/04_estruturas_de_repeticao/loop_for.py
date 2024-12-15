quantidade = int(input('Quantas vezes esse loop deve rodar?'))
soma = 0

for n in range(1, quantidade + 1):
    num = int(input(    'Informe o {n}/{quantidade} valor: '))
    soma = soma + num
print(f'A soma é {soma}')
