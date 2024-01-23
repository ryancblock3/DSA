class Node:
    def __init__(self, value):
        # Node constructor initializes a new node with a given value
        self.value = value
        self.left = None  # Reference to the left child node
        self.right = None  # Reference to the right child node

class BinarySearchTree:
    def __init__(self):
        # BinarySearchTree constructor initializes an empty binary search tree
        self.root = None  # Reference to the root node

    def insert(self, value):
        # Insert a new node with the given value into the binary search tree
        new_node = Node(value)
        
        # If the tree is empty, set the new node as the root
        if self.root is None:
            self.root = new_node
            return True
        
        # Traverse the tree to find the correct position for the new node
        temp = self.root
        while True:
            if new_node.value == temp.value:
                # If the value already exists, return False (no duplicates allowed)
                return False
            if new_node.value < temp.value:
                # If the new value is less than the current node's value, move left
                if temp.left is None:
                    # If the left child is None, insert the new node here
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                # If the new value is greater, move right
                if temp.right is None:
                    # If the right child is None, insert the new node here
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        # Check if a node with the given value exists in the binary search tree
        temp = self.root
        while temp is not None:
            if value < temp.value:
                # If the value is less than the current node's value, move left
                temp = temp.left
            elif value > temp.value:
                # If the value is greater, move right
                temp = temp.right
            else:
                # If the value is equal, the node with the value exists
                return True
        # If the value is not found, return False
        return False



# Testing Constructor
        
# my_tree = BinarySearchTree()
# print(my_tree.root)
                    
# Testing Insert
                    
# my_tree = BinarySearchTree()
# my_tree.insert(2)
# my_tree.insert(1)
# my_tree.insert(3)
# print(my_tree.root.value)
# print(my_tree.root.left.value)
# print(my_tree.root.right.value)
                
# Testing Contains
    
my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)
print(my_tree.contains(27))
print(my_tree.contains(17))