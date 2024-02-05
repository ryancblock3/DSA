# Node class represents a node in a singly linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  # Reference to the next node in the list

# LinkedList class represents a singly linked list
class LinkedList:
    def __init__(self, value):
        # Initialize a new linked list with a single node
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
            self.tail = new_node
        self.length += 1
        return True
    
    # Remove and return the last node from the linked list
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        # Traverse to the last node while updating references
        while temp.next is not None:
            pre = temp
            temp = temp.next
            self.tail = pre
            self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
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
            self.head = new_node
        self.length += 1
        return True
    
    # Remove and return the first node from the linked list
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    # Get the node at the specified index in the linked list
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
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
        temp = self.get(index - 1)
        # Update references to insert the new node at the specified index
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    # Remove and return the node at the specified index in the linked list
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            # If removing the first node, use the pop_first method
            return self.pop_first()
        if index == self.length -1:
            # If removing the last node, use the pop method
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        # Update references to remove the node at the specified index
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    # Reverse the linked list
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        # Reverse the direction of links while traversing the list
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


        
        
# Pre Append Testing #

# my_linked_list = LinkedList(2)
# my_linked_list.append(3)
# my_linked_list.prepend(1)
# my_linked_list.print_list()

# Pop First Testing #

# my_linkled_list = LinkedList(2)
# my_linkled_list.append(1)
# print(my_linkled_list.pop_first())
# print(my_linkled_list.pop_first())
# print(my_linkled_list.pop_first())

# Get Testing #

# my_linked_list = LinkedList(0)
# my_linked_list.append(1)
# my_linked_list.append(2)
# my_linked_list.append(3)
# print(my_linked_list.get(2))
    
# Set Testing #
    
# my_linked_list = LinkedList(11)
# my_linked_list.append(3)
# my_linked_list.append(23)
# my_linked_list.append(7)
# my_linked_list.set_value(1,4)
# my_linked_list.print_list()
    
# Insert Testing
    
# my_linked_list = LinkedList(0)
# my_linked_list.append(2)
# my_linked_list.insert(1,1)
# my_linked_list.print_list()
    
# Remove Testing
    
# my_linked_list = LinkedList(11)
# my_linked_list.append(3)
# my_linked_list.append(23)
# my_linked_list.append(7)
# print(my_linked_list.remove(2), '/n')
# my_linked_list.print_list()
            
# Reverse Testing
# my_linked_list = LinkedList(1)
# my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.append(4)
# my_linked_list.reverse()
# my_linked_list.print_list()