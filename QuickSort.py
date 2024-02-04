def swap(my_list, index1, index2):
    # Swaps elements at two given indices in the list
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

def pivot(my_list, pivot_index, end_index):
    # Partitions the list around a pivot element
    swap_index = pivot_index

    for i in range(pivot_index + 1, end_index + 1):
        # If the current element is less than the pivot, swap it with the element at swap_index
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    
    # Swap the pivot element to its correct position in the sorted order
    swap(my_list, pivot_index, swap_index)
    
    # Return the index where the pivot element is now placed
    return swap_index

def quick_sort_helper(my_list, left, right):
    # Recursively sorts the list using the QuickSort algorithm
    if left < right:
        # Find the pivot index and partition the list
        pivot_index = pivot(my_list, left, right)
        
        # Recursively apply quick_sort_helper to the left and right partitions
        quick_sort_helper(my_list, left, pivot_index - 1)
        quick_sort_helper(my_list, pivot_index + 1, right)
    
    # Return the sorted list
    return my_list

def quick_sort(my_list):
    # Wrapper function for quick_sort_helper
    return quick_sort_helper(my_list, 0, len(my_list) - 1)

# Example usage
print(quick_sort([4, 6, 1, 7, 3, 2, 5]))
