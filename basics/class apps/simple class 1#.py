class Person:
    name = ''
    age = 0
    def person_info(self): 
        print('The name is ' + self.name + ' and the age is ' + str(self.age))
        
pep = Person()
pep.name = 'Mark'
pep.age = 22
print(pep.name)
pep.person_info()
del pep.name
print(pep.name)