# Node class
class Node:
    def __init__(self, patient_name, disease, priority, next_node=None):
        self.patient_name = patient_name
        self.disease = disease
        self.priority = priority
        self.next = next_node

# Hospital class
class Hospital:
    # Constructor
    def __init__(self):
        self.head = None

    # Method to admit a patient with parameters: name, disease, and priority
    def add_patient(self, patient_name, disease, priority):
        new_node = Node(patient_name, disease, priority)
        if not self.head or self.head.priority > priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.priority <= priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    # Method to discharge a patient
    def remove_patient(self):
        if not self.head:
            print("No patients to remove.")
            return None
        removed_patient = self.head
        self.head = self.head.next
        return removed_patient

    # Method to display the queue
    def display_queue(self):
        current = self.head
        if not current:
            print("The queue is empty.")
            return
        while current:
            print(f"Priority: {current.priority}, Patient Name: {current.patient_name}, Disease: {current.disease}")
            current = current.next

    # Method to move a patient up in priority
    def move_patient_up(self, patient_name):
        if not self.head or self.head.patient_name == patient_name:
            return False

        prev = None
        current = self.head

        while current and current.patient_name != patient_name:
            prev = current
            current = current.next

        if current and prev:
            if prev != self.head:
                prev.next = current.next
                current.next = self.head
                self.head = current
                return True
        return False

if __name__ == "__main__":
    queue = Hospital()
    capacity = 0

    # Display menu
    while True:
        print("\nEmergency Room Queue System")
        print("1. Admit Patient")
        print("2. Discharge Patient")
        print("3. Move Patient Up in Priority")
        print("4. Display Queue")
        print("5. Check Availability of Rooms to Admit Patient")
        print("6. Exit")
        print("Menu for Priority: 1.Emergency 2.Critical 3.Non_urgent 4.Elective")
        print()

        choice = input("Enter your choice: ")

        if choice == '1':
            # Check capacity of hospital
            if capacity < 10:
                patient_name = input("Enter patient name: ")
                disease = input("Enter patient disease: ")
                priority = int(input("Enter patient priority: "))
                print()
                queue.add_patient(patient_name, disease, priority)
                capacity += 1
            else:
                print("We are sorry. The hospital is full.")
                print()

        elif choice == '2':
            removed = queue.remove_patient()
            if removed:
                print(f"Removed Patient - Name: {removed.patient_name}")
                print()
                capacity -= 1

        elif choice == '3':
            patient_name = input("Enter patient name to move up: ")
            success = queue.move_patient_up(patient_name)
            if success:
                print("Patient moved up successfully.")
                print()
            else:
                print("Patient not found or is already at the top.")
                print()

        elif choice == '4':
            print("Current Queue:")
            queue.display_queue()
            print()

        elif choice == '5':
            if capacity < 10:
                print("Remaining capacity:", capacity)
                print("Patient can be admitted.")
                print()
            else:
                print("We are sorry. We are unable to admit your patient.")
                print()

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")
