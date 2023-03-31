# dict_add_multiple_keys.py
"""
Add Multiple Keys
If we wanted to add multiple key : value pairs to a
dictionary at once, we can use the .update() method.
.update() inserts the specified items to the dictionary.
The specified items can be a dictionary, or an
iterable object with key value pairs.
"""

user_ids = {
"teraCoder": 9018293,
"proProgrammer": 119238
}

user_ids.update({"theLooper": 138475, "stringQueen": 85739})

print(user_ids)
