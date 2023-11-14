class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        hash_index = self._hash(key)
        if self.table[hash_index] is None:
            self.table[hash_index] = Node(key, value)
            self.size += 1
        else:
            current_node = self.table[hash_index]
            while current_node:
                if current_node.key == key:
                    current_node.value = value
                    return
                current_node = current_node.next
            new_node = Node(key, value)
            new_node.next = self.table[hash_index]
            self.table[hash_index] = new_node
            self.size += 1

    def search(self, key):
        hash_index = self._hash(key)
        current = self.table[hash_index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError(key)

    def remove(self, key):
        hash_index = self._hash(key)
        previous = None
        current = self.table[hash_index]
        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[hash_index] = current.next
                    self.size -= 1
                return
            previous = current
            current = current.next
        raise KeyError(key)

    def __len__(self):
        return self.size

    def __contains__(self, key):
        try:
            self.search(key)
            return True
        except KeyError:
            return False

    def print_table(self):
        for i in range(self.capacity):
            current = self.table[i]
            print(f"Index is: {i}")
            while current:
                print(f"{current.key}: {current.value}")
                current = current.next


if __name__ == '__main__':

    # Create a hash table with
    # a capacity of 5
    ht = HashTable(5)

    # Add some key-value pairs
    # to the hash table
    ht.insert("apple", 3)
    ht.insert("banana", 2)
    ht.insert("cherry", 5)

    # Check if the hash table
    # contains a key
    print("apple" in ht)  # True
    print("durian" in ht)  # False

    # Get the value for a key
    print(ht.search("banana"))  # 2

    # Update the value for a key
    ht.insert("banana", 4)
    print(ht.search("banana"))  # 4

    print(ht.print_table())
    ht.remove("apple")
    # Check the size of the hash table
    print(len(ht))  # 3

    # Print the table after all
    print(ht.print_table())

