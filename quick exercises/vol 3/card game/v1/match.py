import random

class Match():
    def __init__(self, p1, p2):
        self.player1, self.player2 = p1, p2
    
    def match_info(self):
        self.player1['mana'] = 2
        self.player2['mana'] = 1
        print('P1: {}\nP2: {}'.format(self.player1['name'], self.player2['name']))  
    
    def table(self):
        
        print(
'''
                    <{}***>      
                    {} 
{} 
                           
'''.format('*' * self.player1['mana'], self.player1['name'], random.sample(self.player1['deck'], 5)),
'''
                    <{}****> 
                    {} 
{} 
                          
'''.format('*' * self.player2['mana'], self.player2['name'], random.sample(self.player2['deck'], 5))
        )