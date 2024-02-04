# Heaps and Treaps

## Heaps

Max Heap - Complete Binary Tree that maintains the simple property that a nodes key is greater than or equal to the nodes childrens keys

Insert - Starts by inserting the node in the trees last level, then swaps the node with the parent until no max heap property violation occurs.

Remove - Replaces the root with the last levels last node and swaps the node with its greatest chil until no max heap property violation occurs.

Min heap - opposite of max heap

## Heaps Using Arrays

Heaps are typically stored using arrays. Left to right, top to bottom. Root = index of 0, left child is index 1, right child is 2 and so on

## Python: Heaps

Array Implementation is efficient because the tree is nearly full. This means that the root index will always be 0 and the index of any nodes parent and children can be calculated easily.
1. parent_index = (node_index - 1) // 2
2. left_child_index = 2 * node_index + 1
3. right_child_index = 2 * node_index + 2

MaxHeap methods insert() and remove() make use of percolate_up() and percolate_down()

## Heap Sort

HeapSort - sorting algorithm that takes advantage of max-heaps properties by repeatedly removing the max and building a sorted array in reverse order.

Heapify - used to turn an array into a heap

## Python: Heap Sort

# Binary max heap percolate down
def max_heap_percolate_down(node_index, heap_list, list_size):
    child_index = 2 * node_index + 1
    value = heap_list[node_index]

    while child_index < list_size:
        # Find the max among the node and all the node's children
        max_value = value
        max_index = -1
        i = 0
        while i < 2 and i + child_index < list_size:
            if heap_list[i + child_index] > max_value:
                max_value = heap_list[i + child_index]
                max_index = i + child_index
            i = i + 1
                                    
        if max_value == value:
            return

        # Swap heap_list[node_index] and heap_list[max_index]
        temp = heap_list[node_index]
        heap_list[node_index] = heap_list[max_index]
        heap_list[max_index] = temp
        
        node_index = max_index
        child_index = 2 * node_index + 1


# Sorts the list of numbers using the heap sort algorithm
def heap_sort(numbers):
    # Heapify numbers list
    i = len(numbers) // 2 - 1
    while i >= 0:
        max_heap_percolate_down(i, numbers, len(numbers))
        i = i - 1
                
    i = len(numbers) - 1
    while i > 0:
        # Swap numbers[0] and numbers[i]
        temp = numbers[0]
        numbers[0] = numbers[i]
        numbers[i] = temp

        max_heap_percolate_down(0, numbers, i)
        i = i - 1

## Priority Queue Abstract Data Type

Priority Queue is a queue where each item has a priority and item with higher priority are closer to the front of the queue.

Enqueu operation inserts an item such that the item is closer to the front than all items with a lower priority

Dequeue operation removes and returns the item at the front of the queue, which also has the highest priority

## Treaps

A treap is a balanced binary search tree that maintains near-min height by randomizing the order of insertions.