v1 = input('Digite um dado: ')

tipo = ''
if v1.isnumeric():
    tipo = 'numeric'
elif v1.isalpha():
    tipo = 'alpha'
else:
    tipo = 'outro'

print('O valor é {0}'.format(tipo))
