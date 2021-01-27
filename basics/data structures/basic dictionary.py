fighters = {
    'gg': 'Guilty Gear',
    'sf': 'Street Fighter',
    'tk': 'Tekken',
    'mk': 'Mortal Kombat',
    'mvc': 'Marvel Vs. Capcom'
}

query = ['Gg', 'gG', 'sf', 'dbz', 'MK', '1']

for acronym in query:
    print(acronym)
    print(fighters.get(acronym.lower(), 'Not here'))
