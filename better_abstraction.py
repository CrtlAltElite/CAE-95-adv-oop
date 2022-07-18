from abc import ABC, abstractmethod

class Duck(ABC):

    def swim(self):
        print("Float in pond")

    @abstractmethod
    def display(self):
        pass

class Quackable(ABC):
    def quack():
        print("quack")

class Flyable(ABC):
    def fly():
        print("flap flap flap")


class DecoyDuck(Duck):
    def display(self):
        print("I am a Decoy")

class Rubberduck(Duck, Quackable):

    def display(self):
        print("I am a rubber Ducky")

    def quack(self):
        print("squeak!")

class RedHead(Duck, Flyable, Quackable):
    def display(self):
        print("I am a redheaded Duck")

class Mallard(Duck, Flyable, Quackable):
    def display(self):
        print("I am  a Mallard")

## Head First Design Patterns (OReilly) Eric Freeman