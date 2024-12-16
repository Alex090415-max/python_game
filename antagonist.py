class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        print(f"\n{self.name}: Attacks {target.name} for {self.attack_power} damage!!!")
        target.take_damage(self.attack_power)

    def take_damage(self, damage, increased=False):
        if isinstance(damage, (int, float)): # check this at a later point! (or try running it without it)
            actual_damage = damage
        else:
            actual_damage = damage.calculate_damage(increased)

        self.health -= actual_damage
        print(f"{self.name} takes {actual_damage} damage! Current health: {self.health}")
        if self.health <= 0:
            print(f"{self.name} has been defeated!")        
