__author__ = 'Donald Cull'
VOWELS = "aeiou"
name = input("what is your name: ")
vowel_count = 0
for vowel in name:
    if vowel in VOWELS:
        vowel_count += 1
length_name = len(name)
print("Out of {} letters, {} has {} vowels".format(length_name, name, vowel_count))

