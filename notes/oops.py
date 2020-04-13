'Object oriented programming systems (OOPS)'

from pprint import pprint
import json

class CandyMachine:
    'Food dispenser'

    kind = 'junk food'

    def __init__(self, location):
        self.location = location
        self.cost = {}
        self.available = {}
        self.earnings = 0.0

    def load(self, product, quantity, price):
        self.cost[product] = price
        self.available[product] = quantity

    def __len__(self):
        return len(self.cost)

    def vend(self, product, money):
        if self.available.get(product, 0) == 0:
            raise ValueError(f'Sorry, I am out of {product}')
        cost = self.cost[product]
        if cost > money:
            raise ValueError(f'Sorry, the {product} costs ${cost:.2f}')
        change = money - cost
        print(f'Here, have a {product} and here is your change ${change:.2f}')
        self.available[product] -= 1
        self.earnings += cost

    def report(self):
        print(f'\nThere are {len(self)} kinds of products possibly in the machine')
        print('-' * 40)
        for product, quantity in self.available.items():
            if quantity:
                print(f'We have {quantity} {product} on hand for ${self.cost[product]:.2f}')
        print('-' * 40)
        print(f'The total earnings are: ${self.earnings:.2f}')

    def load_json(self, filename):
        with open(filename) as f:
            shipment = json.load(f)
        for product, prod_info in shipment.items():
            quantity, price = prod_info
            self.cost[product] = price
            new_quantity = self.available.get(product, 0) + quantity
            self.available[product] = new_quantity            

if __name__ == '__main__':
    
    cm_17_2 = CandyMachine('Cisco Way -- Bldg 17 -- Floor 2 -- Breakroom')
    cm_17_2.load('reeses', 5, 0.75)
    cm_17_2.load('skittles', 3, 1.25)

    cm_17_3 = CandyMachine('Cisco Way -- Bldg 17 -- Floor 3 -- Breakroom')
    cm_17_3.load('reeses', 4, 0.75)
    cm_17_3.load('snickers', 5, 0.60)
    cm_17_3.load('popcorn', 2, 2.50)

    pprint(vars(cm_17_2))
    pprint(vars(cm_17_3))

    cm_17_2.vend('reeses', 1.00)
    cm_17_2.vend('skittles', 2.00)
    cm_17_2.vend('skittles', 2.00)
    cm_17_2.vend('skittles', 2.00)
    cm_17_2.report()

    cm_17_3.vend('reeses', 1.40)
    cm_17_3.report()

    cm_15_1 = CandyMachine('Cisco Way -- Bldg 15 -- Floor 1 -- Breakroom')
    cm_15_1.load('snickers', 3, 0.60)
    cm_15_1.load('reeses', 7, 0.90)
    cm_15_1.report()

    cm_15_1.load_json('notes/cm_15_1.json')
    cm_15_1.report()
