#
class Creature:
    def __init__(self, name, species, power_level, speed, habitat, special_ability, weakness):
        """Initializes a creature with its attributes."""
        self.name = name
        self.species = species
        self.power_level = power_level
        self.speed = speed
        self.habitat = habitat
        self.special_ability = special_ability
        self.weakness = weakness

    def describe(self):
        """
        Prints out the details of the creature..
        
        """
     
        # print(f"Creature: {self.name}")
        print(f"Species: {self.species}")
        print(f"Power Level: {self.power_level}")
        print(f"Speed: {self.speed}")
        print(f"Habitat: {self.habitat}")
        print(f"Special Ability: {self.special_ability}")
        print(f"Weakness: {self.weakness}")
        print("-" * 30)

    def use_ability(self):
        """Uses the creature's special ability."""
        print(f"{self.name} uses {self.special_ability}!")

#
class Dragon(Creature):
    def fly(self):
        """Allows the dragon to fly."""
        print(f"{self.name} spreads its wings and takes off into the sky!")


#
class Elf(Creature):
    def stealth(self):
        """Allows the elf to become stealthy."""
        print(f"{self.name} blends into the shadows, becoming nearly invisible.")

#
class Mermaid(Creature):
    def swim(self):
        """Allows the mermaid to swim."""
        print(f"{self.name} glides effortlessly through the waves.")

#
class Golem(Creature):
    def __init__(self, name, power_level, speed):
        """Initializes a golem with specific attributes."""
        super().__init__(name, "Golem", power_level, speed, "Forests", "Earthquake Smash", "Dark Magic")

    def smash(self):
        """Allows the golem to smash the ground."""
        print(f"{self.name} slams the ground, causing a small earthquake!")

#
drake = Dragon("Drake", "Dragon", 90, 60, "Mountains", "Fire Breath", "Ice")
legolas = Elf("Legolas", "Elf", 80, 100, "Forests", "Archery Mastery", "Dark Magic")
ariel = Mermaid("Ariel", "Mermaid", 70, 80, "Oceans", "Siren Song", "Pollution")
rocky = Golem("Rocky", 95, 30)

#
drake.describe()
drake.use_ability()
drake.fly()

#
legolas.describe()
legolas.use_ability()
legolas.stealth()

#
ariel.describe()
ariel.use_ability()
ariel.swim()

#
rocky.describe()
rocky.use_ability()
rocky.smash()