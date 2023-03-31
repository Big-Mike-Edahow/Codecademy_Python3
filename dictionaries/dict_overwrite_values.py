# dict_overwrite_values.py
"""
If we use a key that already has an entry in the
dictionary, our value assignment would overwrite
the existing value attached to that key.
"""

oscar_winners = {
"Best Picture": "La La Land",
"Best Actor": "Casey Affleck",
"Best Actress": "Emma Stone",
"Animated Feature": "Zootopia"
}

oscar_winners["Supporting Actress"] = "Viola Davis"
oscar_winners["Best Picture"] = "Moonlight"

print(oscar_winners)
