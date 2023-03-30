import random

class Pokemon:
    def __init__(self):
        self.__name = ""
        self.type = []
        self.__pv = 100
        self.level = 0
        self.attack_power = 0
        self.defense = 0
        self.names_pokemon = [["Bulbizzare", ["Poison", "Plante"]], ["Salamèche", ["Feu"]], ["Marill", ["Feu", "fée"]], ["Carapuce", ["Eau"]], ["Roucool", ["Normal", "Vol"]], ["Evoli", ["Normal"]]]

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setPV(self, points):
        self.__pv = points

    def getPV(self):
        return self.__pv
    
    # Choix d'un pokemon depuis la liste 
    def choosePokemon(self):
        print('Choissisez votre pokemon parmis la liste ')
        flag = False
        for pokemon in self.names_pokemon:
            chaine = ' - '.join(str(i) for i in pokemon[1])
            print(pokemon[0] + " / Type: " + chaine)
        while not flag:
            input_name = input("> ") 
            for name, type in self.names_pokemon:
                if name == input_name:
                    self.setName(input_name)
                    self.type = type
                    flag = True
                    break
            else:
                print('Le pokemon n\'existe pas, Veuillez réessayez' )
    
    # Pokemon adversaire aléatoire
    def randomPokemon(self):
        pokemon_random = random.choice(self.names_pokemon)
        self.setName(pokemon_random[0])
        self.type = pokemon_random[1]
        






