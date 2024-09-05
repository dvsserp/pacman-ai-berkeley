import Node

#circular linked list
class Queues:
    def __init__(self):
        self.head = None

    def enqueue(self, data):
        if self.head == None:
            self.head = Node.Node(data, None)
            self.head.next = self.head
        else:
            newNode = Node.Node(self.head.data, self.head.next)
            self.head.data = data
            self.head.next = newNode
            self.head = self.head.next
            #create new node, then set the node to contain the head data and connect it with the next head. the head data becomes just data 
            #then it is connected to the new node which is the new head, then the head is transferred to the next node which is the new Node

    def dequeue(self):
        data = self.head.data
        if self.head.next == self.head:
            self.head = None
        else:
            self.head.data = self.head.next.data
            self.head.next = self.head.next.next
        return data
    #saves the data of head. If head is by itself, it gets removed. otherwise it saves the next head data then points the original head to the 3rd data(last data). 

    def peek(self):
        return self.head.data