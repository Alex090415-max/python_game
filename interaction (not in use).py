# def search_room(player):
#   print("You search the room...")
#   items_found = ["medkit", "ammo", "key"]
#   print(f"You found: {', '.join(items_found)}.")
#   player.inventory.extend(items_found)

# def pick_up_item(player, item):
#   if item in player.inventory:
#       print(f"You already have a {item}.")
#   else:
#       print(f"You pick up the {item}.")
#       player.inventory.append(item)

# def use_item(player, item):
#   if item in player.inventory:
#       if item == "medkit":
#           player.health += 20
#           player.inventory.remove(item)
#           print(f"You use a {item}. Health restored by 20 points.")
#       elif item == "ammo":
#           print("You replenish your ammo.")
#       elif item == "key":
#           print("You use the key.")
#       else:
#           print(f"The {item} can't be used right now.")
#   else:
#       print(f"You don't have a {item}.")

# def check_inventory(player):
#   if player.inventory:
#       print("You check your inventory:")
#       for item in player.inventory:
#           print(f"- {item}")
#   else:
#       print("Your inventory is empty.")
