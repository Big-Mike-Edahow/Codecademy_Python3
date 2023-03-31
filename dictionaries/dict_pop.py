# dict_pop.py
"""
.pop() removes the specified item from the dictionary.
The return value of .pop() is the value of the key removed.
"""

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

print(available_items, "\n")
print("Health points:", health_points)
