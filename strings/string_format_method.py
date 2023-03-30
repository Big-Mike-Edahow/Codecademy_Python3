# string_format_method.py
"""
.format() takes variables as an argument
and includes them in the string that it is
run on. You include {} marks as placeholders
for where those variables will be imported.
"""

title = "A lovely day"
poet = "Mike Jackson"

def poem_title_card(title, poet):
  poem_desc = "The poem \"{}\" is written by {}.".format(title, poet)
  return poem_desc

poem = poem_title_card(title, poet)
print(poem)
