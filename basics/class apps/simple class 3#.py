class Game:
    def __init__(self, name, franchise, grade):
        self.name = name
        self.franchise = franchise
        self.grade = grade
        
    game_info = lambda self: print(self.__dict__)
        

game1 = Game('Yakuza 0', 'Ryu Ga Gotoku', 'S-')
game2 = Game('DmC Devil May Cry', 'Devil May Cry', 'B+')
game3 = Game('Call Of Duty Black Ops: Cold War', 'Call Of Duty', 'A-')

game1.game_info()
game2.game_info()
game3.game_info()