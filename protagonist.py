from inventory import Inventory


class Player:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        self.inventory = Inventory()  # Unified inventory for all items (initially had weapons and first aid seperate)
        self.current_weapon = None
        self.aiming = False

    def equip_weapon(self, weapon):
        if weapon in self.inventory.items:
            self.current_weapon = weapon
            print(f"{self.name} has equipped the {weapon.name}.")
        else:
            print(f"{self.name} doesn't have the {weapon.name} in their inventory.")

    def unequip_weapon(self):
        if self.current_weapon:
            print(f"{self.name} has unequipped the {self.current_weapon.name}.")
            self.current_weapon = None
        else:
            print(f"{self.name} has no weapon equipped.")

    def attack(self, target):
        if self.current_weapon:
            if self.aiming:
                print(f"{self.name} aims and attacks {target.name} with {self.current_weapon.name} for increased damage!")
                if self.current_weapon.use_weapon():
                    target.take_damage(self.current_weapon, increased=True)
                    self.aiming = False
            else:
                print(f"{self.name} attacks {target.name} with {self.current_weapon.name}.")
                if self.current_weapon.use_weapon():
                    target.take_damage(self.current_weapon)
        else:
            if self.aiming:
                self.strong_strike(target)
                self.aiming = False
            else:
                self.unarmed_attack(target)

    def unarmed_attack(self, target):
        damage = self.strength * 0.5
        print(f"\n{self.name} punches {target.name}.")
        target.take_damage(damage)

    def strong_strike(self, target):
        damage = self.strength
        print(f"\n{self.name} executes a precise kick on {target.name}!")
        target.take_damage(damage)

    def aim(self):
        if self.current_weapon and self.current_weapon.name in ["Handgun", "Shotgun", "Rocket launcher"]: #if you change the capitalisation, don't forget this otherwise it breaks!
            self.aiming = True
            print(f"{self.name} is aiming with the {self.current_weapon.name} for the next attack.")
        elif not self.current_weapon:
            self.aiming = True
            print(f"\n{self.name} lines up for a forceful kick...")
        else:
            print("AIM is only available for handgun, shotgun, rocket launcher, or unarmed attacks!")

    def reload(self):  # Doesn't work at the moment! Come back at a later point
        if self.current_weapon:
            self.current_weapon.reload()
        else:
            print(f"{self.name} has no weapon equipped!")

    def check_ammo(self):
        if self.current_weapon and self.current_weapon.magazine_capacity:
            print(f"Current ammo for {self.current_weapon.name}: {self.current_weapon.current_ammo}/{self.current_weapon.magazine_capacity}")
        else:
            print(f"{self.name} has no weapon equipped or the weapon doesn't use ammo.")

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage! Current health: {self.health}")
#        if self.health <= 0:
#            print(f"{self.name} YOU ARE DEAD!") This is probably not needed and causes duplication

    def use_item(self, item):
        if item in self.inventory.items:
            if item.name == "First Aid Kit":
                needed_health = 100 - self.health #players will always need to have 100 health starting point or else this breaks
                actual_heal = min(item.value, needed_health)
                self.health += actual_heal
                print(f"{self.name} used {item.name} and restored {actual_heal} health points. Current health: {self.health}.")
                self.inventory.remove_item(item)
            else:
                print(f"{self.name} cannot use {item.name}.")
        else:
            print(f"{self.name} does not have {item.name} in the inventory.")


