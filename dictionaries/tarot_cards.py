# tarot_cards.py
"""
We have provided a pack of tarot cards, tarot. You are going
to do a three card spread of your past, present, and future.
"""

tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"The Strength", 9:	"The Hermit", 10:	"The Wheel of Fortune", 11:	"The Justice", 12:	"The Hanged Man", 13:	"The Death", 14:	"The Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"The Judgement", 21:	"The World", 22: "The Fool"}

spread = {}

spread["past"] = tarot.pop(1)
spread["present"] = tarot.pop(12)
spread["future"] = tarot.pop(21)

for key, value in spread.items():
  print("Your "+key+" is "+value+" card. ")
