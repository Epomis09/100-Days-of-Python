# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

sum = 0
for height in student_heights:
    sum += height

student_heights_length = 0
for student in student_heights:
    student_heights_length += 1

print(round(sum/student_heights_length))