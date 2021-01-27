import string

plain_text = 'hello world'
shift = 26 - 7

shift %= 26

alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]

print(shifted)

table = str.maketrans(alphabet, shifted)

encrypted = plain_text.translate(table)

print(encrypted)