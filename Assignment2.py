'''
Question 1:

score = int(input("Enter your score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
'''






'''
Question 2:

students = {}

while True:
    print("\n1. Add Student")
    print("2. Update Student Grade")
    print("3. Display All Grades")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        students[name] = grade
        print("Student added successfully.")

    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print("Grade updated successfully.")
        else:
            print("Student not found.")

    elif choice == "3":
        for name, grade in students.items():
            print(name, ":", grade)

    elif choice == "4":
        break

    else:
        print("Invalid choice.")
'''





'''
Question 3:

file = open("sample.txt", "w")
file.write("This is a sample file.\n")
file.write("Writing data using Python file handling.")
file.close()

print("Data written to file successfully.")

'''





'''
Question 4:

file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()
'''
