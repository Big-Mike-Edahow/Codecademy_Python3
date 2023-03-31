# dict_get_all_values.py
"""
Dictionaries have a .values() method that returns a dict_values
object (just like a dict_keys object but for values!) with all
of the values in the dictionary. It can be used in the place of
a list for iteration:
 
for score_list in test_scores.values():
  print(score_list)
"""

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0

for exercises in num_exercises.values():
  total_exercises += exercises
print("Total exercises:",total_exercises)
