
class Fight:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def checkPV(self): 
        print(self.pokemon1.getPV())
        if self.pokemon1.getPV() == 0:
            print(self.pokemon1.getName() + " a perdu")
        elif self.pokemon2.getPV() == 0:
            print(self.pokemon2.getName() + " a perdu")