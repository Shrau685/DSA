# Node class
class Node:
    def __init__(self, id, name, items):
        self.id = id
        self.name = name
        self.items = items
        self.next = None

# CircularQueue class
class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, id, name, items):
        new_node = Node(id, name, items)
        if self.front is None and self.rear is None:
            self.front = self.rear = new_node
            self.rear.next = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front

    def dequeue(self):
        if self.front is None:
            print("No orders to delete.")
        elif self.front == self.rear:
            temp = self.front
            self.front = self.rear = None
            print(f"Order deleted\nID: {temp.id}\nName: {temp.name}\nItems: {temp.items}")
        else:
            temp = self.front
            self.front = self.front.next
            self.rear.next = self.front
            print(f"Order deleted\nID: {temp.id}\nName: {temp.name}\nItems: {temp.items}")

    def display(self):
        if self.front is None:
            print("No orders")
            return
        temp = self.front
        print("List of orders:")
        while True:
            print(f"ID: {temp.id}\nName: {temp.name}\nItems: {temp.items}\n")
            temp = temp.next
            if temp == self.front:
                break

# HotelManagementSystem class
class HotelManagementSystem:
    def __init__(self):
        self.order = CircularQueue()

    def menu(self):
        while True:
            print("\nHotel Management System")
            print("1. Add Order")
            print("2. Remove Order")
            print("3. View orders")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_item()
            elif choice == '2':
                self.remove_item()
            elif choice == '3':
                self.view_item()
            elif choice == '4':
                print("Exiting system.")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_item(self):
        id = int(input("Enter ID: "))
        name = input("Enter your name: ")
        items = input("Enter your ordered items: ")
        self.order.enqueue(id, name, items)
        print("Order added successfully")

    def remove_item(self):
        self.order.dequeue()

    def view_item(self):
        print("\nList of orders:\n")
        self.order.display()

# Main code to start the hotel management system
if __name__ == "__main__":
    rms = HotelManagementSystem()
    rms.menu()
