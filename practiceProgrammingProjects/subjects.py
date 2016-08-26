__author__ = 'Donald Cull'


# subjects = []
# subject = input("Subject: ")
# while subject != '':
#     subject = subjects.append(input("Subject: "))
# print(subjects)
def f(x):
    x = 2 * x
    return x


# x = 1
# result = f(x + 1 ) + f(x + 2 )
# print (result)

# VOWELS = "aeiou"
# phrase = input("Enter a string")
# for vowel in phrase:
#     if vowel in VOWELS:
#         print(vowel, end='')

scores = [[85, 97, 97, 2, 49], [12, 84, 85, 1, 51], [87, 75, 71, 70, 81], [68, 0, 30, 97, 72], [6, 39, 63, 17, 61], [82, 47, 29, 31, 45], [61, 37, 47, 56, 74], [90, 79, 92, 59, 22], [16, 77, 20, 83, 41], [7, 69, 22, 40, 28]]
count_1 = 0
count_2 = 1
for i in range(5):
    print(i)
    print(scores[count_1])
    print(scores[count_2])
    print()
    count_1 += 2
    count_2 += 2

# for index_i in range(10):
#     print("{:3.0f}".format(scores[i][index_i]), end="")

# for i in scores:
#     print(i)
    # for score in scores:
    #     print(scores[:][::2])
# print(len(scores))
# for subject in range(scores,None,2):
#     for scores in subject:
#         print(scores[subject][scores])
