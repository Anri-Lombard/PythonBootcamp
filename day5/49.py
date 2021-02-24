# could not use len() or sum() for this challenge
student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
total_students = 0
for height in student_heights:
    total_height += height
    total_students += 1

average = total_height / total_students
print(average)
