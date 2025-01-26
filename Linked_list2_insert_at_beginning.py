class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
def insert_at_beginning(head, new_data):
    # Create a new node with the given data
    new_node = Node(new_data)
    # Point new node's next to the current head
    new_node.next = head
    # Return the new node which is the new head
    return new_node
    
        

N1=Node(10) 
N2=Node(20) 
N3=Node(30)    

N1.next=N2
N2.next=N3

head=N1
current=head
print("original linked list : ")
while(current != None):
    print(current.data)
    current=current.next

# Insert new node at the beginning
head = insert_at_beginning(head, 0)

# Print modified linked list
print("Inserted linked list:")
current=head
while(current!=None):
    print(current.data)
    current=current.next