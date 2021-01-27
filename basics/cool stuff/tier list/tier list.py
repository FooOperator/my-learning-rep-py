import os
import json

tier_list = {
    'S': [],
    'A': [],
    'B': [],
    'C': [],
    'D': [] 
}



thisPath = 'lists\\'

if not os.path.exists(thisPath):
    os.makedirs(thisPath)

entry = ''
item = ''
file_name = input('nome da tier list: ')
os.system('cls')


while True:
    entry = input('Qual tier (S, A, B, C, D) ?\n0 para sair\n').upper()
    try:
        if entry == '0':
            break
        tier_list[entry]
    except:
        os.system('cls')
        print('Esse rank não existe!')
        continue
    item = input('Nome da coisa: ')
    tier_list[entry].append(item)
    os.system('cls')

os.system('cls')

for item in tier_list:
    print("Tier {}:\n{}".format(item, tier_list.get(item)))

f = open(thisPath + file_name + '.json', 'w')
f.write(json.dumps(tier_list, indent=4, sort_keys=False))
f.close()
