class Fight:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.winner = False

    # Fonction d'ataque, avec l'attaquant et la victime en arg
    def attack(self, attacker, victim):
        result = 0
        if "Eau" in attacker.type and "Feu" in victim.type or "Feu" in attacker.type and "Terre" in victim.type or "Terre" in attacker.type and "Eau" in victim.type :
            result = (victim.getPV() + victim.defense) - (attacker.attack_power * 2)
        elif "Eau" in attacker.type and "Terre" in victim.type or "Feu" in attacker.type and "Eau" in victim.type or "Terre" in attacker.type and "Feu" in victim.type  :
            result = (victim.getPV() + victim.defense) - (attacker.attack_power * 0.5)
        elif "Normal" in attacker.type and "Eau" in victim.type or "Normal" in attacker.type and "Feu" in victim.type or "Normal" in attacker.type and "Terre" in victim.type:
             result = (victim.getPV() + victim.defense) - (attacker.attack_power * 0.75)
        else: 
            result = (victim.getPV() + victim.defense) - (attacker.attack_power)
        if result <= 0:
            victim.setPV(0)
        else:
            victim.setPV(result)

    # Vérifie qui a gagné
    def checkWinner(self): 
        if self.pokemon1.getPV() == 0:
            print("|| Dommage tu as perdu... Ton adversaire " + self.pokemon2.getName() + " a gagné ||\n")
            print(" ")
            self.winner = True
        elif self.pokemon2.getPV() == 0:
            print("|| Bravo ! Tu as gagné avec le pokemon " + self.pokemon1.getName() + " ||\n")
            print(" ")
            self.winner = True

