from classes.Pokemon import *

class Type(Pokemon):
    def __init__(self):
        super().__init__()  # Appel du constructeur de la classe parent
        
    # Initie les points/attaque/defense en fonction du type
    def initPoints(self):
        if "Poison" and "Plante" in self.type:
            self.setPV(110)
            self.defense = 40
            self.attack_power = 100
        elif "Feu" and "Vol" in self.type:
            self.setPV(120)
            self.defense = 35
            self.attack_power = 90
        elif "Electrique" and "Vol" in self.type:
            self.setPV(125)
            self.defense = 35
            self.attack_power = 85
        elif "Normal" and "Vol" in self.type:
            self.setPV(105)
            self.defense = 45
            self.attack_power = 80
        elif "Electrique" in self.type or "Poison" in self.type:
            self.defense = 60
            self.attack_power = 95
        elif "Eau" in self.type or "Feu" in self.type or "Normal" in self.type or "Terre" in self.type or "Plante" in self.type:
            self.defense = 35
            self.attack_power = 85

    # Affiche ses capacités
    def displayPokemon(self):
        print(self.getName() + '\nPoints de vie: ' + str(self.getPV()) + "\nAttaque: " + str(self.attack_power) + "\nDéfense: " + str(self.defense))