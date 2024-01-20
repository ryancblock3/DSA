class Node:
    def __init__(self, value):
        # Node class represents an element in the Stack with a value and a reference to the next node
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        # Stack class initializes with a starting value, creating a new node
        new_node = Node(value)
        # The top pointer points to the single node initially
        self.top = new_node
        # Height keeps track of the number of nodes in the stack (initially 1)
        self.height = 1

    def print_stack(self):
        # Print all elements in the stack
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        # Add a new node with the given value to the top of the stack
        new_node = Node(value)
        if self.height == 0:
            # If the stack is empty, set the top pointer to the new node
            self.top = new_node
        else:
            # Otherwise, add the new node to the top and update the top pointer
            new_node.next = self.top
            self.top = new_node
        # Increment the height of the stack
        self.height += 1
        return True  # Return True to indicate successful push
    
    def pop(self):
        # Remove and return the node from the top of the stack
        if self.height == 0:
            return None  # If the stack is empty, return None
        temp = self.top
        # Update the top pointer to the next node
        self.top = self.top.next
        temp.next = None
        # Decrement the height of the stack and return the removed node
        self.height -= 1
        return temp



# Testing Stack Constructor
            
# my_stack = Stack(4)
# my_stack.print_stack()
    
# Testing Push
    
# my_stack = Stack(2)
# my_stack.push(1)
# my_stack.print_stack()
    
# Testing Pop
    
# my_stack = Stack(7)
# my_stack.push(23)
# my_stack.push(3)
# my_stack.push(11)
# my_stack.pop()
# my_stack.print_stack()
        
