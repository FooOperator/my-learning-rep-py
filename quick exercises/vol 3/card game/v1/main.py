import random 
from match import Match

class Player():
    def __init__(self, name):
        cards = {
            'mage': ['fireball', 'frostblast', 'blind', 'dispel', 'stun'],
            'warrior': ['crush', 'slam', 'grab', 'shout', 'headbutt']
        }

        decks = {
            'mage': [cards['mage'][random.choice(range(len(cards['mage'])))] for i in range(20)],
            'warrior': [cards['warrior'][random.choice(range(len(cards['warrior'])))] for i in range(20)]
        }
        
        self.name = name
        self.deck = decks[random.choice(['mage', 'warrior'])]
    
p1 = Player('Cuckas')
p2 = Player('Brendo')

match = Match(p1.__dict__, p2.__dict__)
match.match_info()
match.table()

