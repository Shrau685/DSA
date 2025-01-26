class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to delete a node at a given position
def delete_at_position(head, position):
    if not head:
        return head

    # If head needs to be removed
    if position == 0:
        return head.next

    temp = head
    for i in range(position - 1):
        temp = temp.next
        if temp is None or temp.next is None:
            return head

    # Node temp.next is the node to be deleted
    temp.next = temp.next.next
    return head

# Manually creating the linked list
N1 = Node(10)
N2 = Node(20)
N3 = Node(30)
N4 = Node(40)
N5 = Node(50)

# Linking nodes
N1.next = N2
N2.next = N3
N3.next = N4
N4.next = N5

# Printing the original list
current = N1
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

# Deleting node at position 2
N1 = delete_at_position(N1, 2)

# Printing the list after deletion
current = N1
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")
