import random

from antagonist import Enemy
from items import first_aid
from protagonist import Player
from weapons import handgun, knife, rocket_launcher, shotgun


def random_encounter():
    player = Player("Captain Lucas Bennett", 100, 30)
    creeper = Enemy("Creeper", 100, 25)
    spitter = Enemy("Spitter", 200, 60)
    brute = Enemy("Brute", 250, 80)
    soldier = Enemy("Soldier", 100, 25)
    player.inventory.add_item(knife)
    player.inventory.add_item(handgun)
    player.inventory.add_item(shotgun)
    player.inventory.add_item(rocket_launcher)
    player.inventory.add_item(first_aid)

    enemies = [creeper, creeper, creeper, spitter, spitter, soldier, brute] #used this for randomising
    enemy = random.choice(enemies)

    print(f"\n--- Random Encounter ---")
    print(f"Captain Lucas Bennett encounters a {enemy.name}!")
    print(f"\n{enemy.name} stands ready for combat.")
    print("\nIt's time to test your skills against this formidable opponent.")
    print("Remember to switch weapons, aim, and use your combat skills effectively.")
    print("Type 'EQUIP KNIFE', 'EQUIP HANDGUN', 'EQUIP SHOTGUN', 'EQUIP ROCKETS', 'UNEQUIP', 'ATTACK', 'AIM', 'USE FIRST AID', 'RUN' or 'QUIT'.") # i'll probably get rid of this later when theres a way of viewing the list of actions
    print(f"The {enemy.name} prepares to attack!")
    print("Make your move now!")

    while player.health > 0 and enemy.health > 0:
        action = input(f"\nCaptain Lucas Bennett: ").strip().upper()

        if action == "QUIT":
            print("\nleaving for amin meu!") # update this when time
            from main import main_menu
            main_menu()
            return
        elif action == "RUN": #to be used if importing through out the game
            print(f"{player.name} runs from the {enemy.name}!")
            break
        elif action.startswith("EQUIP"):
            weapon_choice = action.split()[1].lower()
            if weapon_choice == "knife":
                player.equip_weapon(knife)
            elif weapon_choice == "handgun":
                player.equip_weapon(handgun)
            elif weapon_choice == "shotgun":
                player.equip_weapon(shotgun)
            elif weapon_choice == "rockets":
                player.equip_weapon(rocket_launcher)
            else:
                print("Invalid weapon choice!")

        elif action == "UNEQUIP":
            player.unequip_weapon()

        elif action == "ATTACK":
            if player.current_weapon:
                player.attack(enemy)
            else:
                print(f"{player.name} strikes {enemy.name}!") #check this
                player.unarmed_attack(enemy)

            if enemy.health > 0:
                enemy.attack(player)

        elif action == "AIM":
            player.aim()

        elif action == "USE FIRST AID":
            player.use_item(first_aid)
            print(f"Current health: {player.health}")

        else:
            print("Invalid command. Type 'EQUIP KNIFE', 'EQUIP HANDGUN', 'EQUIP SHOTGUN', 'EQUIP ROCKETS', 'UNEQUIP', 'ATTACK', 'AIM', 'USE FIRST AID' or 'QUIT'.")

    if player.health <= 0:
        print("Captain Lucas Benett has been defeated. Game over.")
    elif enemy.health <= 0:
        print(f"The {enemy.name} has been defeated. Well done!")

if __name__ == "__main__":
    random_encounter()
