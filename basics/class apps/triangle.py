class Triangle:
    def __init__(self, height, base):
        self.height = height
        self.base = base
    
    def __repr__(self):
        self.area = (self.height * self.base)/2
        return f'This triangle\'s area is {self.area}'

t1 = Triangle(55, 3)

print(t1)