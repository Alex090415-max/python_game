from combat_tutorial import simulated_basic_attack
from inventory_tutorial import inventory_tutorial

#NOTE: there is an error in the code during the aim handgun - moved to combat_tutorial.py

def basic_training():
  while True:
    print("\n--- Basic Training ---")
    print("1. Survival Basics")
    print("2. Combat Training")
    print("3. Return to Main Menu")
    print("\nEnter your choice...(1, 2 or 3): ")   

    
    choice = input("\n").strip()
    if choice == "1":
      inventory_tutorial()
    elif choice == "2":
      simulated_basic_attack()
    elif choice == "3":
        from main import main_menu
        main_menu()
      
    else:
      print("Invalid choice. Please try again.")



  













