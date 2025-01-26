class PatientNode:
    def __init__(self, patient_id, name, condition, next=None):
        self.patient_id = patient_id
        self.name = name
        self.condition = condition
        self.next = next

class PatientQueue:
    def __init__(self):
        self.head = None  # Start of the queue

    def is_empty(self):
        return self.head is None

    def add_patient(self, patient_id, name, condition):
        new_patient = PatientNode(patient_id, name, condition)
        if self.is_empty():
            self.head = new_patient
        else:
            # Traverse to the end of the list
            current = self.head
            while current.next:
                current = current.next
            current.next = new_patient

    def remove_patient(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        removed_patient = self.head
        self.head = self.head.next
        return removed_patient

    def move_up_priority(self, patient_id):
        if self.is_empty():
            raise Exception("Queue is empty")
        
        prev = None
        current = self.head
        while current and current.patient_id != patient_id:
            prev = current
            current = current.next
        
        if current is None:
            raise Exception("Patient not found")
        
        if prev is None:
            return  # Patient is already at the head of the list
        
        # Remove the patient from its current position
        prev.next = current.next
        
        # Move the patient to the head
        current.next = self.head
        self.head = current

    def display_queue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        
        current = self.head
        while current:
            print(f"Patient ID: {current.patient_id}, Name: {current.name}, Condition: {current.condition}")
            current = current.next

    def search_patient(self, patient_id):
        current = self.head
        while current:
            if current.patient_id == patient_id:
                return current
            current = current.next
        raise Exception("Patient not found")

    def update_patient_info(self, patient_id, name=None, condition=None):
        patient = self.search_patient(patient_id)
        if name:
            patient.name = name
        if condition:
            patient.condition = condition

def main():
    queue = PatientQueue()
    
    while True:
        print("\nEmergency Room Patient Management System")
        print("1. Add Patient")
        print("2. Remove Patient")
        print("3. Move Patient Up in Priority")
        print("4. Display Queue")
        print("5. Search Patient")
        print("6. Update Patient Information")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            patient_id = int(input("Enter Patient ID: "))
            name = input("Enter Patient Name: ")
            condition = input("Enter Patient Condition: ")
            queue.add_patient(patient_id, name, condition)
            print("Patient added successfully.")
        
        elif choice == '2':
            try:
                removed_patient = queue.remove_patient()
                print(f"Removed Patient: ID: {removed_patient.patient_id}, Name: {removed_patient.name}")
            except Exception as e:
                print(e)
        
        elif choice == '3':
            patient_id = int(input("Enter Patient ID to move up: "))
            try:
                queue.move_up_priority(patient_id)
                print("Patient moved up in priority.")
            except Exception as e:
                print(e)
        
        elif choice == '4':
            print("Current Queue:")
            queue.display_queue()
        
        elif choice == '5':
            patient_id = int(input("Enter Patient ID to search: "))
            try:
                patient = queue.search_patient(patient_id)
                print(f"Found Patient: ID: {patient.patient_id}, Name: {patient.name}, Condition: {patient.condition}")
            except Exception as e:
                print(e)
        
        elif choice == '6':
            patient_id = int(input("Enter Patient ID to update: "))
            name = input("Enter new Patient Name (leave empty to keep current): ")
            condition = input("Enter new Patient Condition (leave empty to keep current): ")
            try:
                queue.update_patient_info(patient_id, name if name else None, condition if condition else None)
                print("Patient information updated.")
            except Exception as e:
                print(e)
        
        elif choice == '7':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
