class StudentInformationSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, age, grade):
        self.students[student_id] = {"Name": name, "Age": age, "Grade": grade}
        print("Student added successfully.")

    def retrieve_student(self, student_id):
        student = self.students.get(student_id)
        if student:
            print(f"Student ID: {student_id}, Info: {student}")
        else:
            print("Student not found.")

    def delete_student(self, student_id):
        if self.students.pop(student_id, None):
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    def update_student(self, student_id, name=None, age=None, grade=None):
        student = self.students.get(student_id)
        if student:
            if name:
                student["Name"] = name
            if age:
                student["Age"] = age
            if grade:
                student["Grade"] = grade
            print("Student updated successfully.")
        else:
            print("Student not found.")

    def display_all_students(self):
        if self.students:
            for student_id, info in self.students.items():
                print(f"Student ID: {student_id}, Info: {info}")
        else:
            print("No students in the system.")

# Example usage
if __name__ == "__main__":
    system = StudentInformationSystem()
    while True:
        print("\nOptions:\n1. Add Student\n2. Retrieve Student\n3. Delete Student\n4. Update Student\n5. Display All Students\n6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            grade = input("Enter Grade: ")
            system.add_student(student_id, name, age, grade)
        elif choice == '2':
            student_id = input("Enter Student ID: ")
            system.retrieve_student(student_id)
        elif choice == '3':
            student_id = input("Enter Student ID: ")
            system.delete_student(student_id)
        elif choice == '4':
            student_id = input("Enter Student ID: ")
            name = input("Enter new Name (or press Enter to skip): ")
            age = input("Enter new Age (or press Enter to skip): ")
            grade = input("Enter new Grade (or press Enter to skip): ")
            system.update_student(student_id, name or None, age or None, grade or None)
        elif choice == '5':
            system.display_all_students()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
