# with_explained.py
"""
The with keyword invokes something called a context
manager for the file that we’re calling open() on.
This context manager takes care of opening the file
when we call open() and then closing the file after
we leave the indented block.
"""

with open('fun_file.txt') as close_this_file:

  setup = close_this_file.readline()
  punchline = close_this_file.readline()

  print(setup)
