# R224774h Joshua Mukonyora Assignment 2 Parallel...C Prog Carry
# Question 1: Vehicle class hierarchy


class Vehicle:
    def move(self):
        return "The vehicle is moving"


class Car(Vehicle):
    def move(self):
        return "The car is driving on the road"


class Bike(Vehicle):
    def move(self):
        return "The bike is being pedaled on the track"



# Question 2: Polymorphism with shapes and total area


import math


class Shape:
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


def total_area(shapes):
    return sum(shape.calculate_area() for shape in shapes)



# Question 3: Using super() in Rectangle

class BaseShape:
    def __init__(self):
        print("Shape constructor called")

    def calculate_area(self):
        pass


class RectangleSuper(BaseShape):
    def __init__(self, width, height):
        super().__init__()  # Call BaseShape constructor
        self.width = width
        self.height = height

    def calculate_area(self):
        # Demonstrating super() usage in method
        super().__init__()
        return self.width * self.height



# Question 4: Duck typing with Dog and Cat


class Dog:
    def make_sound(self):
        return "Woof! Woof!"


class Cat:
    def make_sound(self):
        return "Meow! Meow!"


def process_sound(sound_object):
    print(sound_object.make_sound())



# Question 5: Abstract Base Class for File Handlers


from abc import ABC, abstractmethod


class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass


class TextFileHandler(FileHandler):
    def read(self):
        return "Reading text file..."

    def write(self, data):
        return f"Writing '{data}' to text file"


class BinaryFileHandler(FileHandler):
    def read(self):
        return "Reading binary file..."

    def write(self, data):
        return f"Writing {data} to binary file"



# Example Usage for All Questions

if __name__ == "__main__":
    print("=== Question 1 ===")
    v = Vehicle()
    c = Car()
    b = Bike()
    print(v.move())
    print(c.move())
    print(b.move())

    print("\n=== Question 2 ===")
    shapes = [Circle(5), Rectangle(4, 6), Circle(3)]
    print("Total area of shapes:", total_area(shapes))

    print("\n=== Question 3 ===")
    rect_super = RectangleSuper(4, 5)
    print("Rectangle area using super():", rect_super.calculate_area())

    print("\n=== Question 4 ===")
    dog = Dog()
    cat = Cat()
    process_sound(dog)
    process_sound(cat)

    print("\n=== Question 5 ===")
    text_handler = TextFileHandler()
    binary_handler = BinaryFileHandler()
    print(text_handler.read())
    print(text_handler.write("Hello World"))
    print(binary_handler.read())
    print(binary_handler.write(b'101010'))

