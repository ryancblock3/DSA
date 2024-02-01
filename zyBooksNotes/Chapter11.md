# Searching and Algorithm Analysis

## Python: Linear and Binary Search

Linear Search - Comparing each item in a given list, one at a time, to a key.

linear_search()

Binary Search - Performed on a sorted list, compares the middle element to the key. If middle element = key then it returns the index, if the middle element is greater than the key the loop proceeds by searching the first half, adverse if the middle element is smaller than they key.

mid = (high + low) // 2

## Constant Time Operations

Constant Time Operation - an operation that for a given processor always operates in the same amount of time, regardless of input values.

## Growth of Functions and Complexity

T(N) Runtime complexity

Lower Bound - A function f(N) that is less than or equal to the best case T(N), for all values of N >= 1

Upper Bound - A function f(N) that is >= the worst case T(N), for all values of N >= 1

Asymptotic Notation - Only indicated the growth rate of a bounding function.

O notation provides a growth rate for an algorithm's upper bound.

Ω notation provides a growth rate for an algorithm's lower bound.

Θ notation provides a growth rate that is both an upper and lower bound.

## Recursive Definitions

Recursive Algorithm - an algo that breaks the problem into smaller subproblems and applies the algo to itself to solve the smaller problems.

Base Case - A case where a recuursive algo completes without applying itself to a smaller problem.

## Recursive Algorithms

FibonacciNumber(termIndex) {
   if (termIndex == 0)
      return 0
   else if (termIndex == 1)
      return 1
   else
      return FibonacciNumber(termIndex - 1) + FibonacciNumber(termIndex - 2)
}

BinarySearch(numbers, low, high, key) {
   if (low > high)
      return -1

   mid = (low + high) / 2
   if (numbers[mid] < key) {
      return BinarySearch(numbers, mid + 1, high, key)
   }
   else if (numbers[mid] > key) {
      return BinarySearch(numbers, low, mid - 1, key)
   }
   return mid
}

## Analyzing the Time Complexity of Recursive Algorithms


