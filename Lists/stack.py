class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Stack:
    def __init__(self, top=None, cap=5):
        self.top = top
        self.cap = cap
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size >= self.cap

    def push(self, data):
        if self.is_full():
            return print("You have reached the limit of capacity")
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            print("Out of value")
        removed_node = self.top
        self.top = removed_node.next
        self.size -= 1

    def printStack(self):
        curr = self.top
        while curr is not None:
            print(curr.data)
            curr = curr.next

    def get_top(self):
        return self.top.data

stack = Stack()
stack.push(5)
stack.push(2)
stack.push(3)
stack.push(6)
stack.push(7)
stack.pop()
stack.push(9)
stack.pop()
print(f"The value of the top in the stack list is: {stack.get_top()}")
print(stack.printStack())
