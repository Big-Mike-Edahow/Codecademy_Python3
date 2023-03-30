# string_split_escape_sequence.py
"""
Newline or \n will allow us to split a multi-line
string by line breaks and \t will allow us to
split a string by tabs. \t is particularly useful
when dealing with certain datasets because it is
not uncommon for data points to be separated by
tabs.
"""

spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split('\n')
print(spring_storm_lines)
