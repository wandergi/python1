# implementing classes on a project i.e. parent class and child class
class Animal:
    def speak(self):
        print("Animal is speaking")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


class Cat(Animal):
    def meow(self):
        print("Cat is meowing")


d = Dog()
d.bark()

c = Cat()
c.meow()
