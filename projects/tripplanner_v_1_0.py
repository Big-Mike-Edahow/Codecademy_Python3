# tripplanner_v_1_0.py

def trip_planner_welcome(name): 
  print("Welcome to tripplanner v1.0 " + name + "\n")

trip_planner_welcome("Mike")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate = estimated_time_rounded(2.43)

def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
  print("Your trip starts off in " + origin)
  print("And you are traveling to " + destination + "\n")
  print("You will be traveling by " + mode_of_transport)
  print("It will take approximately " + str(estimated_time) + " hours")


destination_setup("Blackfoot", "American Falls", estimate, "Car")