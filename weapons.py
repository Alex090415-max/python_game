class Weapon:
    def __init__(self, name, action, base_damage, magazine_capacity=None, total_magazines=None):
        self.name = name
        self.action = action
        self.base_damage = base_damage
        self.magazine_capacity = magazine_capacity
        self.total_magazines = total_magazines
        self.current_ammo = magazine_capacity if magazine_capacity is not None else 0  # Starts full or at zero if no magazine

    def use_weapon(self):
        if self.magazine_capacity:
            if self.current_ammo > 0:
                self.current_ammo -= 1 # check this error
                print(f"You use the {self.name}. {self.action}")
                print(f"Current ammo: {self.current_ammo}/{self.magazine_capacity}")
            else:
                print(f"\nThe {self.name} is out of ammo! Reload first!")
                return False
        else:
            print(f"You use the {self.name}. {self.action}")
        return True

    def reload(self): # not working at the moment
        if self.total_magazines and self.total_magazines > 0: #Note to self chekc thid
            self.total_magazines -= 1 #check this
            self.current_ammo = self.magazine_capacity
            print(f"{self.name} reloaded. Total magazines left: {self.total_magazines}")
        else:
            self.current_ammo = 0  # checks current ammo is zero if no magazines are left
            print(f"No more magazines left for the {self.name}!")

    def calculate_damage(self, increased=False):
        damage = self.base_damage
        # if self.magazine_capacity: #I think this is now obsolate
        #     damage += self.current_ammo  # check this
        if increased:
            damage *= 2  # Double the damage if aiming
        return damage

# Define specific weapons with distinct base damage values
knife = Weapon("Knife", "You attack with a swift, sharp stab!", base_damage=5)
handgun = Weapon("Handgun", "Bang!", base_damage=20, magazine_capacity=7, total_magazines=5)
shotgun = Weapon("Shotgun", "Boom!", base_damage=60, magazine_capacity=2, total_magazines=3)
rocket_launcher = Weapon("Rocket launcher", "KABOOM!", base_damage=500, magazine_capacity=1, total_magazines=2)

# use a dictionary to store the weapons?
# weapons = {
#     "knife": knife,
#     "handgun": handgun,
#     "shotgun": shotgun,
#     "rocket launcher": rocket_launcher
# }
