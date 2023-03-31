# streaming_service.py
"""
Using a dict comprehension, create a dictionary called
plays that goes through zip(songs, playcounts) and
creates a song:playcount pair for each song in songs
and each playcount in playcounts.
"""

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {song:playcount for [song, playcount] in zip(songs, playcounts)}

plays["Respect"] = 94
plays["Purple Haze"] = 1

"""
Create a dictionary called library that has two
key: value pairs.
key "The Best Songs" with a value of the plays dict
key "Sunday Feelings" with a value of an empty dict
"""
library = {"The Best Songs": plays, "Sunday Feelings": {}}

print(library)
