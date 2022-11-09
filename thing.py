student1= {
    "age": 20,
    "name": "Fred",
    "phone_number": "555-5555"
}
student2 ={
    "age": 30,
    "name": "Jenny",
    "phone_number": "555-5555"
}
print("The name of the student is" + student2['name'])
student_list = [
    student1, student2
]
print(student_list)

i = 0
while (i < len(student_list)):
    print(student_list[i])
    i += 1
for i in student_list:
    print(i)

student_names =["Jed", "Jen", "Sandy"]
for student_name in student_names:
    print(student_name)
print(student_names[0])

i = len(student_names)
while (i >= 0):
    print(student_names[i])
    i -= 1

student_names.append('Emily')
student_names