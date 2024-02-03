# Stacks and Queues

## Stack Abstract Data Type

Stack - ADT where items are only inserted and removed from top of stack.

Push - insert object to top of stack

Pop - remove object off top of stack

Peek - Look at item at top of stack but dont remove it

isEmpty - returns True if stack is empty

GetLength - returns the number of items in the stack

Last-in First-out

## Stacks Using Linked Lists

A stack is often created with a linked list. Push is performed with prepend and pop is performed with removing the head node

## Python: Array-Based Stacks

A stack can also be implemented with an array with the two following variables 
1. allocationSize - an int for the arrays allocated size
2. length - an int for the stacks length

Unbounded Stack - stack with no upper limit on length

Bounded Stack - stack with upper limit, this the array cannot resize

Full - A bounded stack with equal to the max length

### Unbound Stack

class Stack:
    def __init__(self):
        self.stack_list = []
    
    def pop(self):
        return self.stack_list.pop()
    
    def push(self, item):
        self.stack_list.append(item)

### Bound Stack

class Stack:
    # Initializes the stack. If the optional_max_length argument is omitted or 
    # negative, the stack is unbounded. If optional_max_length is non-negative, 
    # the stack is bounded.
    def __init__(self, optional_max_length = -1):
        self.stack_list = []
        self.max_length = optional_max_length
    #
    # Pops and returns the stack's top item.
    def pop(self):
        return self.stack_list.pop()
    #
    # Pushes an item, provided the push doesn't exceed bounds. Does nothing 
    # otherwise. Returns True if the push occurred, False otherwise.
    def push(self, item):
        # If at max length, return false
        if len(self.stack_list) == self.max_length:
            return False
        #
        # If unbounded, or bounded and not yet at max length, then push
        self.stack_list.append(item)
        return True



## Queue Abstract Data Type

Queue - ADT where items are inserted at the end and removed from the front

Enqueue - insert item at end of a queue

Dequeue - removes and returns the item at the front of the queue.

Peek - returns but does not remove item at the front of queue

IsEmpty - returns true if queue has no items

GetLength - Returns the number of items in the queue.

First-in First-out

## Queues Using Linked Lists

Linked lists are often used for implementing a stack where the head node is the queues front and the tail node is the queues end. 

Enqueue = append

Dequeue = removing head node

## Python: Array Based Queues

Arrays can be used to implement a queue with the following variables
1. Length - an int for the queues length
2. front_index - an int for the front item index

Bounded Queues - Queue with a max length

Unbounded Queue - Queue without a max length, can grow indefinitely

## Python: Stacks and Queues Using Linked Lists

[Stack Python Code](../Stacks.py)

[Queue Python Code](../Queues.py)

## Deque Abstract Data Type

Deque (pronounced "deck", short for double ended queue) - ADT which items can be inserted and removed at both the front and the back

PushFront - inserts item at front of the deque

PushBack - inserts item at the back of the deque

PopFront - removes and returns item at front of deque

PopBack - removes and returns item at back of deque

PeekFront - returns but does not remove item at front of deque

PeekBack - returns but does not remove item at back of deque

isEmpty - Returns True if deque is empty

GetLength - Returns the number of items in deque

