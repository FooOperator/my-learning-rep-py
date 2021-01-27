person = ('a bunch of stupid random words aaaaaaaaa')

search = lambda word : person.find(word)

print(search('a'))# first index
print(search('crap')) #-1 aka not found
print(search('stupid'))# 11th index
print(search('a bunch of'))# first index because it treats as a substring