from classes.Type import Type
from classes.Fight import Fight
import time

def start():
    while True:
        print(' ')
        print('MENU')
        print('1 - Lancer la partie')
        print('2 - Quitter')
        print(' ')
        number = input('Entrer un chiffre > ')
        print(' ')
        if number.isdigit() == False:
            print(' ')
            print('Entrer le chiffre 1 ou 2 !')
            print(' ')
        elif number == "1":
            game()
        elif number == "2":
            break
        else:
            print(' ')
            print('Entrer un chiffre valide !')
            print(' ')

def game():
    my_pokemon = Type()
    my_pokemon.choosePokemon()
    my_pokemon.initPoints()
    print("")
    print("-----------------")
    print("")
    print("Ton pokemon")
    my_pokemon.displayPokemon()
    pokemon_random = Type()
    pokemon_random.randomPokemon()
    pokemon_random.initPoints()
    print("")
    print("Ton adversaire")
    pokemon_random.displayPokemon()

    print("")
    print("Prêt pour le combat ? (Appuyer sur la touche entrée)")
    input()
    
    fight = Fight(my_pokemon, pokemon_random)
    while my_pokemon.getPV() > 0 and pokemon_random.getPV() > 0:
        print("À ton tour ! Attaque ton adversaire " + pokemon_random.getName() + " avec ton Pokemon " + my_pokemon.getName() + " (Appuyer sur la touche entrée)")
        input()
        fight.attack(my_pokemon, pokemon_random)
        print('PV de l\'adversaire ' + pokemon_random.getName() + ' : ' + str(pokemon_random.getPV()))
        print('')
        fight.checkWinner()
        if fight.winner == True:
            break

        time.sleep(1)
        print("À son tour ! " + pokemon_random.getName() + " vous attaque")
        time.sleep(2)
        fight.attack(pokemon_random, my_pokemon)
        print('')
        print('PV de ton pokemon ' + my_pokemon.getName() + ' : ' + str(my_pokemon.getPV()))
        print('')
        time.sleep(2)
        fight.checkWinner()
        if fight.winner == True:
            break
start()