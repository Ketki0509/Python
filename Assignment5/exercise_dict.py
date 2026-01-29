student_dict = {"Alice":85, "John":78, "Bob":75}
student_name = input("Enter the student's name: ")
if student_name in student_dict:
    student_marks = student_dict[student_name]
    print(f"{student_name}'s marks: {student_marks}")
else:
    print("Student not found.")