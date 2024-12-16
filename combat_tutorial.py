from antagonist import Enemy
from protagonist import Player
from weapons import handgun, knife

player = Player("Private Sarah Williams", 100, 20)

def simulated_basic_attack():
  print("\n--- Simulated Combat Training ---")
  print("Private Sarah Williams stands at attention.")
  print("Captain Carlos Torres approaches.")
  print("\nCaptain Torres: Welcome, Private Williams!")
  print("Captain Torres: Today, you will learn essential combat skills!")
  print("Captain Torres: Let's begin with the basics.")
  print("Captain Torres: In front of you is a training aid.")
  print("Captain Torres: Start by performing a punch.")  
  print("\nSarah takes a deep breath, focusing on the training aid before her.")
  print("\nCaptain Torres: You can initiate an punch by typing 'ATTACK':")

  while True:
      action = input("\nPrivate Sarah Williams: ").strip().upper()
      if action == "QUIT":
          exit_combat_tutorial()
          return
      if action == "ATTACK":
          print("------------------------------")
          print("Sarah executes a strike on the training aid!")
          print("The training aid wobbles slightly but remains standing.")
          print("\nCaptain Torres: Well done, Private Williams...")
          print("Captain Torres: I'm glad to see that you're not entirely useless!")
          simulated_strong_attack()
      else:
          print("\nCaptain Torres: That's not the correct command!") 
          print("Captain Torres: Mistakes in the field could be fatal!")
          print("Captain Torres: Type 'ATTACK' Or 'QUIT' if you've had enough!") 


def simulated_strong_attack():
  print("Captain Torres: Now, let's move on to more advanced combat techniques.")
  print("Captain Torres: To perform a more powerful attack, aim before striking.")
  print("Captain Torres: First, type 'AIM' to prepare your attack.")
  print("Captain Torres: Then, type 'ATTACK' to deliver a strong strike.")
  while True:
        action = input("\nPrivate Sarah Williams: ").strip().upper()
        if action == "QUIT":
            exit_combat_tutorial()
            return
        elif action == "AIM":
          print("\nSarah lines up ready to kick the training aid...")
          action = input("\nPrivate Sarah Williams: ").strip().upper()
          if action == "QUIT":
              exit_combat_tutorial()
              return
          elif action == "ATTACK":
            print("------------------------------")
            print("\nSarah executes a precise kick on the training aid!")
            print("Thwack! The training aid wobbles before eventually standing.")
            print("\nCaptain Torres: Good, Private Williams.")
            print("Captain Torres: Enter any command to move on to the next stage.")
            action = input("\nPrivate Sarah Williams: ").strip().upper()
            training_match()
          else:
            print("\nCaptain Torres: That's not the correct command!") 
            print("Mistakes in the field could be fatal!")
            print("Captain Torres: Type 'ATTACK' Or 'QUIT' if you've had enough!")
        else:
            print("\nCaptain Torres: That's not the correct command!") 
            print("Captain Torres: Mistakes in the field could be fatal!")
            print("Captain Torres: Type 'ATTACK' Or 'QUIT' if you've had enough!")

def training_match():  
  soldier = Enemy("Private Lamar Washington", 100, 25)

  print("\n--- Simulated Training Match ---")
  print("Private Sarah Williams stands at attention, waiting instructions.")
  print("Captain Carlos Torres approaches, his expression serious and focused.")
  print("\nCaptain Torres: Private Williams, you’ve shown promise in your training.")
  print("Captain Torres: But now it's time to put those skills to the test.")
  print("Captain Torres: You will be facing another soldier in a combat scenario.")
  print("\nSarah's heart pounds in her chest.")
  print("\nCaptain Torres: This will not be simple. Your opponent will fight back.")
  print("Captain Torres: Remember your training. Stay focused and use your training.")
  print("Captain Torres: Private Lamar Washington, step forward!")
  print("\nPrivate Washington strides confidently into the ring, smirking.")
  print("\nPrivate Lamar Washington: You ready for this, Williams?")
  print("Private Lamar Washington: I'm not going to go easy on you.")
  print("\nCaptain Torres: Alright, soldiers...")
  print("Captain Torres: Begin!")     # quitting here may not work!

  while player.health > 0 and soldier.health > 0:      
    action = input("\nPrivate Sarah Williams: ").strip().upper()      
    if action == "QUIT":
        exit_combat_tutorial()
        return
    if action == "AIM":
          print("\nSarah lines up ready to kick the training aid...") #check this fixes it!
          action = input("\nPrivate Sarah Williams: ").strip().upper()
          if action == "QUIT":
              exit_combat_tutorial()
              return
    elif action == "ATTACK":
        player.attack(soldier)
        if soldier.health > 0:
            soldier.attack(player)
    else:
        print("Private Washington dodges your attack!")
        if soldier.health > 0:
          soldier.attack(player)
  if player.health <= 0: # This needs fixing because it says you are dead!
    print("You lost: Enter any command to continue...")
    action = input("\nPrivate Sarah Williams: ").strip().upper()
    print("------------------------------")
    print("Private Sarah Williams staggers back, exhausted and defeated.")
    print("Captain Carlos Torres steps forward, with a concerned expression.")    
    print("\nCaptain Torres: Private Williams, you gave a good effort")
    print("Captain Torres: But in the field, defeat is fatal.")
    print("Captain Torres: Your opponent will not show mercy.")
    print("Captain Torres: So you cannot afford mistakes.")   
    print("\nSarah listens, her face reflecting the weight of his words.")    
    print("\nCaptain Torres: Train harder and focus more!")
    print("Captain Torres: This training is designed to prepare you for real combat")
    print("Captain Torres: Learn from this experience, and come back stronger.")    
    print("\nSarah nods, determination replacing the defeat in her eyes.")    
    print("\nCaptain Torres: Good. Now, take some time to recover.")
    print("Captain Torres: I expect to see improvement. Dismissed.")
    print("\nEnter any command to move on to the next stage.")
    action = input("\nPrivate Sarah Williams: ").strip().upper()
    combat_knife_training()


def combat_knife_training():
    print("\n--- Combat Knife Training ---")
    player.inventory.add_item(knife)
    print("Private Sarah Williams stands ready")
    print("Captain Carlos Torres approaches, his expression stern and focused.")
    print("\nCaptain Torres: Private Williams, the combat knife is an essential tool.")
    print("Captain Torres: It’s not just a weapon, but a versatile tool for survival.")
    print("Captain Torres: Today, you will learn the basic techniques.")
    print("\nSarah nods, her determination clear in her eyes.")
    print("\nCaptain Torres: Let's begin with a basic attack.")
    print("Captain Torres: First, type 'EQUIP KNIFE!' to ready your combat knife.")
    print("Captain Torres: Or type 'QUIT' if you've had enough!")
    
    while True:
      action = input("\n").strip().upper()
      if action == "QUIT":
        exit_combat_tutorial()
        return
      if action.startswith("EQUIP"):
          weapon_choice = action.split()[1].lower()
          if weapon_choice == "knife":
              player.equip_weapon(knife)
              print("\nCaptain Torres: Now, ATTACK the training aid!")
              while True:
                  action = input("\n").strip().upper()
                  if action =="QUIT":
                      exit_combat_tutorial()
                      return   
                  if action == "ATTACK":
                      # needs descriptive text here
                      print("Sarah strikes the training aid with her combat knife!")
                      print("The training aid wobbles slightly but remains standing.")
                      print("\nCaptain Torres: Well done, Private Williams!")
                      print("Captain Torres: You're getting the hang of this!")
                      print("Captain Torres: Maybe you're ready for a firearm.")
                      firearm_basic_training()
                      return
                  else:
                    print("\nCaptain Torres: That's not the correct command!") 
                    print("Captain Torres: Mistakes in the field could be fatal!")
                    print("Captain Torres: Type 'ATTACK' Or 'QUIT' if you've had enough!")
          else:
              print("\nCaptain Torres: That's not the correct command!") 
              print("Captain Torres: Mistakes in the field could be fatal!")
              print("Captain Torres: Type 'EQUIP KNIFE' Or 'QUIT' if you've had enough!")
      else:
          print("\nCaptain Torres: That's not the correct command!") 
          print("Captain Torres: Mistakes in the field could be fatal!")
          print("Captain Torres: Type 'EQUIP KNIFE' Or 'QUIT' if you've had enough!")


def firearm_basic_training(): # error handling not working
    player.inventory.add_item(handgun)
    print("\n--- Firearm Basic Training ---")
    print("Captain Torres: Now, let's move on to the next stage.")
    print("Captain Torres: A firearm requires precision and control.")
    print("Captain Torres: First, equip the handgun by typing 'EQUIP HANDGUN'.")
    print("Captain Torres: Or type 'QUIT' if you need a break.")  

    while True:
        action = input("\n").strip().upper()
        if action == "QUIT":
          exit_combat_tutorial()
          return
        if action.startswith("EQUIP"):
          weapon_choice = action.split()[1].lower()
          if weapon_choice == "handgun":
              player.equip_weapon(handgun)
              print("\nCaptain Torres: Now, let's see you shoot!")
              print("Captain Torres: You can also AIM to prepare your attack, Private")
              while True:
                  action = input("\n").strip().upper()
                  if action == "QUIT":
                      exit_combat_tutorial()
                      return
                  if action == "ATTACK":
                      print("Sarah aims carefully and fires at the target!")
                      print("The shot rings out, hitting the target squarely.")
                      print("\nCaptain Torres: Excellent shot, Private Williams!")
                      print("Captain Torres: You're ready for the next challenge!")
                      practice_weapon_switching()
                      return
                  elif action == "AIM": #currently broken
                    player.aim()   
                    print("Sarah stares down the barrel of the handgun.")
                    print("Sarah: I'm ready to fire!")
                    print("\nCaptain Torres: Good, now type 'ATTACK' to fire!")
                  else:
                    print("Captain Torres: That's not the correct command!")
                    print("Captain Torres: Mistakes in the field could be fatal!")
                    print("Captain Torres: Type 'ATTACK' Or 'QUIT' if you've had enough!")
          else:
            print("\nCaptain Torres: That's not the correct command!") 
            print("Captain Torres: Mistakes in the field could be fatal!")
            print("Captain Torres: Type 'AIM' to aim or 'ATTACK' to fire, or 'QUIT' if you've had enough!")
        else:
            print("\nCaptain Torres: That's not the correct command!") 
            print("Captain Torres: Mistakes in the field could be fatal!")
            print("Captain Torres: Type 'EQUIP HANDGUN' or 'QUIT' if you've had enough!")
    
    
def practice_weapon_switching():
    # player.inventory.add_item(knife)
    # player.inventory.add_item(handgun)
    dummy = Enemy("Training aid", 100, 0)
    player.unequip_weapon()
    print("\n--- Weapon Switching Practice ---")
    print("Private Sarah Williams stands ready, waiting for her final training lesson.")
    print("Captain Carlos Torres approaches, holding a stern yet encouraging expression.")
    print("\nCaptain Torres: Private Williams, your final lesson is to practice switching between your weapons.")
    print("Captain Torres: You can also unequip your weapon and fight using punches and kicks.")
    print("Captain Torres: Type 'EQUIP KNIFE', 'EQUIP HANDGUN', 'UNEQUIP', 'ATTACK', 'AIM', or 'QUIT' to return to the main menu.")
    print("Captain Torres: Show me your proficiency with each of these skills.")
    
    while True:
      action = input("\nPrivate Sarah Williams: ").strip().upper()
    
      if action == "QUIT":
          print("\nCaptain Torres: Good work, Private. Dismissed!")
          exit_combat_tutorial()
          return
      elif action.startswith("EQUIP"):
          weapon_choice = action.split()[1].lower()
          if weapon_choice == "knife": #was coming up invalid (probbaly because of capitalising Knife)
              player.equip_weapon(knife)
          elif weapon_choice == "handgun":
              player.equip_weapon(handgun)
          else:
              print("Invalid weapon choice!")
    
    
      elif action == "UNEQUIP":
          player.unequip_weapon()
    
      elif action == "ATTACK":
          if player.current_weapon:
              player.attack(dummy)
              if dummy.health <= 0: #Note to self: this isn't working
                exit_combat_tutorial()
                return             
          else:
              print("No weapon equipped. Use your punch or kick!")
              player.unarmed_attack(dummy)
    
      elif action == "AIM": #not currently working! (doens't add damage to kick)(works for handgun)
          player.aim()    
      else:
          print("Invalid command. Type 'EQUIP KNIFE', 'EQUIP HANDGUN', 'UNEQUIP', 'ATTACK', 'AIM', or 'QUIT'.")
    
def exit_combat_tutorial():
    from tutorial import basic_training
    basic_training()

if __name__ == "__main__":
    from tutorial import basic_training
    basic_training()


