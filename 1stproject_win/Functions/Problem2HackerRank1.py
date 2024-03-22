# Given the names and grades for each student in a class of
# students, store them in a nested list and print the name(s)
# of any student(s) having the second-lowest grade.
# Note: If there are multiple students with the second-lowest grade,
# order their names alphabetically and print each name on a new line.

n = int(input("Enter no. of students in the class = "))
students = []
for i in range(n):
    name = input(f'Enter Name {i+1} : ')
    marks = input(f'Enter Marks of {name} : ')
    students.append([name, marks])

for i in range(n):
    for j in range(n-1):
        if students[j][1] > students[j+1][1]:
            students[j], students[j+1] = students[j+1], students[j]

c = 1
s = students[0]
for i in range(1, n):
    if s[1] == students[i][1]:
        c += 1
s = students[c]
c1 = 1
for i in range(c+1, n):
    if s[1] == students[i][1]:
        c1 += 1
min_student = students[c:c+c1]
min_student.sort()
for i in range(len(min_student)):
    print(min_student[i][0])
