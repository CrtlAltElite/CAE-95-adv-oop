from abc import abstractmethod


from abc import ABC, abstractmethod

class Duck(ABC):
    def swim(self):
        print("float in pond")

    def quack(self):
        print("Quack")

    def fly(self):
        print("flap flap flap")

    @abstractmethod
    def display(self):
        pass

class Mallard(Duck):
    def display(self):
        print("I am a Mallard")

class RedHead(Duck):
    def display(self):
        print("I am a Read Headed Duck")

class RubberDuck(Duck):
    def quack(self):
        print("Squeak")
    
    def display(self):
        print("I am a Rubber Ducky!")

    def fly(self):
        pass

class DecoyDuck(Duck):

    def quack(self):
        pass
    
    def display(self):
        print("I am a decoy")

    def fly(self):
        pass

