""" A Python program that defines an abstract Animal base class with a shared constructor and an abstract speak() method, then builds 
three child classes (Dog, Parrot, Lion) that each inherit from Animal using super(), add their own unique attribute, and 
implement speak() with their own output. Finally,  you create objects from each child class and run the sound show."""

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} is speaking")

class Dog(Animal):
    def __init__(self, name, age):
        self.age = age
        super().__init__(name)


d = Dog("Max", "4")
d.speak()