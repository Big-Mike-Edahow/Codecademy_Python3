# magic8.py
# Python program that can answer any
# “Yes” or “No” question with a
# different fortune each time it
# executes.

# import the random module
import random

# variable declarations
name = "Joe"
question = "Will I be successful today?"
answer = ""
random_number = random.randint(1, 11)

# Check whether or not we're getting
# random numbers
# print(random_number)

# The Magic 8-Ball's fortune-telling 
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtfull"
elif random_number == 10:
  answer = "Too bad so sad"
elif random_number == 11:
  answer = "Hit the road, Jack"
else:
  answer = "Error"

# Output the results
if name == "":
  print(question)
if len(question) == 0:
  print("The Magic-8 Ball cannot provide a forturne unless you ask it something.") 
else:
  print(name, "asks:", question)
  print("Magic 8-Ball's answer:", answer)