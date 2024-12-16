from items import first_aid
from protagonist import Player


def inventory_tutorial():
    player = Player("Private Emma Hoffman", 25, 20)
    print("Welcome to the Inventory Management Tutorial!")

    # Add the first_aid item to the inventory
    print("\nAdding a First aid to your inventory...")
    player.inventory.add_item(first_aid)

    # List items in the inventory
    print("\nCurrent inventory:")
    player.inventory.list_items()

    # Dr. Maria Bauer as the instructor guiding Emma
    print("\nDr. Maria Bauer: Private Hoffman, today you'll learn how to manage your medical inventory.")
    print("Dr. Maria Bauer: We'll start by adding a First Aid Kit to your inventory.")
    print("Dr. Maria Bauer: Your current health is 25. Let's practice using the First Aid Kit to restore your health.")
    print("Dr. Maria Bauer: Remember, managing your supplies effectively is crucial in emergency situations.")

    # Hint at the secret facility
    print("Dr. Maria Bauer: In this facility, we handle situations that are... highly classified. Your discretion and attention to detail are paramount.")

    # Input loop to practice using the First Aid Kit
    while player.health < 100:
        action = input("\nType 'USE FIRST AID' to use the First Aid Kit or 'QUIT' to exit: ").strip().upper()
        if action == "QUIT":
            print("\nDr. Maria Bauer: Good job, Private Hoffman. Tutorial completed!")
            break
        elif action == "USE FIRST AID":
            player.use_item(first_aid)
            print(f"Current health: {player.health}")
        else:
            print("Invalid command. Please type 'USE FIRST AID' or 'QUIT'.")

    if player.health >= 100:
        print("\nDr. Maria Bauer: Excellent! Your health is now full. Well done, Private Hoffman!")
        print("\nDr. Maria Bauer: As a recent graduate who topped her class, your quick thinking and problem-solving skills are commendable.")
        print("\nDr. Maria Bauer: Here, in this undisclosed location, we face challenges that the outside world could hardly imagine. Your skills will be put to the test.")
        player.inventory.list_items()

if __name__ == "__main__":
    inventory_tutorial()
