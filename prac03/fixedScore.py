"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
def main():
    score = float(input("Enter score: "))
    result = determine_grade(score)
    print(result)

def determine_grade(score):
    if score >= 90:
        grade = ("excellent!")
    elif score >= 50:
        grade = ("Passable")
    else:
        grade = ("Bad")
    return grade
main()