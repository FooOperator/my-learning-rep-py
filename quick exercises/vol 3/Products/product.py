class Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
    
    def prod_manager(self, op, update):
        if op == '1':
            self.quantity += int(update)
        else:
            self.quantity -= int(update)
        return self.quantity
    
    def show_info(self):
        print('\nINFO DO USER\nNome: {}\nPreço: {}\nQuantidade: {}'.format(self.name, self.price, self.quantity))        