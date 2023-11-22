class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hashIndex = self._hash(key)
        while self.keys[hashIndex] is not None:
            hashIndex = (hashIndex + 1) % self.size

        self.keys[hashIndex] = key
        self.values[hashIndex] = value

    def search(self, key):
        hashIndex = self._hash(key)
        while self.keys[hashIndex] is not None:
            if self.keys[hashIndex] == key:
                return self.values[hashIndex]
            hashIndex = (hashIndex + 1) % self.size
        return None

    def remove(self, key):
        hashIndex = self._hash(key)
        while self.keys[hashIndex] is not None:
            if self.keys[hashIndex] == key:
                self.keys[hashIndex] = None
                self.values[hashIndex] = None
                emptyIdx = hashIndex

                currentIdx = (emptyIdx + 1) % self.size
                while self.keys[currentIdx] is not None:
                    properHashIdx = self._hash(self.keys[currentIdx])

                    if (emptyIdx <= currentIdx) and (emptyIdx >= properHashIdx):
                        self.keys[emptyIdx] = self.keys[currentIdx]
                        self.values[emptyIdx] = self.values[currentIdx]

                        self.keys[currentIdx] = None
                        self.values[currentIdx] = None

                        emptyIdx = currentIdx

                    currentIdx = (currentIdx + 1) % self.size
                return
            hashIndex = (hashIndex + 1) % self.size

    def display(self):
        for i in range(self.size):
            if self.keys[i] is not None:
                print(f"({self.keys[i]}, {self.values[i]})", end=" ")
            else:
                print("None", end=" ")
        print()

# Example usage:
hash_table = HashTable(10)

hash_table.insert(15, "fifteen")
hash_table.insert(18, "eighteen")
hash_table.insert(10, "ten")
hash_table.insert(25, "twenty-five")
hash_table.insert(14, "fourteen")
hash_table.insert(24, "twenty-four")

hash_table.display()

print("Search 'ten':", hash_table.search(10))
print("Search 'four':", hash_table.search(4))

hash_table.remove(15)

hash_table.display()