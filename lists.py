"""n = int(input("Enter a number of students:"))
students = [0] * n
oldest = 0
for i in range(len(students)):
    students[i] = int(input(" (%d) Enter a student's age:" %(i+1)))
    if oldest < students[i]:
        oldest = students[i]
print("Oldest student's age = %d" %(oldest))"""


### If the 'n' is unknown

students = []
oldest = 0
while True:
    age = int(input("Enter student's age (or -1 to quit): "))
    if age == -1:
        break
    if oldest < age:
        oldest = age
    students.append(age)
print(oldest)