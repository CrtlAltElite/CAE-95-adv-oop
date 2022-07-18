class Animal():
    acc = 9.8
    def __init__(self, name, species, legs=4):
        self.name = name
        self.species = species
        self.legs = legs
        self.random = 55
    
    def speak(self):
        print("Some Generic Animal Sound")

    def run(self):
        print("gallops")


class Dog(Animal):
    speed = 15

    def __init__(self, is_house_trained, name, species, legs=4):
        super().__init__(name, species, legs)
        self.is_housed_trained = is_house_trained
    
    def describe(self):
        print(f'The Dog has {self.speed} mph speed and {self.acc} m/s**2 \
            acceration and is a {self.species} and is housetrained {self.is_housed_trained}')

    # method overriding .. this will override the method in the parent class
    def speak(self):
        print("BAAARRKKKK!!!!!!")

mydog = Dog(True, 'Sparky', "lab", 4)
mydog.describe()
mydog.run()
mydog.speak()

print(isinstance(mydog, Animal))
print(isinstance(mydog, Dog))

class Cat(Animal):
    speed = 12

    def __init__(self, is_litter_box_trained, name, species, legs=4):
        super().__init__(name, species, legs)
        self.is_litter_box_trained = is_litter_box_trained

    def describe(self):
        print(f'The Cat has {self.speed} mph speed and {self.acc} m/s**2 \
            acceration and is a {self.species} and is litterbox trained {self.is_litter_box_trained}')    

    def speak(self):
        print("MEEEOOOOWWW")

my_cat = Cat(True, "Garfield", "Calico")
my_cat.describe()
my_cat.speak()


animals = [mydog, my_cat]

for animal in animals:
    print(animal.name)
    animal.speak()
    animal.describe()


class Mutt(Dog):
    def __init__(self,second_species, is_house_trained, name, species, legs =4):
        super().__init__(is_house_trained, name, species, legs)
        self.second_species= second_species

    def describe(self):
        print(f"The mutt is a mix of {self.species} and {self.second_species}")

tippi = Mutt("Pitbull", True, "Tippi", "Boxer")
tippi.describe()
tippi.run()
tippi.speak()



