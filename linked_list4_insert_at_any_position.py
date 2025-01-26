#program to implement linked list by creating nodes
class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None

#node creation
N1=Node(1)
N2=Node(2)
N3=Node(3)
N4=Node(4)
N5=Node(5)

#linking the elements of list by passing address of next node in next of previous node
N1.next=N2
N2.next=N3
N3.next=N4
N4.next=N5

#head is the the node from which traversing of list is starting
head=N1
current=head
new_node=Node(6)

#inserting at position two
while(current !=None and current.data !=2 ):
    current=current.next

#now current=2     
new_node.next=current.next
current.next=new_node
#print the linked list by traversing
head=N1
current=head
while(current != None):

    print(current.data)
    current=current.next