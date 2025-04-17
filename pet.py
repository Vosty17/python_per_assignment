class pet:
    def __init__(self, name, hunger, energy, happiness):
        self.name = name
        self.hunger = hunger
        self.energy = energy
        self.happiness = happiness

    def eat(self):
        self.hunger -= 1  # Modify the hunger attribute of the object
        return self.hunger
