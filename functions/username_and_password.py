# username_and_password.py
"""
The username should be a slice of the first three letters of
their first name and the first four letters of their last name.
If their first name is less than three letters or their last name
is less than four letters it should use their entire names.
"""
"""
for the temporary password, they want the function to take the
input user name and shift all of the letters by one to the right,
so the last letter of the username ends up as the first letter
and so forth. For example, if the username is AbeSimp, then the
temporary password generated should be pAbeSim.
"""

first_name = "Mike"
last_name = "Jackson"

def username_generator(first_name, last_name):
    if len(first_name) < 3:
        user_name = first_name
    else:
        user_name = first_name[0:3]
    if len(last_name) < 4:
        user_name += last_name
    else:
        user_name += last_name[0:4]
    return user_name
  
    
def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password

user_name = username_generator(first_name, last_name)
password = password_generator(user_name)

print("first name:", first_name)
print("last name:", last_name, "\n")

print("username:", user_name)
print("password:", password)
