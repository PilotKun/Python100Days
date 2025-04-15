student_height = input("input a list of student heights \n").split()

for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
print(student_height)

total_height = 0
for height in student_height:
    total_height += height
print(total_height)

students = 0
for student in student_height:
    students += 1
print(students)

avg = round(total_height / students)
print(avg)