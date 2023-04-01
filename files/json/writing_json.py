# writing_json.py
"""
Writing a JSON File
We import the json module, open up a write-mode
file under the variable json_file, and then use
the json.dump() method to write to the file.
json.dump() takes two arguments: first the data
object, then the file object you want to save.
"""

data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

import json

with open('data.json', 'w') as data_json:
  json.dump(data_payload, data_json)

