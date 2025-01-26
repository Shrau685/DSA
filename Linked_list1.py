#program to implement linked list by creating nodes
class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None

#node creation
N1=Node(1)
N2=Node(2)
N3=Node(3)


#linking the elements of list by passing address of next node in next of previous node
N1.next=N2
N2.next=N3


#head is the the node from which traversing of list is starting
head=N1
current=head

#print the linked list by traversing
while(current != None):

    print(current.data)
    current=current.next

