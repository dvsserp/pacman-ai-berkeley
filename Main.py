import Stack
import Queues

queue = Queues.Queues()
stack = Stack.Stack()

""""
stack.push(5)
stack.push(7)
stack.push(8)

data = stack.peek()

print(data)

print(stack.pop())

print(stack.peek())
"""

queue.enqueue(5)
queue.enqueue(7)
queue.enqueue(8)

print(queue.peek())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())