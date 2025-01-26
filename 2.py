class Node:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.next = None
        self.prev = None

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    def add_item(self, name, quantity, price):
        new_node = Node(name, quantity, price)
        if self.head is None:
            self.head = new_node
            new_node.prev = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
            self.head.prev = new_node


    def remove_item(self, name):
        if self.head is None:
            print("List is empty")
            return 
        current = self.head
        while True:
            if current.name == name:
                if current.next == current:
                    self.head = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    if current == self.head:
                        self.head = current.next
                print(f"Item '{name}' removed successfully")
               
                return
            current = current.next
            if current == self.head:
                break
        print(f"Item '{name}' not found.")

    def update_item(self, name):
        current = self.head
        while True:
            if current.name == name:
                current.quantity = int(input("Enter the new quantity: "))
                current.price = int(input("Enter the new price: "))
                print(f"Item '{name}' updated successfully")
                return
            current = current.next
            if current == self.head:
                break
        print(f"Item '{name}' not found.")

    def display_order(self):
        print("Order Details")
        if self.head is None:
            print("No items to display.")
            return
        current = self.head
        while True:
            print(f"Name: {current.name}, Quantity: {current.quantity}, Price: {current.price}")
            current = current.next
            if current == self.head:
                break

    def search_item(self):
        name = input("Enter the name of item: ")
        current = self.head
        while True:
            if current.name == name:
                print(f"Name: {current.name}, Quantity: {current.quantity}, Price: {current.price}")
                return
            current = current.next
            if current == self.head:
                break
        print(f"Item '{name}' not found.")

class RetailManagementSystem:
    def __init__(self):
        self.order = DoublyCircularLinkedList()

    def menu(self):
        while True:
            print()
            print("Retail Management System")
            print("1. Add Item")
            print("2. Remove Item")
            print("3. Update Item")
            print("4. Display Order")
            print("5. Search Item")
            
            choice = input("Enter your Choice: ")
            if choice == '1':
                self.add_new_item()
            elif choice == '2':
                self.remove_an_item()
            elif choice == '3':
                self.update_an_item()
            elif choice == '4':
                self.display_order()
            elif choice == '5':
                self.search_item()
            else:
                print("Invalid choice, please try again.")

    def add_new_item(self):
        name = input("Enter the name: ")
        quantity = int(input("Enter the Quantity: "))
        price = int(input("Enter the price: "))
        self.order.add_item(name, quantity, price)
        print("Item added successfully.")
       

    def remove_an_item(self):
        name = input("Enter the name of item: ")
        self.order.remove_item(name)

    def update_an_item(self):
        name = input("Enter the name of item: ")
        self.order.update_item(name)

    def display_order(self):
        self.order.display_order()

    def search_item(self):
        self.order.search_item()

if __name__ == "__main__":
    rms = RetailManagementSystem()
    rms.menu()


