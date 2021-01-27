class Person:
    def __init__(self):
        self.name = input('name: ').capitalize()
        self.age = int(input('age: '))
        self.color = input('favorite color? ').capitalize()
        
    person_info = lambda self : print('My name is {} and I\'m {} years old and my favorite color is {}'.format(self.name, self.age, self.color))      
        
pep = Person()

pep.person_info()

class People:
    pass