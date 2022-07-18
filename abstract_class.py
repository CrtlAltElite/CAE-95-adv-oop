from abc import ABC, abstractmethod

class Animal(ABC):
    acc = 9.8
    def __init__(self, name, species, legs=4):
        self.name = name
        self.species = species
        self.legs = legs
        self.random = 55
    
    @abstractmethod
    def speak(self):
        # print("Some Generic Animal Sound")
        pass

    # @abstractmethod
    def run(self):
        print("Animal Moves")
        # pass

class Dog(Animal):
    speed = 15
    def __init__(self, is_house_trained, name, species, legs=4):
        super().__init__(name, species, legs)
        self.is_housed_trained = is_house_trained

    def speak(self):
        print("BBARRRRKKK!!!!!")

    def run(self):
        print("gallops on legs")


nala = Dog(True, "Nala", "Black Lab")
nala.speak()
nala.run()
