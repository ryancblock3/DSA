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
    
    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
    
    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    
    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)    
        self.__r_insert(self.root, value)

    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def __delete_node(self, current_node, value):
        if current_node == None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if current_node.left == None and current_node.right == None:
                return None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
        return current_node
    
    def delete_node(self, value):
        self.root = self.__delete_node(self.root, value)

    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop()
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results
    
    def dfs_pre_order(self):
        results = []
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results
    
    def dfs_post_order(self):
        results = []
        def traverse(current_node):    
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)
        traverse(self.root)
        return results
    
    def dfs_in_order(self):
        results = []
        def traverse(current_node):    
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results


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
    
# my_tree = BinarySearchTree()
# my_tree.insert(47)
# my_tree.insert(21)
# my_tree.insert(76)
# my_tree.insert(18)
# my_tree.insert(27)
# my_tree.insert(52)
# my_tree.insert(82)
# print(my_tree.contains(27))
# print(my_tree.contains(17))
    
#Testing Recursive Binary Search Tree
    
# my_tree = BinarySearchTree()
# my_tree.insert(47)
# my_tree.insert(21)
# my_tree.insert(76)
# my_tree.insert(18)
# my_tree.insert(27)
# my_tree.insert(52)
# my_tree.insert(82)

# print('BST Contains 27:')
# print(my_tree.r_contains(27))

# print('\nBST Contains 17:')
# print(my_tree.r_contains(17))

#Testing Recursive Insert

# my_tree = BinarySearchTree()
# my_tree.insert(2)
# my_tree.insert(1)
# my_tree.insert(3)
# print('Root:', my_tree.root.value)
# print('Root --> Left:', my_tree.root.left.value)
# print('Root --> Right:', my_tree.root.right.value)
        
# Testing Min Value
        
# my_tree = BinarySearchTree()
# my_tree.insert(47)
# my_tree.insert(21)
# my_tree.insert(76)
# my_tree.insert(18)
# my_tree.insert(27)
# my_tree.insert(52)
# my_tree.insert(82)
# print(my_tree.min_value(my_tree.root))
# print(my_tree.min_value(my_tree.root.right))3
        
# Testing Delete
        
# my_tree = BinarySearchTree()
# my_tree.insert(2)
# my_tree.insert(1)
# my_tree.insert(3)
# print('Root:', my_tree.root.value)
# print('Root --> Left:', my_tree.root.left.value)
# print('Root --> Right:', my_tree.root.right.value)
# my_tree.delete_node(2)
# print('Root:', my_tree.root.value)
# print('Root --> Left:', my_tree.root.left.value)
# print('Root --> Right:', my_tree.root.right.value) # Cant figure out why I am getting AttributeError
    
# Testing Breadth First Search
    
# my_tree = BinarySearchTree()
# my_tree.insert(47)
# my_tree.insert(21)
# my_tree.insert(76)
# my_tree.insert(18)
# my_tree.insert(27)
# my_tree.insert(52)
# my_tree.insert(82)
# print(my_tree.BFS())
    
# Testing Depth First Search Pre Order
    
# my_tree = BinarySearchTree()
# my_tree.insert(47)
# my_tree.insert(21)
# my_tree.insert(76)
# my_tree.insert(18)
# my_tree.insert(27)
# my_tree.insert(52)
# my_tree.insert(82)
# print(my_tree.dfs_pre_order())
    
# Testing Depth First Search Post Order
    
# my_tree = BinarySearchTree()
# my_tree.insert(47)
# my_tree.insert(21)
# my_tree.insert(76)
# my_tree.insert(18)
# my_tree.insert(27)
# my_tree.insert(52)
# my_tree.insert(82)
# print(my_tree.dfs_post_order())
    
# Testing Depth First Search In Order
    
# my_tree = BinarySearchTree()
# my_tree.insert(47)
# my_tree.insert(21)
# my_tree.insert(76)
# my_tree.insert(18)
# my_tree.insert(27)
# my_tree.insert(52)
# my_tree.insert(82)
# print(my_tree.dfs_in_order())