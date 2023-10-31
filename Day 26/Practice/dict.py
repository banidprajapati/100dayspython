import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

# student_score = {student: random.randint(1, 100) for student in names}

# print(student_score)
student_score = {'Alex': 82, 'Beth': 43, 'Caroline': 95,
                 'Dave': 47, 'Eleanor': 80, 'Freddie': 86}
passed_student = {key: value
                  for key, value in student_score.items() if value >= 60}
# for i in student_score.values():
#     print(i)
print(passed_student)
