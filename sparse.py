# Convert sparse matrix to a compact list representation
arr1 = [
    [0, 0, 45, 0, 90],
    [0, 67, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 89, 0],
    [36, 0, 0, 0, 0],
    [34, 56, 0, 0, 0],
    [0, 0, 0, 78, 98]
]

# Create a compact representation of the sparse matrix
arr2 = []
for i in range(len(arr1)):
    for j in range(len(arr1[0])):
        if arr1[i][j] != 0:
            arr2.append([i, j, arr1[i][j]])

# Function to display the compact array
def print_arr2(arr2):
    print("Row  Column  Value")
    for i in range(len(arr2)):
        print(f"{arr2[i][0]:<5}{arr2[i][1]:<8}{arr2[i][2]}")

# Function to find the highest grade
def highest_grade(arr2):
    max_grade = -1
    student_id = -1
    for i in range(len(arr2)):
        if arr2[i][2] > max_grade:
            max_grade = arr2[i][2]
            student_id = arr2[i][0]
    print(f"The highest marks are {max_grade}, obtained by student {student_id}.")

# Function to calculate the average grade for a subject
def avg_grade_per_subj(arr2):
    subject = int(input("Enter the subject number (column index): "))
    total = 0
    count = 0
    for i in range(len(arr2)):
        if arr2[i][1] == subject:
            total += arr2[i][2]
            count += 1
    if count == 0:
        print(f"No grades available for subject {subject}.")
    else:
        print(f"The average grade for subject {subject} is {total / count:.2f}.")

# Function to find the subject with the highest grade
def sub_with_high(arr2):
    max_grade = -1
    subject_id = -1
    for i in range(len(arr2)):
        if arr2[i][2] > max_grade:
            max_grade = arr2[i][2]
            subject_id = arr2[i][1]
    print(f"The subject with the highest grade is {subject_id}, and the grade is {max_grade}.")

# Function to display menu options
def print_menu():
    print("\nMenu:")
    print("1: Display all students' grades with subjects")
    print("2: Find the highest grade")
    print("3: Calculate average grade per subject")
    print("4: Find the subject with the highest grade")
    print("5: Exit")

# Main program
stop = False
while not stop:
    print_menu()
    try:
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                print_arr2(arr2)
            case 2:
                highest_grade(arr2)
            case 3:
                avg_grade_per_subj(arr2)
            case 4:
                sub_with_high(arr2)
            case 5:
                stop = True
                print("Exiting the program. Goodbye!")
            case _:
                print("Invalid input. Please try again.")
    except ValueError:
        print("Please enter a valid number.")
