__author__ = 'Donald Cull'

my_words = {}
phrase = input("Enter a phrase: ").split()
for word in phrase:
    if word in my_words:
        my_words[word] += 1
    else:
        my_words[word] = 1
longest_word_length = max(len(word) for word in my_words)
sorted(my_words)
for key, value in my_words.items():
    print("{1:{0:}}: {2}".format(longest_word_length, key, value))

# keys = MY_WORDS.keys()
# print(keys)

# print(MY_WORDS.items())