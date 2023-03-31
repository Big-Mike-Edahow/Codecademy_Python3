# dict_get.py
"""
.get() returns the value of the item with the specified key.
If the key you are trying to .get() does not exist, it will return None by default.
"""

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder", 100000)
stack_id = user_ids.get("superStackSmash", 100000)
not_there_id = user_ids.get("SuperMario")

print(tc_id)
print(stack_id)
print(not_there_id)
