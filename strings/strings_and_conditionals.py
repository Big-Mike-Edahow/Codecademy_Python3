# strings_and_conditionals.py
# in checks if one string is part of another string.

# Returns true if letter is in word
def letter_check(word, letter):
  for character in word:
    if character == letter:
      return True
  return False

# Returns True if little string is in big string
def contains(big_string, little_string):
  return little_string in big_string

# Creates a new list of letters in comon to both strings
def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common

print(letter_check("Idaho", 'a'))

print(contains("I wish I was a Klondike Bar", "I wish I was a"))

print(common_letters("Mary had a little lame", "Peter picked a peck of pickled peppers"))
