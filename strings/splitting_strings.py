# splitting_strings.py
"""
If we provide an argument for .split() we can
dictate the character we want our string to be
split on. This argument should be provided as
a string itself.
"""

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

# Split the string on the commas
author_names = authors.split(',')

print(author_names, "\n")

# Split the author name on the space between
# the first and last names, then append the
# last name to the new list author_last_name
author_last_names = []
for name in author_names:
  author_last_names.append(name.split()[-1])
  
print(author_last_names)
