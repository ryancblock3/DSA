# Implementation of Data Structures

## Array (Chapter 10.1, 10.4, 13.16)

Array - Data structures that stores an ordered list of items, each item is directly accessible via index

## Linked list (doubly & singly linked) (Chapter 13.1,13.2,13.7,13.11,13.12,13.15,13.16)

List - ADT for holding ordered data

Common list operations -
- Append - insert at end of list
- Prepend - insert at start of list
- InsertAfter - insert after a defined index
- Remove - search and removes item from list
- Search - searches list for a defined item, returns if found, else returns null
- Print - prints lists items in order
- PrintReverse - prints lists items in reverse order
- Sort - sorts the lists items in ascending order
- IsEmpty - returns true if list has no items
- GetLength - returns the number of items in list

Singly Linked List - ADT where each node has data and a pointer to the next node. First node is called the head and the last node is called the tail.

Sigly Linked List Operations
 - Append - insert at end of list
    - Appened to empty list: If the lists head pointer is null the algorithm points the lists head and tail pointers to the new node
    - Append to non-empty list: If the lists head pointer is not null, the algorithm points the tail nodes next pointer and the lists tail pointer to the new node.
- Prepend - insert at the start of a list
    - Prepend to empty list: If the lists head pointer is null the algorithm points the lists head and tail pointers to the new node
    - Prepend to non-empty list: If the lists head is not null, the algorithm points the new nodes next pointer to the head node, and then points the lists head pointer to the new node.
- InsertAfter - inserts new node after a defined index. Uses curNode (current node) which is a pointer to an existing list node, but can be null when inserting into an empty list.
    - Insert as lists first node: If the head pointer is null, the algorithm points the lists head and tail pointers to the new node.
    - Insert After Lists Tail Node: If the lists head pointer is not null, and curNode points to the lists tail node the algorithm points the tail nodes next pointer and the lists tail pointer to the new node.
    - Insert in middle of list: If the lists head pointer is not null and curNode does not point to the lists tail node, the algorithm points the new nodes next pointer to curNodes next node and then points curNodes next pointer to the new node.
- RemoveAfter - removes the node after a defined list node. Also uses curNode parameter.
    - Remove lists head node (special case): If curNode is null, the algorithm, points to sucNode to the head nodes next node and points he lists head pointer to sucNode. If sucNode is null the only list node was removed, so the lists tail pointer is pointed to null
    - Remove node after curNode: If curNodes next pointer is not null (a node after curNode exists) the algorithm points sucNode to the node after curNode's next node. Then curNode's next pointer is pointed to sucNode. If sucNode is null, the list's tail node was removed, so the algorithm points the list's tail pointer to curNode (the new tail node).
- Search - returns the first node whose data matches that key, or returns null if a matching node was not found.

Doubly-Linked List - a data structure implements a list ADT, where each node has data, a pointer to the next node, and a pointer to the previous node.

Common Doubly-Linked List Operations
- Append - inserts the new node after the list's tail node
    - Append to empty list: If the list's head pointer is null (empty), the algorithm points the list's head and tail pointers to the new node.
    - Append to non-empty list: If the list's head pointer is not null (not empty), the algorithm points the tail node's next pointer to the new node, points the new node's previous pointer to the list's tail node, and points the list's tail pointer to the new node.
- Prepend - inserts the new node before the list's head node and points the head pointer to the new node
    - Prepend to empty list: If the list's head pointer is null (empty), the algorithm points the list's head and tail pointers to the new node.
    - Prepend to non-empty list: If the list's head pointer is not null (not empty), the algorithm points the new node's next pointer to the list's head node, points the list head node's previous pointer to the new node, and then points the list's head pointer to the new node.
- InsertAFter - inserts the new node after a provided existing list node. curNode is a pointer to an existing list node. The InsertAfter algorithm considers three insertion scenarios
    - Insert as first node: If the list's head pointer is null (list is empty), the algorithm points the list's head and tail pointers to the new node.
    - Insert after list's tail node: If the list's head pointer is not null (list is not empty) and curNode points to the list's tail node, the new node is inserted after the tail node. The algorithm points the tail node's next pointer to the new node, points the new node's previous pointer to the list's tail node, and then points the list's tail pointer to the new node.
    - Insert in middle of list: If the list's head pointer is not null (list is not empty) and curNode does not point to the list's tail node, the algorithm updates the current, new, and successor nodes' next and previous pointers to achieve the ordering {curNode newNode sucNode}, which requires four pointer updates: point the new node's next pointer to sucNode, point the new node's previous pointer to curNode, point curNode's next pointer to the new node, and point sucNode's previous pointer to the new node.
- Remove - removes a provided existing list node
    - Successor exists: If the successor node pointer is not null (successor exists), the algorithm points the successor's previous pointer to the predecessor node.
    - Predecessor exists: If the predecessor node pointer is not null (predecessor exists), the algorithm points the predecessor's next pointer to the successor node.
    - Removing list's head node: If curNode points to the list's head node, the algorithm points the list's head pointer to the successor node.
    - Removing list's tail node: If curNode points to the list's tail node, the algorithm points the list's tail pointer to the predecessor node.

## Stack operations (Chapter 14.1)

Stack - an ADT in which items are only inserted on or removed from the top of a stack

Stack Operations
- Push - inserts an item on the top of stack
- Pop - removes and returns item at top of stack
- Peek - Returns but does not remove item at top of stack
- IsEmpty - Returns true if stack has no items
- GetLength - Returns the number of items in stack

## Queue operations (push, pop, peek, enqueue, dequeue) (Chapter 14.4)

Queue - an ADT in which items are inserted at the end of the queue and removed from the front of the queue

Queue Operation
- Enqueue - Inserts item at the end of queue
- Dequeue - Returns and removes item at front of queue
- Peek - Returns but does not remove item at front of queue
- IsEmpty - Returns True if the queue has no items
- GetLength - Returns the number of items in the queue

## Deque operations (Chapter 14.8)

Deque - an ADT in which items can be inserted and removed at both the front and back.

Deque Operations
- PushFront - inserts item at the front of the deque
- PushBack - inserts item at the back of the deque
- PopFront - Returns and removes item at front of deque
- PopBack - Returns and removes item at back of deque
- PeekFront - Returns but does not remove item at front of deque
- PeekBack - Returns but does not remove item at back of deque
- IsEmpty - Returns true if deque is empty
- GetLength - Returns the number of items in the deque

## Hash table (Chapter 15)

Hash Table - A data structure that stores unordered items by mapping (or hashing) each item to a location in an array

Main advantage of a hash table is searching/inserting/removing and item may only be O(1)

Key - Value used to map to an index

Bucket - array element that the Hash Function sorts itms into.

Modulo Operator % - computes the integer remainder when dividing two numbers

Example - 20 element has table - key % 20 will map keys to a bucket indices 0 to 19

Collisions - Occurs when item being inserted into has table maps to the same bucket as an existing item in the hash table

Chaining - Collision resolution where each bucket has a list of items.

Open Addressing - Collision resolution where it is resolved by looking for an empty bucket elsewhere in the table

## Trees (leaf nodes, root, height) (Chapter 16)

Binary Tree - Each node has up to two children, known as left and right child.

Leaf - A tree node with no children

Internal Node - A node with at least one child

Parent - A node with a child is that childs parent

Ancestors - Include a nodes parent, parents parent, all the way up to the root

Root - The one tree node with no parent. The top node

Edge - the link between a node to a child

Depth - Number of edges on the path from the root to the node

Level - All nodes with the same depth

Height - The largest depth of any node

Full Tree - Every node contains either 0 or two children

Complete Tree - All levels except possibly hte last level contain all nodes and all nodes in the last level are as far left as possible

Perfect Tree - All internal nodes have 2 children and all leaf nodes are at the same level

## Heaps (Chapter 18)

Max Heap - Complete Binary Tree that maintains the simple property that a nodes key is greater than or equal to the nodes childrens keys

Insert - Starts by inserting the node in the trees last level, then swaps the node with the parent until no max heap property violation occurs.

Remove - Replaces the root with the last levels last node and swaps the node with its greatest chil until no max heap property violation occurs.

Min heap - opposite of max heap

Heaps are typically stored using arrays. Left to right, top to bottom. Root = index of 0, left child is index 1, right child is 2 and so on

## Sets (including: intersection) (Chapter 19.1 & 19.2)

Set - Collection of distinct elements

Add - Addes an element to the set, provided an equal element doesnt already exist

Key Value - primitive data value that serves as a unique identifier for the element

Sets distinguish elements based on key values

Union - of sets X and Y denoted as X ∪ Y, is a set that contains every element from X, every element from Y, and no additional elements. Commutative

Intersection - of sets X and Y, denoted as X ∩ Y, is a set that contains every element that is in both x and y, and no addional elements. Commutative

Difference - of sets X and Y, denoted as X \ Y, is a set that contains every elements that is in X but not in Y, and no additional elemetns. Non-Commutative

Filter - produces a subset containing only elements from x that satisfy a particular condition

Filter Predicate - Filtering condition

Map - On set X produces a new set by applying some function to each element

## Graph (vertices, adjacency) (Chapter 20)

Graph - Data structure for representing connections amoung items

Graphs consist of
1. Vertex (or node) - represents item in a graph
2. Edge - represents a connection between two vertices

Adjacent - Two vertices are adjacent if connected by an edge

Path - Sequence of edges leaading from a vertex to another vertex

Path Length - Number of edges in path

Distance - number of edges on the shortest path between two vertices

Adjacency list - graphical represntation showing each vertex and its list of adjacent vertices

Adjacency Matrices - Graphical representation where each vertex is assigned to a matrix row and column and a matric element is 1 if the corresponding two vertices have an edge, or is 0 otherwise

Breadth-First Search - is a traversal that visits a starting vertex, then all vertices of distance 1, then 2, and so on, without revisiting a vertex

Depth-First Search - is a traversal that visits a starting index, then visits every vertex along each path starting from that vertex to the paths end before backtracking

Directed Graph (digraph) - consists of vertices connected by directed edges

Directed Edge - connection between a starting vertex and a terminating vertex

Path - Sequence of directed edges leading from a source vertex to a destination vertex

Cycle - Path that starts and ends at the same vertex
    1. Cyclic if the graph contains a cycle
    2. Acyclic if the graph does not contain a cycle 

Weighted graph - Associates a weight with each edge.

Weight / Cost - represents some numerical value between vertex items, such as cost between airports. Can be directed or undirected.

Path Length (weighted) - sum of edge weights in a path

Cycle Length - sum of edge weights in a cycle

Negative Edge Weight Cycle - has a cycle length less than 0
