# Additional Material

## Bubble Sort

Bubble Sort - Soring algo that iterates through a list, comparing and swapping adjacent elements if the second element is less than the first element.

[Bubblesort](../BubbleSort.py)

## Quickselect

Quickselect - Algo that selects the kth smallest element in a list

// Selects kth smallest element, where k is 0-based
Quickselect(numbers, first, last, k) {
   if (first >= last)
      return numbers[first]

   lowLastIndex = Partition(numbers, first, last)

   if (k <= lowLastIndex)
      return Quickselect(numbers, first, lowLastIndex, k)
   return Quickselect(numbers, lowLastIndex + 1, last, k)
}

## Python: Quickselect

def quickselect(numbers, start_index, end_index, k):
    if start_index >= end_index:
        return numbers[start_index]

    low_last_index = partition(numbers, start_index, end_index)
    if k <= low_last_index:
        return quickselect(numbers, start_index, low_last_index, k)
  
    return quickselect(numbers, low_last_index + 1, end_index, k)

## Bucket Sort

Bucket Sort - Numerical sorting algo that distributes numbers into bucks, sorts each bucket with an additional sorting algo, and then concatenates buckets together.

Bucket - Container for numerical values in a specific range

BucketSort(numbers, numbersSize, bucketCount) {
   if (numbersSize < 1)
      return

   buckets = Create list of bucketCount buckets

   // Find the maximum value
   maxValue = numbers[0]
   for (i = 1; i < numbersSize; i++) {
      if (numbers[i] > maxValue)
         maxValue = numbers[i]
   }

   // Put each number in a bucket
   for each (number in numbers) {
      index = floor(number * bucketCount / (maxValue + 1))
      Append number to buckets[index]
   }

   // Sort each bucket
   for each (bucket in buckets)
      Sort(bucket)

   // Combine all buckets back into numbers list
   result = Concatenate all buckets together
   Copy result to numbers
}

## List Data Stucture

List Data Structure - A data structure containing the lists head and tail and may also include additional information such as list size

List Node Data Structure - Maintains the data for each list element, including the elements data and pointers to the other list element

## Curcular Lists

Circular Linked List - Linked list where the tail nodes points to the head of the list instead of null. Used to represent a repeating process
