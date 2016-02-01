"""
CP1404/CP5632 workshop code, starting point
Random word generator - based on format of words

Could use string.ascii_lowercase to get all letters (and remove vowels to get just consonants)
"""
import random

__author__ = 'Lindsay Ward'

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

word_format = "ccvc"
word = ""
for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)

print(word)
