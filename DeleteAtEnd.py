class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def delete(self,head):
    current=head
    if not self.head:
        return None 
    while current!=None:
        current=current.next
    current.next=None
    return 
N1=Node(10)
N2=Node(20)
N3=Node(30) 
N1.next=N2
N2.next=N3
head=N1
current=head

while current!=None:
    print(current.data,end="->")
    current=current.next
print(None)    
head=delete(N1)

current=head

while current!=None:
    print(current.data,end="->")
    current=current.next
