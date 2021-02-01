student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total = 0
count = 0
for height in student_heights:
    total += height
    count += 1

if count > 0:
    average_height = round(total/count)
    print(f"The average height is {average_height}")