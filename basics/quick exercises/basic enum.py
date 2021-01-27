from enum import Enum

class Countries(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672

sortedKeys = []

for country in Countries:
    print(country._name_)
    print(country._value_)
    sortedKeys.append(country._value_)

print(sorted(sortedKeys))