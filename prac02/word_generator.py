__author__ = 'Donald Cull'

"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

(Another way to get just consonants would be to use string.ascii_lowercase (all letters) and remove the vowels)
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

# word_format = input("Please enter # for consonants and % for vowels:")
# while word_format.isdigit():
    # word_format = input("Please enter # for consonants and % for vowels:")
word = ""
word_size = random.randint(1, 20)
for i in range(word_size):
    word += random.choice(CONSONANTS)
    word += random.choice(VOWELS)
#for kind in word_format:
 #   if kind == "#":
    #    word += random.choice(CONSONANTS)
  #  elif kind == "%":
    #    word += random.choice(VOWELS)
   # else:
    #    word += kind

print(word)