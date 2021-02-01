class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f'name: {self.name}\nage: {self.age}'
    def __len__(self):
        return len(self.name)

p1 = Person('Chad', 13)
p2 = Person('Stacy', 30)
p3 = Person('Karen', 55)

print(p1, len(p1))
print(p2, len(p2))
print(p3, len(p3))
