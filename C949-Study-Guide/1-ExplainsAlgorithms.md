# Factors of an Algorithm

1. **Modularity** - This feature was perfectly designed for the algorithm if you are given a problem and break it down into small-small modules or small-small steps, which is a basic definition of an algorithm.

2. **Correctness** - An algorithm's correctness is defined as when the given inputs produce the desired output, indicating that the algorithm was designed correctly. An algorithm's analysis has been completed correctly.

3. **Maintainability** - It means that the algorithm should be designed in a straightforward structured way so that when you redefine the algorithm, no significant changes are made to the algorithm.

4. **Functionality** - It takes into account various logical steps to solve a real-world problem.

5. **Robustness** - Robustness refers to an algorithm's ability to define your problem clearly.

6. **User-Friendly** - If the algorithm is difficult to understand, the designer will not explain it to the programmer.

7. **Simplicity** - If an algorithm is simple, it is simple to understand.

8. **Extensibility** - Your algorithm should be extensible if another algorithm designer or programmer wants to use it.

---

# Characteristics of an Algorithm

## Well-Defined Inputs

1. The expected inputs of an algorithm must be well-defined to ensure its correctness, predictability, and repeatability.

2. Well-defined inputs ensure that the algorithm's behavior is deterministic, meaning the same input will always produce the same output.

3. Unambiguous inputs help prevent incorrect implementations and misunderstanding of the algorithm's requirements.

4. With well-defined inputs, it is easier to optimize the algorithm based on the characteristics of the input.

## Well-Defined Outputs

1. The outputs of an algorithm should be well-defined to ensure that the algorithm produces the intended and accurate result for a given set of inputs.

2. It avoids ambiguity and guarantees that the algorithm solves the problem correctly.

3. It is also easy to verify the correctness of the algorithm's implementation.

4. Well-defined outputs allow you to optimize the algorithm further to achieve the results more efficiently.

## Unambiguity

1. Ambiguity is the algorithm's description can lead to incorrect implementations and unreliable results. That is why it is important for an algorithm to be unambiguous.

2. It allows the algorithm to be predictable, i.e., the same input produces the same output, making debugging an implementation easier.

3. It is also easier for unambiguous algorithms to be standardized and used widely for different applications.

4. While implementing unambiguous algorithms, you can focus more on optimizations rather than handling unexpected errors and edge cases.

## Finiteness

1. The algorithm should end after a finite amount of time, and it should have a limited number of instructions.

2. A finite algorithm ensures that it will eventually stop executing and produce a result.

3. An infinite algorithm would never reach a conclusion, which is impractical in real-world scenarios where computation cannot be performed indefinitely.

4. The time and space complexity can be analyzed in the case of a finite algorithm, which is important for performing further optimizations.

## Language Independence

1. A language-independent algorithm can be easily ported to different programming languages and platforms, making it more adaptable and usable across various environments.

2. Being language-independent also makes an algorithm future-proof, which means it can be implemented easily using newer programming languages.

3. It is important for algorithms to be language-independent in educational settings where students are exposed to different programming languages.

4. It also makes it easier to compare the algorithm's performance using different programming languages.

## Effectiveness and Feasibility

1. An algorithm should be feasible because feasibility indicates that it is practical and capable of being executed within reasonable constraints and resources.

2. It also avoids excessive execution times, which can make an algorithm unusable in real-world scenarios.

3. Feasible algorithms can be easily implemented using existing hardware infrastructure without using specialized resources.

4. They are adopted easily for usage across fields due to their practical hardware requirements.

# Data Flow Diagramming

## What is a data flow diagram?

A data flow diagram shows the way information flows through a process or system. It includes data inputs and outputs, data stores, and the various subprocesses the data moves through. DFDs are built using standardized symbols and notation to describe various entities and their relationships.

![img of a data flow diagram](https://d2slcw3kip6qmk.cloudfront.net/marketing/pages/chart/seo/data-flow-diagram/discovery/data-flow-diagram-7.svg)

## Physical and Logical Data Flow Diagrams

Logical data flow diagrams focus on **what** happens in a particular information flow.

Physical data flow diagrams focus on **how** things happen in an information flow.

## Data Flow Diagram Levels

1. Level 0 DFDs - Also known as context diagrams, are the most basic data flow diagrams. They provide a broad view that is easily digestible but offers little detail.

2. Level 1 DFDs - Are still a general overview but they go into more detail than a context diagram.

3. Level 2+ DFDs - simple break processes down into more detailed sub-processes.

# Classes

![img breaking down classes](https://miro.medium.com/v2/resize:fit:828/format:webp/1*NxXw72-CDGp7b7pz2kga5g.png)

A class is a user-defined blueprint or prototype from which objects are created.

# Recursive Algorithms

[Recursive Algorithm Example](/Recursion.py)

## What is Recursion?

Recursive algorithm calls itself with smaller input values and returns the result for the current input by carrying out basic operations on the returned value for the smaller input.

## Recursive Algorithm requirements

1. Base case - The simplest instance of a problem, consisting of a condition that terminates the recursive function. This base case evaluates the result when a given condition is met.

2. Recursive Step - It computes the result by making recursive calls to the same function, but with the inputs decreased in size or complexity.

## Call Stack

Programming languages use call stacks to manage the invocation of recursive functions. Like a stack, a call stack for a recursive functions calls the last function in its stack when the base case is met.

![gif of a call stack iterating through a recursive function](https://content.codecademy.com/practice/art-for-practice/stackcall.gif)

# Linear Search

Linear search is defined as a sequential search algorithm that starts at one end and goes through each element of a list until the desired element is found; otherwise, the search continues until the end of the data set.

![gif of a linear search](https://www.tutorialspoint.com/data_structures_algorithms/images/linear_search.gif)

# Binary Search

Binary Search is defined as a searching algorithm used in a **sorted array** by repeatedly dividing the search interval in half. The idea of a binary search is to use the information that the array is sorted and reduce the time complexity to O(log N).

![gif of a binary search](https://d18l82el6cdm1i.cloudfront.net/uploads/bePceUMnSG-binary_search_gif.gif)

# Sorting Algorithms

[Good Resource - Sort Visualizer](https://www.sortvisualizer.com/)

## Selection Sort

[Python Code Example](/SelectionSort.py)

![gif of selection sort](https://miro.medium.com/v2/resize:fit:1144/1*5WXRN62ddiM_Gcf4GDdCZg.gif)

Selection Sort is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list.

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

## Bubble Sort

[Python Code Example](/BubbleSort.py)

![gif of bubble sort](https://miro.medium.com/v2/resize:fit:1400/1*-qR66X2iwdcjhaqq10y9JQ.gif)

Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. This algorithm is not suitable for large data sets as its average and worst-case time complexity is high.

In Bubble Sort algorithm:

- Traverse from left and compare adjacent elements, and the higher one is placed at the right side.
- In this way, the largest element is moved to the rightmost end at first.
- This process is then continued to find the second-largest and place it, and so on until the data is sorted.

Average Complexity - O(n^2)
Best Case - O(n)
**Worst Case -O(n^2)**
Space Complexity - O(1)

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

## Heap Sort

![gif of heap sort](https://upload.wikimedia.org/wikipedia/commons/f/fe/Heap_sort_example.gif)

Heap sort is a comparison-based sorting technique based on the binary heap data structure. It is similar to the selection sort where we first find the minimum element and place the min at the beginning. Repeat the same process for the remaining elements.

First convert the array into the heap data structure using heapify, then one by one delete the root node of the max-heap and replace it with the last node in the heap and then heapify the root of the heap. Repeat this process until the size of the heap is greater than 1.

Average Complexity - O(n x log n)
Best Case - O(n x log n)
**Worst Case -O(n x log n)**
Space Complexity - O(1)

## Radix Sort

Radix sort is a linear sorting algorithm that sorts elements by processing them digit by digit. It is an efficient sorting algorithm for integers or strings with fixed-size keys.

**Worst Case -O(nk), where k is the # of digits in the largest number in the array.**

# Big O

## Time complexity

![big O complexity chart](https://www.researchgate.net/publication/371457259/figure/fig3/AS:11431281166794429@1686405800300/Big-O-time-complexity-chart-based-feature-selection-a-Big-O-complexity-chart-b-Time.ppm)

Big O, also known as Big O notation, represents an algorithm's worst-case complexity. It uses algebraic terms to describe the complexity of an algorithm.

Big O defines the runtime required to execute an algorithm by identifying how the performance of your algorithm will change as the input size grows but does not tell you how fast your algorithm's runtime is.

- O(1) - Excellent/Best
- O(log n) - Good
- O(n) - Fair
- O(n log n) - Bad
- O(n^2), O(2^n), and O(n!) - Horrible/Worst

# Data Structures

1. **Array** - A data structure that stores a fixed-size sequential collection of elements of the same type. Elements in an array can be accessed using their index, which starts from 0.

![Array Data Structure](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20230726162247/Array-data-structure.png)

2. **Linked List** - A data structure consisting of a sequence of nodes, each containing an element and a reference to the next node. Linked lists can be used to implement dynamic data structures, where the size of the data changes frequently.
d
![Linked List Data Structure](https://media.geeksforgeeks.org/wp-content/uploads/20220829110944/LLdrawio.png)

3. **Binary Search Tree** - A binary tree is a data structure where each node has at most two children, and the left child is always less than its parent, while the right child is always greater than its parent. Binary search trees are commonly used for searching and storing operations.

![Binary Search Tree Data Structure](https://miro.medium.com/v2/resize:fit:1194/0*OJaD7DmFOVdgFfiZ.png)

4. **Hash Table** - A data structure that uses a hash function to map keys to indices of an array, where values associated with the keys can be stored. Hash tables provide constant-time average case for basic operations such as insert, delete, and search.

![Hash Table Data Structure](https://cdn.sanity.io/images/kuana2sp/production/c015c55fca5c286607aff134760bb35e5d54db32-1011x704.webp)

5. **Heap** - A binary tree data structure where the parent nodes are always greater (or less) than their children. Heaps are used to implement priority queues, where the highest (or lowest) priority element is always at the root of the heap.

![Heap Data Structure](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20221220165711/MinHeapAndMaxHeap1.png)

