#Author: Cecelia Williams
#Last Revision: 05.3.2017
#Description: Chapter 25 Stacks


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    

    def is_empty(self):
        return (self.items == [])

    def print_stack(self):
        return self.items




stack1 = Stack()
stack1.push(22)
stack1.push(16)
stack1.push(25)
stack1.push(1)
stack1.push(10)

stack2 = Stack()
stack2.push(3)
stack2.push(7)
stack2.push(12)
stack2.push(10)
stack2.push(5)

print(Stack.print_stack(stack1))
print(Stack.print_stack(stack2))

while not stack1.is_empty():
    print(stack1.pop(), end = " ")

print()
stack2.pop()
print(Stack.print_stack(stack2))
