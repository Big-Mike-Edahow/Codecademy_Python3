# join.py
"""
.join() joins a list of strings together with a
given delimiter.

The syntax of .join() is:
'delimiter'.join(list_you_want_to_join)
"""

reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = ' '.join(reapers_line_one_words)
reapers_line_one += '.'

print(reapers_line_one)
