
def get_student_data():
    name = input("Please enter your name: ")
    first_name = input("Please enter your first name: ")
    student_id = int(input("Please enter your student-id: "))

    return (name, first_name, student_id)

user = get_student_data()
print(user)