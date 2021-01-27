import os

class Member():
    sex_choices = {'M': 'Male', 'F': 'Female'}
    def __init__(self):
        a = '1'
        while a != '0':
            self.name = input('Your name: ')
            while True:
                try:
                    self.age = 0
                    self.age = int(input('Your age: '))
                except ValueError:
                    print('\nNumbers plz')
                else:
                    break
            while True: 
                try:
                    self.sex = self.sex_choices[input('Sex (M/F): ').capitalize()]
                except KeyError:
                    print('\nM or F plz')
                else:
                    break
            a = input('Satisfied? (0 to get out): ')
            os.system('cls')

member = Member()
print(member.__dict__)