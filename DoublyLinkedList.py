# Node class represents a node in a doubly linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  # Reference to the next node in the list
        self.prev = None  # Reference to the previous node in the list

# DoublyLinkedList class represents a doubly linked list
class DoublyLinkedList:
    def __init__(self, value):
        # Initialize a new doubly linked list with a single node
        new_node = Node(value)
        self.head = new_node  # Head points to the first node
        self.tail = new_node  # Tail points to the last node
        self.length = 1  # Length of the linked list

    # Print the values of all nodes in the linked list
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # Append a new node with the given value to the end of the linked list
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            # If the list is empty, set the new node as both head and tail
            self.head = new_node
            self.tail = new_node
        else:
            # Otherwise, add the new node to the end and update references
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    # Remove and return the last node from the linked list
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            # If there's only one node, set head and tail to None
            self.head = None
            self.tail = None
        else:
            # Otherwise, update tail and remove references
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    # Add a new node with the given value to the beginning of the linked list
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            # If the list is empty, set the new node as both head and tail
            self.head = new_node
            self.tail = new_node
        else:
            # Otherwise, add the new node to the beginning and update references
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    # Remove and return the first node from the linked list
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            # If there's only one node, set head and tail to None
            self.head = None
            self.tail = None
        else:
            # Otherwise, update head and remove references
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    # Get the node at the specified index in the linked list
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            # Traverse from the beginning if the index is in the first half
            for _ in range(index):
                temp = temp.next
        else:
            # Traverse from the end if the index is in the second half
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
    
    # Set the value of the node at the specified index in the linked list
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    # Insert a new node with the given value at the specified index
    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            # If inserting at the beginning, use the prepend method
            return self.prepend(value)
        if index == self.length:
            # If inserting at the end, use the append method
            return self.append(value)
        new_node = Node(value)
        before = self.get(index-1)
        after = before.next
        # Update references to insert the new node at the specified index
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True
    
    # Remove and return the node at the specified index in the linked list
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            # If removing the first node, use the pop_first method
            return self.pop_first()
        if index == self.length - 1:
            # If removing the last node, use the pop method
            return self.pop()
        before = self.get(index - 1)
        after = self.get(index + 1)
        # Update references to remove the node at the specified index
        before.next = after
        after.prev = before
        self.length -= 1
        return 
    
    # Another method to remove and return the node at the specified index
    def remove_method_two(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            # If removing the first node, use the pop_first method
            return self.pop_first()
        if index == self.length - 1:
            # If removing the last node, use the pop method
            return self.pop()
        temp = self.get(index)
        # Update references to remove the node at the specified index
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp



# Testing Constructor

# my_doubly_linked_list = DoublyLinkedList(7)
# my_doubly_linked_list.print_list()
    
#Testing Appened

# my_doubly_linked_list = DoublyLinkedList(1)
# my_doubly_linked_list.append(2)
# my_doubly_linked_list.print_list()
    
# Testing Pop
    
# my_doubly_linked_list = DoublyLinkedList(1)
# my_doubly_linked_list.append(2)
# my_doubly_linked_list.print_list()
# my_doubly_linked_list.pop()
# my_doubly_linked_list.print_list()
    
# Testing Prepend
    
# my_doubly_linked_list = DoublyLinkedList(2)
# my_doubly_linked_list.append(3)
# my_doubly_linked_list.prepend(1)
# my_doubly_linked_list.print_list()
    
# Testing Pop First
    
# my_doubly_linked_list = DoublyLinkedList(2)
# my_doubly_linked_list.append(1)
# my_doubly_linked_list.pop_first()
# my_doubly_linked_list.print_list()
    
# Testing Get

# my_doubly_linked_list = DoublyLinkedList(0)
# my_doubly_linked_list.append(1)
# my_doubly_linked_list.append(2)
# my_doubly_linked_list.append(3)
# print(my_doubly_linked_list.get(1))
# print(my_doubly_linked_list.get(2))
    
# Testing Set_Value
    
# my_doubly_linked_list = DoublyLinkedList(11)
# my_doubly_linked_list.append(3)
# my_doubly_linked_list.append(23)
# my_doubly_linked_list.append(7)
# my_doubly_linked_list.set_value(1, 4)
# my_doubly_linked_list.print_list()
    
# Testing Insert
    
# my_doubly_linked_list = DoublyLinkedList(1)
# my_doubly_linked_list.append(3)
# my_doubly_linked_list.insert(1,2)
# my_doubly_linked_list.print_list()
    
# Texting Remove
    
# my_doubly_linked_list = DoublyLinkedList(1)
# my_doubly_linked_list.append(2)
# my_doubly_linked_list.append(3)
# my_doubly_linked_list.remove_method_two(2)
# my_doubly_linked_list.print_list()
