# Lists

## List Abstract Data Type

List is a common ADT for holding ordered data

Append(list, x) - inserts x at end of list
Prepend(list, x) - inserts x at start of list
InsertAfter(list, w, x) - inserts x after w
Remove(list, x) - removes x
Search(list, x) - returns item if found, else null
Print(list) - prints lists items in order
PrintReverse(list) - prints lists items in reverse order
Sort(list) - sorts the lists in ascending order
IsEmpty(list) - Returns true if list has no items
GetLength(list) - Returns the number of elements in the list

## Singly-linked Lists

Singly Linked Lists is a list ADT where each node has a data and a pointer to the next node

Head - first node
Tail - last node

Singly Linked Lists are a type of positional lists where elements contain pointers to the next and or previous elements

Append inserts new node after the list's tail

Prepend inserts new node to the list's head

## Singly-linked Lists: Insert

InsertAfter inserts a new node after a provided existing list node 

## Singly-linked Lists: Remove

RemoveAfter removes the node after the specified list node

## Linked List Search

Search algo returns the first node whose data matched that key or returns null if that matching node was not found

## Python: Singly Linked Lists

[See LinkedList.py](../LinkedList.py)

## Doubly-linked Lists

Doubly linked list - ADT where each node has data, a pointer to the next node, and a pointer to the previous node.

Positionaly Indexed

Has head and tail

Append inserts a new node at the tail

Prepend inserts a new node at the head

## Doubly-linked Lists: Insert

InsertAfter inserts the new node after a provided existing list node

## Doubly-linked Lists: Remove

Remove removes a provided existing list node
curNode > existing list node
sucNode > nodes successor
predNode > nodes predecessor

## Python: Doubly-linked Lists

[See DoublyLinkedList.py](../DoublyLinkedList.py)

insert_after() inserts node after a specified node

remove() unlinks a given node from list and joining prev and next node pointers

## Linked List Traversal

List traversal visits all nodes and performs an operation on each node. A common example is printing all nodes.

ListTraverse(list) {
   curNode = list⇢head // Start at head

   while (curNode is not null) { 
      Print curNode's data        
      curNode = curNode⇢next
   }
}

Reverse Traversal visits all nodes with the tail node first and end at the head.

ListTraverseReverse(list) {
   curNode = list⇢tail // Start at tail

   while (curNode is not null) { 
      Print curNode's data        
      curNode = curNode⇢prev
   }
}

## Sorting Linked Lists

Insertion sort works similarly to the insertion sort algo used for arrays, but does not work on singly linked lists as backwards traversal is not possible.

Insertion sort can be changed to work with singly linked lists by traversing the liost from the head toward the current element.

Linked lists do not allow indexed access, therefore it is difficult for sorting algorithms to operate on linked lists.

Insertion sort and merge sort are more easily adapted to sort linked lists than shell sort, quick sort, and heap sort.

## Python: Sorting Linked Lists

Insertion sort visits all nodes and shifts the nodes backward to be placed in the correct sorted positions in doubly linked lists

def insertion_sort_doubly_linked(self):
    current_node = self.head.next
    while current_node != None:
        next_node = current_node.next
        search_node = current_node.prev
         
        while ((search_node != None) and 
               (search_node.data > current_node.data)):
            search_node = search_node.prev
      
        # Remove and re-insert curNode
        self.remove(current_node)
            
        if search_node == None:
            current_node.prev = None
            self.prepend(current_node)      
        else:
            self.insert_after(search_node, current_node)

        # Advance to next node
        current_node = next_node

from LinkedList import LinkedList
from Node import Node

num_list = LinkedList() 
node_a = Node(72)
node_b = Node(91)
node_c = Node(53)
node_d = Node(12)

num_list.append(node_a)
num_list.append(node_b)
num_list.append(node_c)
num_list.append(node_d)

 Output list
print('List after adding nodes:', end=' ')
node = num_list.head
while node != None:
    print(node.data, end=' ')
    node = node.next
print()

num_list.insertion_sort_doubly_linked()

 Output list
print('List after insertion sort:', end=' ')
node = num_list.head
while node != None:
    print(node.data, end=' ')
    node = node.next
print()

## Linked List Dummy Nodes

Dummy nodes (or header nodes) is a node with unused data member that always resides at the head of the list and cannot be removed.

When a singly linked list with a dummy node is created the dummy node is allocated and the lists head tand tail pointers point to the dummy node.

In a doubly linked list the dummy node always has the prev pointer set to null 

ListRemove does not allow for removal of the dummy node.

## Linked Lists: Recursion

Forward traversal through a linked list can be implemented with rescursion.

Recursion can be used with searching similar to forward traversal where each call examines one node.

## Array-Based Lists

Array Based List ADT supports common ADT operations such as prepend, insert after, remove, and search

Array have a fixed size and need to be dynamically allocated as needed as the number of elements change

Resize is called when size = length, where resize will allocate a new array twice the size of the current length commonly. this is O(N) because all elements need to be copied to another array.

## Python: Array-Based List

Python's List is an array-based data structure