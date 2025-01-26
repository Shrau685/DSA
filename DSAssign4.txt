import os
class Node:
    def __init__(self, task):
        self.task = task
        self.next = None



class Stack():
    def __init__(self):
        self.head = None

    def push(self,task):
        task1 = Node(task)
        if (self.head is None):
            self.head = task1
            return
        task1.next = self.head
        self.head = task1

    def remove(self):
        if self.head is None:
            print("the task list is empty")
            return
        self.head = self.head.next

    def print1(self):
        temp = self.head
        if self.head is None:
            print("The list is Empty")
            return
        while (temp != None):
            print("task name : ", temp.task)
            temp = temp.next




class todolist :
    def __init__(self) :
        self.l1 = Stack()
        self.l2 = Stack()
        self.l3 = Stack()

    def add(self,task_z):
        print("1 : high priority task")
        print("2  : Medium priority task")
        print("3 : low priority task")
        z = int(input("Enter on which priority you want to perform : "))
        match z :
            case 1 :
                self.l1.push(task_z)
            case 2 :
                self.l2.push(task_z)
            case 3 :
                self.l3.push(task_z)
            case _ :
                print("Enter valid input")

                
    def removeStack(self) : 
        if self.l1.head is None : 
            self.l2.remove()
            print("task removed Succesfully")

            return
        if self.l2.head is None : 
            self.l2.remove()
            print("task removed Succesfully")
            return
        if self.l3.head is None : 
            print("The task list is Empty")
            return
        
        self.l1.remove()
        print("task removed Succesfully")



    def print2(self):
        print("1 : high priority task")
        print("2  : Medium priority task")
        print("3 : low priority task")
        z = int(input("Enter which priority task you want to print : "))
        match z :
            case 1 :
                self.l1.print1()
            case 2 :
                self.l2.print1()
            case 3 :
                self.l3.print1()
            case _ :
                print("Enter valid input")

    def oper(self) :
        print("1 : To-do list : ") 
        print("2 : to add task")
        print("3 : to remove top task")
        print("4 : exit")

t1 = todolist()
stop = 1
while stop == 0 : 
    t1.oper()
    oop = int(input("ENter which task you want to perform : "))
    match (oop) : 
        case 2 : 
            task_z = input("Enter task name : ")
            t1.add(task_z)
        case 1 : 
            t1.print2()
        case 3 : 
            t1.removeStack()
        case 4 : 
            stop = 1
        case _ : 
            print("Enter valid input")
