import string as s

print(list(filter(lambda x: int(x) % 2 == 0, s.digits)))
print(list(filter(lambda x: int(x) % 2 == 1, s.digits)))
print(list(filter(lambda x: x in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'], s.ascii_lowercase)))