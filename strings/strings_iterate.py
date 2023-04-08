# strings_iterate.py
"""
Because strings are lists, that means we can
iterate through a string using for or while loops.
"""
word = "Supercalifragilisticexpialidocious"

def get_length(word):
  counter = 0
  for letter in word:
    counter += 1
  return counter
print("The length of " + word + " is:")
print(get_length(word), "Characters.")

