# everything_is_an_object.py
"""
Everything is an Object
Attributes can be added to user-defined objects after instantiation, so it’s possible for an object to have some attributes that are not explicitly defined in an object’s constructor. We can use the dir() function to investigate an object’s attributes at runtime. dir() is short for directory and offers an organized presentation of object attributes.

Python automatically adds a number of attributes to all objects that get created. These internal attributes are usually indicated by double-underscores. But sure enough, attribute is in that list.
"""

print(dir(5))

def this_function_is_an_object(num):
  return "Cheese is {} times better than everything else".format(num)

print(dir(this_function_is_an_object))
