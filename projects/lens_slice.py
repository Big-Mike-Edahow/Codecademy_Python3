# lens_slice.py
# Organize pizza slice sales data.

# Declare and initialize variables
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

# Count the number of $2 slices
# and print the result
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# Determine to number of pizzas
# and print the result
num_pizzas = len(toppings)
print("We sell", num_pizzas, "different kinds of pizza!")

# Create a new two dimensional list
# that contains the pizza price and
# the topping and print the list
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print(pizza_and_prices)

# Sort the list from the cheapest pizza
# to the most expensive
pizza_and_prices.sort()
cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]

# Customer bought the last slice of 
# anchovies pizza. Remove anchovies
# from the menu and add peppers
pizza_and_prices.pop()
pizza_and_prices.insert(4, [2.5, "peppers"])

# Slice the three cheapest pizza slices
# from the list for the three blind
# mice and print the result
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)