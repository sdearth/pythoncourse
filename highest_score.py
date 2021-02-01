student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

high_score = -1

for score in student_scores:
    if score > high_score:
        high_score = score

print(high_score)