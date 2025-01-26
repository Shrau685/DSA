class Node:
    def __init__(self, task, priority):
        self.task = task
        self.priority = priority
        self.next = None

class Stack:
    def __init__(self):
        self.head = None  # Start with an empty stack
    
    def push(self, task, priority):
        new_node = Node(task, priority)
        new_node.next = self.head
        self.head = new_node
        print(f"Task '{task}' with priority '{priority}' added successfully.")
    
    def pop(self):
        if not self.head:
            print("The stack is empty. No task to remove.")
            return
        popped_task = self.head.task
        self.head = self.head.next
        print(f"Task '{popped_task}' removed successfully.")
    
    def peek(self):
        if not self.head:
            print("The stack is empty. No task to display.")
            return
        print(f"Task '{self.head.task}' is at the top of the stack.")
    
    def display(self):
        if not self.head:
            print("The stack is empty. No tasks to display.")
            return
        current = self.head
        print("Current tasks in the stack:")
        while current:
            print(f"Task: {current.task}, Priority: {current.priority}")
            current = current.next

if __name__ == "__main__":
    stack = Stack()
    stack.push("Complete project proposal", "High")
    stack.push("Schedule Team Meeting", "Medium")
    stack.push("Review draft presentation", "Low")
    stack.push("Prepare weekly report", "High")
    stack.push("Respond to client emails", "Medium")
    stack.display()
    stack.peek()
    stack.pop()
    stack.display()
