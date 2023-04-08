# shipping.py
# Take the weight of a package and determine
# the cheapest way to ship that package using
# Sal’s Shippers.

# Varible declarations
weight = 41.5
cost_ground = 0
cost_ground_premium = 125
cost_drone = 0

# Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3 + 20
elif weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75

# Print the Ground Shipping costs
print("Ground Shipping Premium $", cost_ground_premium)
print("Ground Shipping =", cost_ground)

# Drone Shipping
if weight <= 2:
  cost_drone = weight * 4.5
elif weight <= 6:
  cost_drone = weight * 9
elif weight <= 10:
  cost_drone = weight * 12
else:
  cost_drone = weight * 14.25

# Print the Drone Shipping costs
print("Drone Shipping =", cost_drone)