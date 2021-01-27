from product import Product as prod

while True:
    test = prod(input('>nome: '), input('>preço: '), input('>quantidade: '))
    test.prod_manager(input('>1 para somar, qualquer outro para subtrair: '), input('>quantidade: '))
    test.show_info()
    if input('>deseja continuar? 1 para continuar, qualquer outro para sair: ') == '1':
        continue
    else:
        break