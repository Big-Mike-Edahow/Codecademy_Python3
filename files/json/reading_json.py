# reading_json.py
"""
Reading a JSON File
CSV isn’t the only file format that Python has
a built-in library for. We can also use Python’s
file tools to read and write JSON. JSON, an
abbreviation of JavaScript Object Notation, is
a file format inspired by the programming language
JavaScript.

The name, like CSV is a bit of a misnomer — some
JSON is not valid JavaScript (and plenty of
JavaScript is not valid JSON).

JSON’s format is endearingly similar to Python
dictionary syntax, and so JSON files might be
easy to read from a Python developer standpoint.

Nonetheless, Python comes with a json package that
will help us parse JSON files into actual Python
dictionaries.
"""

import json

with open('message.json') as message_json:
  message = json.load(message_json)
  print(message['text'])
