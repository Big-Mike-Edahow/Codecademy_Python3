# append.py
"""
Write to an Existing File
To write to an existing file, you must add a
parameter to the open() function:

"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content
"""

with open('cool_dogs.txt', 'a') as cool_dogs_file:
  cool_dogs_file.write('Air Buddy\n')
