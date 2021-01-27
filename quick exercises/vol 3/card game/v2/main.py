from enum import Enum

class Heroes(Enum):
    ENFORCER = 1
    TACTICIAN = 2
    BERSERK = 3
    SPECIALIST = 4

class Player():
    def __init__(self):
        self.p_name = input('>Name: ')
        while True:
            print(['{} - {}'.format(i.value, i.name) for i in Heroes])
            try:
                self.p_hero = (Heroes(int(input('>Choose: '))))
                break
            except:
                print('Try again\n')
                
    def info(self):
        print(self.p_name, self.p_hero.name)
    
p1 = Player()
p2 = Player()

p1.info()
p2.info()

