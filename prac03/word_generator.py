__author__ = 'Donald Cull'

"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

(Another way to get just consonants would be to use string.ascii_lowercase (all letters) and remove the vowels)
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def is_valid_format():
    word_format = input("Please enter # for consonants and % for vowels:")
    for char in word_format:
        if char != "c" or char != "v":
            return false
        else:



is_valid_format()
word = ""
#word_size = random.randint(1, 20)
#for i in range(word_size):
 #   word += random.choice(CONSONANTS)
  #  word += random.choice(VOWELS)
for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    elif kind == "v":
        word += random.choice(VOWELS)


print(word)