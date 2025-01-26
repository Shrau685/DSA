def insertion_sort(grades):
    for i in range(1, len(grades)):
        value = grades[i]
        j = i - 1
        while j >= 0 and value < grades[j]:
            grades[j + 1] = grades[j]
            j -= 1
        grades[j + 1] = value

def read_file(filename):
    with open(filename, 'r') as file:
        grades = [int(line.strip()) for line in file]
    return grades

def write_grades(filename, grades):
    with open(filename, 'w') as file:
        for grade in grades:
            file.write(f"{grade}\n")

def main():
    # Read grades from the input file
    grades = read_file(r'grades.txt')

    # Sort the grades using insertion sort
    insertion_sort(grades)

    # Display sorted grades
    print("Sorted grades:")
    for grade in grades:
        print(grade)

    # Write sorted grades to the output file
    write_grades('sorted_grades.txt', grades)

if __name__ == "__main__":
    main()
