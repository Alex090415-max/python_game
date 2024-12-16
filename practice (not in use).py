from antagonist import Enemy
from items import first_aid
from protagonist import Player
from weapons import handgun, knife, rocket_launcher, shotgun

def free_practice():
    player = Player("Captain Avery Hart", 100, 20)
    player.inventory.add_item(knife)
    player.inventory.add_item(handgun)
    player.inventory.add_item(shotgun)
    player.inventory.add_item(rocket_launcher)
    player.inventory.add_item(first_aid)
    soldier = Enemy("Creeper", 100, 25)  # make this global if you want the enemy to remain dead

    print("\n--- Training Fight Back ---")
    print("Captain Avery Hart stands ready for combat.")
    print("\nIt's time to test your skills against an opponent who fights back.")
    print("Remember to switch weapons, aim, and use your combat skills effectively.")
    print("Type 'EQUIP KNIFE', 'EQUIP HANDGUN', 'EQUIP SHOTGUN', 'EQUIP ROCKETS', 'UNEQUIP', 'ATTACK', 'AIM', 'USE FIRST AID' or 'QUIT'.")

    while player.health > 0 and soldier.health > 0:
        action = input("\nCaptain Avery Hart: ").strip().upper()

        if action == "QUIT":
            print("\nGood work, Captain. Dismissed!")
            from main import main_menu
            main_menu()
            return

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
                player.attack(soldier)
            else:
                print("No weapon equipped. Use your punch or kick!")
                player.unarmed_attack(soldier)

            if soldier.health > 0:
                soldier.attack(player)

        elif action == "AIM":
            player.aim()

        elif action == "USE FIRST AID":
            player.use_item(first_aid)
            print(f"Current health: {player.health}")

        else:
            print("Invalid command. Type 'EQUIP KNIFE', 'EQUIP HANDGUN', 'EQUIP SHOTGUN', 'EQUIP ROCKETS', 'UNEQUIP', 'ATTACK', 'AIM', 'USE FIRST AID' or 'QUIT'.")

    if player.health <= 0:
        print("Captain Avery Hart has been defeated. Game over.")
    elif soldier.health <= 0:
        print("The Creeper has been defeated. Well done!")

if __name__ == "__main__":
    free_practice()
