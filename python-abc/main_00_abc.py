#!/usr/bin/env python3
from task_00_abc import Animal, Dog, Cat

bobby = Dog()
garfield = Cat()

print(bobby.sound())  # Output: Bark
print(garfield.sound())  # Output: Meow

try:
    animal = Animal()
    print(animal.sound())
except TypeError as e:
    print(e)  # Output: Can't instantiate abstract class Animal with abstract method sound

