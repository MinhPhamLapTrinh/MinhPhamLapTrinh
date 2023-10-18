class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Queue:
    def __init__(self, front=None, back=None, capacity=5):
        self.front = front
        self.back = back
        self.size = 0
        self.capacity = capacity

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size >= self.capacity

    def enqueue(self, data):
        if self.is_full():
            print("The QUEUE list is full")
        new_node = Node(data)
        if self.is_empty():
            self.front = self.back = new_node
        self.back.next = new_node
        self.back = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("List is empty")
        removed_node = self.front
        self.front = removed_node.next
        self.size -= 1

    def get_front(self):
        return self.front.data

    def printlist(self):
        curr = self.front
        while curr is not None:
            print(curr.data)
            curr = curr.next


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.printlist()
print(f"The value at front: {queue.get_front()} ")
print("---------------------------------------")
print("After remove one node")
print("---------------------------------------")
queue.dequeue()
queue.printlist()
print(f"The value at front: {queue.get_front()} ")
