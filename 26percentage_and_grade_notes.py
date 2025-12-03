# program to calculate percentage and grade

m = float(input("Enter marks in Maths: "))
e = float(input("Enter marks in English: "))
s = float(input("Enter marks in Science: "))
evs = float(input("Enter marks in EVS: "))

# total marks = 400, so percentage:
percentage = (m + e + s + evs) / 400 * 100

print("Percentage =", percentage)

# Nested if for grade:
if percentage >= 90:
    print("Grade: A")
elif percentage >= 80:
    print("Grade: B")
elif percentage >= 70:
    print("Grade: C")
elif percentage >= 60:
    print("Grade: D")
elif percentage >= 40:
    print("Grade: E")
else:
    print("Grade: FAIL")
