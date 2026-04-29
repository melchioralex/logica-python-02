x= int(input('Digite um número: '))
y= int(input('Digite o segundo número: '))

while x<0 or y<0:
    print('Erro: os números devem ser inteiros e positivos')
    x= int(input('Digite um número: '))
    y= int(input('Digite o segundo número: '))

if y%2 == 0:
    r= y-x
    print(f'O resultado é {r}')
else:
    r= (y/x)
    print(f'O resultado é {r}')