'Object Oriented Programming systems'

from pprint import pprint

class candyMachine:
    'Food Dispenser'

    kind = 'junk food'

    def __init__(self, location):
        self.location = location
        self.cost = {}
        self.available = {}
        

cm_17_2 = candyMachine()
cm_17_2.location = 'Cisco Way - Building 17 floor 2 breakroom'
cm_17_3 = candyMachine()
cm_17_3.location = 'Cisco Way - Building 17 floor 3 - breakroom'

