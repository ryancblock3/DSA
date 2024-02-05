# Sorting Algorithms

## Variable declaration (dynamic vs static) (Chapter 2)

An assignment statement assigns a variable with a value, such as x = 5. That statement means x is assigned with 5, and x keeps that value during subsequent statements, until x is assigned again.

Static variables, also known as class variables, have a fixed memory location throughout the execution of a program. They are declared within a class or a function and retain their values between function calls.

Dynamic variables, also referred to as instance variables, are allocated memory during runtime. Unlike static variables, dynamic variables have a memory location that changes as the program executes.

## Assignment operators (Chapter 2)

Assignment Operatiors
- = 
- +=
- -=
- *=
- /=
- %=
- //=
- **=
- &=
- |=
- ^=
- >>=
- <<=

## Types / List basics (Chapter 3.2)

Container - a construct used to group related values together and contains references to other objects instead of data

List - Container created by surrounding a sequence of variables or literals with brackets [].

Element - List items

Index - Position in list, starting with 0.

my_list = [] creates an empty list

append - add new elements to list

pop - remove element from list

remove - remove element from list

len - find length of list

list1 + list2 - Produce new list by concatenating list2 to the end of list1

min - find the list element with smallest value

max - find the list element with the largest value

sum - find the sum of all elements in list

list.index(val) - find the index of the first element in the list whose value matches val

list.count(val) - Count the number of occurrences of the value val in the list


## Order of operations / precedence rules (Chapter 2 & 4)

Order of Operations
1. ()
2. exponent **
3. unary -
4. * / %
5. + - 
6. left to right

Precedence
1. ()
2. * / % + -
3. << => >= == !=
4. not
5. and
6. or

## Loops (Chapter 24)

Loop - Program construct that repeatedly executes the loops statements while the loops expression is true, or when the expression is false, execution proceeds past the loop. Each time a loops statement is called an iteration.

While loop - repeatedly executes an indented block of code as long as the loops expression is True

For Loop - loops over each element in a container one at a time assigning a variable with the next element that can then be used for the loop body

range() - generates a sequence of integers between a starting int that is included in the range, an ending interget that is not included in the range, and an integer step value

Nested Loop - a loop that appears as part of the body of another loop. Outer/Inner loop.

Break - Causes the loop to exit immediately

Continue - causes an immediate jump to the while or for loop header statement

Else - executes if the loop completes normally

enumerate - retrieves both the index and correspoinding element value at the same time, providing a cleaner and more readable solution

## Conditional statements / branching (Chapter 4)

Branch is a sequence of statements only executed under a certain condition.

If-Else branch has two branches
First branch is executed if expression is true
Else the other branch is executed

Three or more branches can be executed by using If-elseif-else branches

Equality operatior = (==)

Inequaluty operator = (!=)

Boolean = True or False

If-else executes one group of statements when an expression is true, and another group when the expression is false.

Multi-branch if-else statements use elif if there are multiple if statements. Each expression is checked in sequence. As soon as one branch's expression is found to be True, that branch executes and no other branch is considered. If no statement is true the else statement is executed.

if

elif

else

Logical operators treat operands as True or False, and evaluates them.

AND - both operands are True

OR - at least one operand is True

NOT - True when one operand is False

Common use of logical operators is to dectect if a value is within a range.

Boolean operators - must be capitalized like True & False

and - both true

or - at least one true

not - at least one false

Can use logical operators to detect ranges. Multi branch if else statements can be used without gaps.

Relational and equality operators work for integer, string, and floating-point, although floating-point should not be used due to imprecise representation of floating-point numbers.

Numbers are arithmetically compared

Strings are compared by converting each character to a numerical value

Lists & Tuples are compared by ordered comparison of every element in the sequence.

Dictionaries are only compared with == and 1=

Common errors-
= instead of == 
=> instead of >=
!> 
<>

in and not in operators are known as membership operators, they yeild a True or False

Membership operators can be used to check if a string is a substring, or matching subset of characters of a larger string. For example 'abc' in '123abcd' returns true.

is and is not are Identity Operators 
x is y is True
x is not y is False

"==" is not the same as an identity operator

Code block - series of statements grouped together.

Code blocks are defined by indentation level.

DONT mix tabs and spaces.

Acceptable number of columns of text is 80-120 but leans more heavily towards 80 columns.

One tab == 4 spaces

Conditional expressions have the following form

expr_when_true if condition else expre_when_false

Conditional expressions has three operands and are reffered to as ternary operation.

Common practice is to restrict usage of conditional expressions as it is difficult to read and comprehend.

## Classes (Chapter 7)

Object - Group of data (variables) and operations that can be performed on that data (functions or methods)

Abstractions - when a user interacts with an object at a high level, hiding lower-level internal details. 

Abstraction is also known as information hiding or encapsulation

Abstract Data Type - a data type whose creation and update are constrained to specific well-defined operations.

Objects maintain a set of attributes that determines that data and behavior of a class

This can be used to instantiate a class by using parentheses such as
my_time = Time()

This creates and instance which is an individual object of the given class.

Instantiation operation automatically calls the __init__ method.

__init__ is commonly known as the constructor and is responsible for setting up the initial state of a new instance

__init__ has a single parameter "self" that automatically references the instance being created.

Multiple instances of a class can be created using different atribute values

time1 = time()
time1.hours = 7
time1.minutes = 30

time2 = time()
time2.hours = 12
time2.minutes = 45

Class object - A 'factory' that creates instance onjects.

Class attribute - shared among all instance of that class

Instance Atrribute - can be unique to each instance

Class Interface - Consists of the methods that a programmer calls to create, modify, or access a class instance

Classes can contain methods used internally that a user of the class need not access. 

Memory Allocation - Process of an application requesting and being granted memory

Memory Deallocation - act of freeing the memory that stores variables or objects in a program.

In python objects are automatically deallocated.

Reference Count - Integer counter that represents how many variables reference an object.

Once reference count is 0 the garbage collector deallocates the memory

## Linear search (Chapter 9)

Linear Search - a search algo that starts of the beginning of a list and checks each element until the key is found or the end of list is reached.

## Binary search (Chapter 9)

Binary search first checks the middle element of a list, and continues until the element is found

Binary Search is defined as a searching algorithm used in a **sorted array** by repeatedly dividing the search interval in half. The idea of a binary search is to use the information that the array is sorted and reduce the time complexity to O(log N).

![gif of a binary search](https://d18l82el6cdm1i.cloudfront.net/uploads/bePceUMnSG-binary_search_gif.gif)

## Big O growth rate O(1), O(n), O(log n), O(n log n), O(n^2) (Chapter 9.3)

Big O Notation - mathematical way of describing how a function behaves in relation to the input size.

![big O complexity chart](https://www.researchgate.net/publication/371457259/figure/fig3/AS:11431281166794429@1686405800300/Big-O-time-complexity-chart-based-feature-selection-a-Big-O-complexity-chart-b-Time.ppm)

Big O, also known as Big O notation, represents an algorithm's worst-case complexity. It uses algebraic terms to describe the complexity of an algorithm.

Big O defines the runtime required to execute an algorithm by identifying how the performance of your algorithm will change as the input size grows but does not tell you how fast your algorithm's runtime is.

- O(1) - Excellent/Best
- O(log n) - Good
- O(n) - Fair
- O(n log n) - Bad
- O(n^2), O(2^n), and O(n!) - Horrible/Worst

[Growth rates for different input sizes](./images/growth-rates.png)

## Sorting algorithms (Chapter 9.5 – 9.9, 12)

## Selection Sort

[Python Code Example](/SelectionSort.py)

![gif of selection sort](https://miro.medium.com/v2/resize:fit:1144/1*5WXRN62ddiM_Gcf4GDdCZg.gif)

Selection Sort is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list.

Selection Sort has the advantage of being easy to code as it involves only one nested loop.

Average Complexity - O(n^2)
Best Case - O(n^2)
**Worst Case - O(n^2)**
Space Complexity - O(1)

## Insertion Sort

[Python Code Example](/InsertionSort.py)

![gif of insertion sort](https://miro.medium.com/v2/resize:fit:1012/1*JP-wURjwf4k23U2G3GNQDw.gif)

Insertion sort is a simple sorting algorithm that works similarly to the way you sort playing cards with your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position when sorted.

To sort an array of size N in ascending order, iterate over the array and compare the current element (key) to its predecessor. If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.

Average Complexity - O(n^2)
Best Case - O(n)
**Worst Case - O(n^2)**
Space Complexity - O(1)

Nearly sorted only contains a few elements that are not in sorted order
Insertion Sort's runtime for nearly sorted lists is O(N)

## Quick Sort

[Python Code Example](/QuickSort.py)

![gif of quick sort](https://colab.research.google.com/drive/1vCuxn8JGjaM6l_0NMbqb1Zx0_2bf3AqU)

Quick Sort is a sorting algorithm based on the divide and conquer algorithm that picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array.

The key to quick sort is partitioning. The target of partitions is to place the pivot (any element can be chosen to be a pivot) at its correct position in the sorted array and put smaller elements to the left of the pivot and all greater elements to the right of the pivot.

Partition is done recursively on each side of the pivot after the pivot is placed in its correct position, and this finally sorts the array.

Average Complexity - O(n x log n)
Best Case - O(n x log n)
**Worst Case -O(n^2)**
Space Complexity - O(n)

## Merge Sort

[Python Code Example](/Merge.py)

![gif of merge sort](https://codepumpkin.com/wp-content/uploads/2017/10/MergeSort_Avg_case.gif)

Merge Sort is defined as a sorting algorithm that works by dividing an array into smaller subarrays, sorting each subarray, and then merging the sorted subarrays back together to form the final sorted array.

Average Complexity - O(n x log n)
Best Case - O(n x log n)
**Worst Case -O(n x log n)**
Space Complexity - O(n)

## Data structures – arrays, linked list, heap, etc (Chapter 10)

Data Structure - Way of organizing, storing, and performing operations on data.

Record - Data structure that stores subitems

Array - Data structures that stores an ordered list of items

Linked List - stores an ordered list of items in nodes where each node stores data and has a pointer to the next node

Binary Tree - DS which each node stores data and has up to two dchildren, know as a left child and a right child

Hash Table - DS that stores unordered items by mapping or hashing each item to a location in an array

Heap - A max heap is a tree that maintains the simple property that a nodes key is greater than or equal to the nodes childrens keys. A min heap is a tree that maintains the simple property that a nodes key is less than or equal to the nodes children keys

Graph - A DS for representing connections among item, and consists of vertices connected by edges. A **vertex** represents an item in a graph. An edge represents a connection between two vertices in a graph.

## ADTs - stack, deque, list, queue, etc. (Chapter 10)

Stack - ADT where items are only inserted and removed from top of stack.

Push - insert object to top of stack

Pop - remove object off top of stack

Peek - Look at item at top of stack but dont remove it

isEmpty - returns True if stack is empty

GetLength - returns the number of items in the stack

Last-in First-out

Queue - ADT where items are inserted at the end and removed from the front

Enqueue - insert item at end of a queue

Dequeue - removes and returns the item at the front of the queue.

Peek - returns but does not remove item at the front of queue

IsEmpty - returns true if queue has no items

GetLength - Returns the number of items in the queue.

First-in First-out

## Time complexity, worst case, efficiency analysis (Chapter 10)

Algorithm Efficiency is meausred by the algorithms compuatuinal complexity

Compuatational Complexity is the amount of resources used by the algorithm.

Runtime complexity is a function T(N) that represents the number of constat time operations that are performed by the algo on an imput size of N.

Best Case - Least possible number of operations

Worst Case - Most possible number of operations

Space Complexity - is a function S(N) that represents the number of fixed-size memory units used by the algo for an input size of N

Auxiliary Space Complexity - the space complexity not including the data.

## Methods for list (Chapter 13.1)

my_list = [] creates an empty list

append - add new elements to list

pop - remove element from list

remove - remove element from list

len - find length of list

list1 + list2 - Produce new list by concatenating list2 to the end of list1

min - find the list element with smallest value

max - find the list element with the largest value

sum - find the sum of all elements in list

list.index(val) - find the index of the first element in the list whose value matches val

list.count(val) - Count the number of occurrences of the value val in the list

## Stack operations (Chapter 14.1)

Stack Operations
- Push - inserts an item on the top of stack
- Pop - removes and returns item at top of stack
- Peek - Returns but does not remove item at top of stack
- IsEmpty - Returns true if stack has no items
- GetLength - Returns the number of items in stack

## Deque operations (Chapter 14.8)

Deque Operations
- PushFront - inserts item at the front of the deque
- PushBack - inserts item at the back of the deque
- PopFront - Returns and removes item at front of deque
- PopBack - Returns and removes item at back of deque
- PeekFront - Returns but does not remove item at front of deque
- PeekBack - Returns but does not remove item at back of deque
- IsEmpty - Returns true if deque is empty
- GetLength - Returns the number of items in the deque
