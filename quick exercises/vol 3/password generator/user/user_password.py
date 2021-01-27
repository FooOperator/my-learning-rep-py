import random

preset_names = ['Kyle', 'Maynard', 'Rudy', 'Carol', 'Rock']

class User():
    characters = {
        'upper': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'lower': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower(),
        'digits': '1234567890',
        'symbols': '{}[](),;:.-_/\\?+*#'
    }  
    
    def __init__(self, inputted_name):
        self.username = inputted_name
    
    def generate(self):
        pool = ''
        while pool == '':
            for i in self.characters:
                if random.choice([True, False]) == True:
                    pool += self.characters[i]
        length = int(len(pool)/2)
        self.password = ''.join(random.sample(pool, length))
    
    def show_info(self):
        print('Username: {}\nPassword: {}'.format(self.username, self.password))

user = User(preset_names[random.choice(range(0, len(preset_names)))])
user.generate()
user.show_info()

