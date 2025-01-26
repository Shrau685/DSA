class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None
def delete(head):
    if head is None:
        print("empty list")
        return None
    new_head=head.next
    del head
    return  new_head  


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
head=N1
#insert new node at end
head=delete(head)
current=head
while current!=None:
    print(current.data,end="-->")
    current=current.next
print("None")    
