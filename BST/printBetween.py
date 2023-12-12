class BST:
    class Node:
        def __init__(self, value=None, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return BST.Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        return node

    def print_between(self, min_val, max_val):
        self._print_between(self.root, min_val, max_val)

    def _print_between(self, node, min_val, max_val):
        if node is not None:
            if min_val < node.value:
                self._print_between(node.left, min_val, max_val)
            if min_val <= node.value <= max_val:
                print(node.value)
            if max_val > node.value:
                self._print_between(node.right, min_val, max_val)

# Example usage:
my_tree = BST()
values_to_insert = [5, 3, 7, 2, 4, 6, 8]

for value in values_to_insert:
    my_tree.insert(value)

# Call the print_between function with a specified range
my_tree.print_between(3, 8)
