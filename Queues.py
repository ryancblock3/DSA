class Node:
    def __init__(self, value):
        # Node class represents an element in the Queue with a value and a reference to the next node
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        # Queue class initializes with a starting value, creating a new node
        new_node = Node(value)
        # The first and last pointers point to the single node initially
        self.first = new_node
        self.last = new_node
        # Length keeps track of the number of nodes in the queue (initially 1)
        self.length = 1

    def print_queue(self):
        # Print all elements in the queue
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        # Add a new node with the given value to the end of the queue
        new_node = Node(value)
        if self.first is None:
            # If the queue is empty, set both first and last pointers to the new node
            self.first = new_node
            self.last = new_node
        else:
            # Otherwise, add the new node to the end and update the last pointer
            self.last.next = new_node
            self.last = new_node
        # Increment the length of the queue
        self.length += 1

    def dequeue(self):
        # Remove and return the node from the front of the queue
        if self.length == 0:
            return None  # If the queue is empty, return None
        temp = self.first
        if self.length == 1:
            # If there is only one node, set both first and last pointers to None
            self.first = None
            self.last = None
        else:
            # Otherwise, update the first pointer to the next node
            self.first = self.first.next
            temp.next = None
        # Decrement the length of the queue and return the removed node
        self.length -= 1
        return temp


# Testing Constructor
        
# my_queue = Queue(4)
# my_queue.print_queue()
        
# Testing enqueue
        
# my_queue = Queue(1)
# my_queue.enqueue(2)
# my_queue.print_queue()
    
# Testing Dequeue
    
# my_queue = Queue(1)
# my_queue.enqueue(2)
# my_queue.dequeue()
# my_queue.print_queue()

