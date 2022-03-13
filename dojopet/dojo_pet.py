from ast import walk


class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treat = treats
        self.pet_food = pet_food
        
    def walk(self):
        self.pet.play()
        return self
    def feed(self):
        self.pet.eat()
        return self
    def bathe(self):
        self.pet.noise()
        return self
                    
class Pet:
    def __init__(self, name, type, trick):
        self.name = name
        self.type = type
        self.trick = trick
        self.health = 0
        self.energy = 0
        
    def sleep(self):
        self.energy += 25
        return self
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"Energy:{self.energy}")
        return self
    def play(self):
        self.health += 5
        print(f"Health:{self.health}")
        return self
    def noise(self):
        print(f"{self.name} like's what you are doing!! guau guau")
        return self
        
        
luke = Pet("Luke","Dog","get's the ball")
alex = Ninja("Alex", "Rodriguez", "candy", "steak", luke)

alex.feed().feed().walk().walk().bathe()

