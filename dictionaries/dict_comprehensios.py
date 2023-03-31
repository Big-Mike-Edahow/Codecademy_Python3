# dict_comprehensios.py
"""
Python allows dictionary comprehensions.

Dictionary comprehension is a concise and
readable way to create dictionaries in
Python. It provides a way to create a new
dictionary from an iterable object like a
list, tuple, or set.

We can create dictionaries using simple
expressions. A dictionary comprehension
takes the form:

{key: value for (key, value) in iterable}
"""

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key: value for key, value in zipped_drinks}

print(drinks, "\n")
print(caffeine, "\n")
print(drinks_to_caffeine)
