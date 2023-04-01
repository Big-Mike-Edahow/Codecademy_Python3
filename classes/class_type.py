# class_type.py
"""
Object-Oriented Programming
A class instance is also called an object.
The pattern of defining classes and creating
objects to represent the responsibilities of
a program is known as Object Oriented
Programming or OOP.

Instantiation takes a class and turns it into
an object, the type() function does the opposite
of that. When called with an object, it returns
the class that the object is an instance of.
"""

class Facade:
  pass

facade_1 = Facade()

facade_1_type = type(facade_1)
print(facade_1_type)
