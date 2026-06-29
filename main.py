""" A Python program that defines an abstract Animal base class with a shared constructor and an abstract speak() method, then builds 
three child classes (Dog, Parrot, Lion) that each inherit from Animal using super(), add their own unique attribute, and 
implement speak() with their own output. Finally,  you create objects from each child class and run the sound show."""

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def __init__(self, age, name):
        self.age = age
        super().__init__(name)

    def speak(self):
        print(f"{self.name} is speaking.")

class Parrot(Animal):
    def __init__(self, age, name):
        self.age = age
        super().__init__(name)

    def speak(self):
        print(f"{self.name} is speaking.")

class Lion(Animal):
    def __init__(self, age, name):
        self.age = age
        super().__init__(name)

    def speak(self):
        print(f"{self.name} is speaking.")


d = Dog("4", "Max")
d.speak()

p = Parrot("3", "Ruby")
p.speak()

l = Lion("4", "Mufasa")
l.speak()