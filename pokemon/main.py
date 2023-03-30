
from Type import *
from Fight import *

def start():
    while True:
        print(' ')
        print('MENU')
        print('1 - Lancer la partie')
        print('2 - Quitter')
        print(' ')
        number = input('Choissisez un chiffre > ')
        print(' ')
        if number.isdigit() == False:
            print(' ')
            print('Veuillez entrer le chiffre 1 ou 2 !')
            print(' ')
        elif number == "1":
            game()
            break
        elif number == "2":
            break
        else:
            print(' ')
            print('Veuillez entrer un chiffre valide !')
            print(' ')


def game():
    my_pokemon = Type()
    my_pokemon.choosePokemon()
    my_pokemon.initPoints()
    print("")
    print("-----------------")
    print("")
    print("Votre pokemon")
    my_pokemon.displayPokemon()

    
    pokemon_random = Type()
    pokemon_random.randomPokemon()
    pokemon_random.initPoints()
    print("")
    print("Voici votre adversaire")
    pokemon_random.displayPokemon()

    print("")
    print("Prêt pour le combat ? (Appuyer sur la touche entrée)")
    input()
    fight = Fight(my_pokemon, pokemon_random)
    fight.checkPV()
start()