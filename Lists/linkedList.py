class LinkedList:
    class Node:
        def __init__(self, data, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

        def get_data(self):
            return self.data

    def __init__(self, front=None, back=None):
        self.front = front
        self.back = back

    def push_front(self, value):
        new_node = self.Node(value, next=self.front, prev=None)
        if self.front is None:
            self.back = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
        self.front = new_node

    def push_back(self, value):
        new_node = self.Node(value, next=None, prev=self.back)
        if self.back is None:
            self.front = new_node
        else:
            new_node.prev = self.back
            self.back.next = new_node
        self.back = new_node

    def pop_front(self):
        if self.front is not None:
            removed_node = self.front
            self.front = self.front.next
            if self.front is None:
                self.back = None
            else:
                self.front.prev = None
        del removed_node

    def pop_back(self):
        if self.back is not None:
            removed_node = self.back
            self.back = removed_node.prev
            if self.back is None:
                self.front = None
            else:
                self.back.next = None
        del removed_node
    def search(self, data):
        current = self.front
        while current is not None:
            if current.data == data:
                return True
            current = self.front.next
        return False

    def printList(self):
        curr = self.front
        while curr is not None:
            print(curr.get_data())
            curr = curr.next
        return None
    def get_front(self):
        return self.front.data


list = LinkedList()
list.push_front(3)
list.push_front(1)
list.push_front(2)
list.pop_front()
list.push_back(4)
list.pop_back()
list.pop_back()
list.push_front(5)
list.push_back(6)

list.printList()
print(f"The front value is: {list.get_front()}")