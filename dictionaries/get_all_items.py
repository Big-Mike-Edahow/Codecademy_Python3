# get_all_items.py
"""
You can get both the keys and the values with the .items() method.
Like .keys() and .values(), it returns a dict_list object. Each
element of the dict_list returned by .items() is a tuple consisting of:
(key, value)
"""

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for occupation, percentage in pct_women_in_occupation.items():
  print("Women make up " + str(percentage) + " percent of " + occupation + "s.") 
  