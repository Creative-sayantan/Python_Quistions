#Calculate percentage of how much grade you get after your score
print("Enter the marks of five subjects::")

subject_1 = float (input ())
subject_2 = float (input ())
subject_3 = float (input ())
subject_4 = float (input ())
subject_5 = float (input ())

total, average, percentage, grade = None, None, None, None
total = subject_1 + subject_2 + subject_3 + subject_4 + subject_5
average = total / 5.0
percentage = (total / 500.0) * 100

if average >= 90:
    grade = 'O'
elif average >= 80 and average < 90:
    grade = 'A'
elif average >= 70 and average < 80:
    grade = 'B'
elif average >= 60 and average < 70:
    grade = 'C'
else:
    grade = 'D'

print ("\nThe Total marks is:   \t", total, "/ 500.00")
print ("\nThe Percentage is:    \t", percentage, "%")
print ("\nThe Grade is:         \t", grade)

