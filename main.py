from practice import random_encounter
from tutorial import basic_training

print("Welcome to the Game!")

def main_menu():
    while True:
        print("\n--- Main Menu ---")
        # print("0. Prelude")
        print("1. Story Mode")
        print("2. Basic Training")
        print("3. Quit")
        print("x. Free Practice") # this is to be used for testing purposes or move into Basic Training        
        print("\nEnter your choice...(1, 2 or 3): ")
        choice = input("\n").strip()
        # if choice == "0":
        #     start_prelude()
        if choice == "1":
            start_game()
        elif choice == "2":
            basic_training()
        elif choice == "3":
            quit_game()
        elif choice == "x":
            random_encounter()
        else:
            print("Invalid choice. Please try again.")

def start_game():
    print("Starting the game...")     

def quit_game():
    print("Exiting the game. Goodbye!")
    exit()

if __name__ == "__main__":
    main_menu()
