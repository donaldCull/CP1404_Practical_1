__author__ = 'Donald Cull'
"""
CP1404/CP5632 Practical
CSV scores file program - broken one
scores file stores scores for each subject for 10 people.
This code reads the lines into lists, saves the first line as a list of subject codes and
converts the rest of the lines from a list of strings into a list of numbers,
which it then prints with the maximum value for that subject.
Nice. Except, it’s broken! It reads the lists per user not per subject so the results are incorrect.
Use the debugger to follow what it's doing... then fix it.
"""


def main():
    scores_file = open("scores.csv")
    scores_data = scores_file.readlines()
    print(scores_data)
    subjects = scores_data[0].strip().split(",")
    score_values = []
    for score_line in scores_data[1:]:
        score_strings = score_line.strip().split(",")
        score_numbers = [int(value) for value in score_strings]
        score_values.append(score_numbers)
    scores_file.close()

    scores_index = 0
    end_score_index = 1
    for i in range(len(subjects)):
        print(subjects[i], "Scores:")
        for score in range(1):
            print(score)
            print(score_values[scores_index])
            print(score_values[end_score_index])

            scores_index += 2
            end_score_index += 2
        # print("Max:", max(score_values[i]+score_values))
        print()


main()