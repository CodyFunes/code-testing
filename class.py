sum = 0
total_no_of_grades = int(input("how many grades will we average: "))
count = 0

while count < total_no_of_grades:
    grade = float(input("Please enter grade: "))
    sum += grade
    count += 1

average = sum/3
print("The average is,", average)




