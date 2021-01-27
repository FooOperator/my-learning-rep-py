import random

cpfs_gerados = []

def gerarcpf():
    cpf = [] 
    for i in range(3):
        for j in range(3):
            cpf.append(str(random.randint(0, 9)))
        cpf.append('.')
    cpf.pop()
    cpf.append('-')
    for i in range(2):
        cpf.append(str(random.randint(0, 9)))
    return ''.join(cpf)
    
while True:
    print('Gerador de CPF')
    if input('>1 para gerar: ') == '1':
        cpfs_gerados.append(gerarcpf())
    else:
        break

print(cpfs_gerados)
