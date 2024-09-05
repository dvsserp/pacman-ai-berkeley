import Node

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head == None:
            self.head = Node.Node(data, None)
        else:
            newNode = Node.Node(data, self.head)
            self.head = newNode
        #If there is no head, it creates a head with no next. Else, it creates a new node and changes that node to head
    def pop(self):
        data = self.head.data
        self.head = self.head.next
        return data
        #establishes data asx the head data, then shifts to next data, then return the next data as head. 

    def peek(self):
        return self.head.data
        #returns the data of the head
