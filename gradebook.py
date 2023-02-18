# gradebook.py
# Organize your subjects and grades using Python

# Declare and initialize list
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

# Add computer science and visual arts to the gradebook
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

# Manipulate the values of the grades
gradebook[5][1] = 98
gradebook[2].remove(85)
gradebook[2].append("Pass")

# Add last semester's gradebook to this semester's gradebook
# to get the full year's gradebook and print the results
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)