# LinkedList class
class LinkedList:
    def __init__(self, id, name, request):
        self.id = id
        self.name = name
        self.request = request
        self.next = None

# Queue class
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, id, name, request):
        newNode = LinkedList(id, name, request)
        if self.rear is None:
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
        else:
            temp = self.front.id
            self.front = self.front.next
            print(f"Request of ID: {temp} resolved successfully")

    def display(self):
        current = self.front
        while current:
            print(f"ID: {current.id}")
            print(f"Name: {current.name}")
            print(f"Requests: {current.request}")
            current = current.next

# CustomerCare class
class CustomerCare:
    def __init__(self):
        self.list = Queue()

    def menu(self):
        while True:
            print("\nWelcome to customer care")
            print("1. Add your requests")
            print("2. Complete Request")
            print("3. See status")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.enqueue_request()
            elif choice == '2':
                self.dequeue_request()
            elif choice == '3':
                self.track_status()
            elif choice == '4':
                print("Exiting system.")
                break
            else:
                print("Invalid choice. Please try again.")

    def enqueue_request(self):
        customer_id = input("Enter customer ID: ")
        name = input("Enter customer name: ")
        requests = input("Enter your required requests: ")
        self.list.enqueue(customer_id, name, requests)
        print("Request sent successfully.")

    def dequeue_request(self):
        self.list.dequeue()

    def track_status(self):
        print("\nStatus of Customer's requests:")
        self.list.display()

# Main code to start the customer care system
if __name__ == "__main__":
    h = CustomerCare()
    h.menu()
