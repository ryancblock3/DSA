# Searching and Sorting Algorithms

## Searching and Algorithms

Algorithm - sequence of steps for accomplishing a task

Linear Search - a search algo that starts of the beginning of a list and checks each element until the key is found or the end of list is reached.

Runtime - time the algorithm takes to execute

An algorithm typically uses a number of steps proportional to the size of the input.

## Binary Search

Binary search first checks the middle element of a list, and continues until the element is found

Binary Search is defined as a searching algorithm used in a **sorted array** by repeatedly dividing the search interval in half. The idea of a binary search is to use the information that the array is sorted and reduce the time complexity to O(log N).

![gif of a binary search](https://d18l82el6cdm1i.cloudfront.net/uploads/bePceUMnSG-binary_search_gif.gif)

## O notation

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

## Algorithm Analysis

Worst Case Runtime - Runtime complexity for an input that results in the logest execution.

Exact-time operations are not crucial. A constant number of O(1) operations is considered a single operation. 

## Soring: Introduction

Sorting - Process of converting a list of elements in ascending or descending order.

Challenge arises because the program cant "see" the whole list.

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