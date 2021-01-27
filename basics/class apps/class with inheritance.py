class Food:
    def _init_(self, name, color):
        self.name = name
        self.color = color
        
class Fruit(Food):
    what_is = lambda self : print('{} is fruit and is {}'.format(self.name, self.color))
        
class Veggie(Food):
    what_isNot = lambda self : print('{} is not fruit but it is {}'.format(self.name, self.color))
    
fr1 = Fruit()
fr2 = Fruit()
vg1 = Veggie()
vg2 = Veggie()

fr1._init_('Apple', 'Red')
fr2._init_('Tangerine', 'Orange')
vg1._init_('Celery', 'Green')
vg2._init_('Garlic', 'White')

fr1.what_is()
fr2.what_is()

vg1.what_isNot()
vg2.what_isNot()
