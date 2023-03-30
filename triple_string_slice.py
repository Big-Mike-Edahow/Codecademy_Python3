# triple_string_slice.py
# Three different ways to slice the last three characters from a string

first_name = "Reiko"
last_name = "Matsuki"

"""
Using a len() statement as the starting index and
omitting the final index lets you slice n
characters from the end of a string, where n is
the amount you subtract from len()
"""
def password_generator(first_name, last_name):
  temp_password = first_name[len(first_name)-3:] + last_name[len(last_name)-3:]
  return temp_password

temp_password = password_generator(first_name, last_name)

print(temp_password)

# Slice the last three elements of the string
temporary_passwd = first_name[-3:] + last_name[-3:]

print (temporary_passwd)

# Slice from index 2 until the end of the string
# Slice from index 4 until the end of the string
# Assumes that you know the length of the string
temporary_password = first_name[2:] + last_name[4:]

print (temporary_password)
