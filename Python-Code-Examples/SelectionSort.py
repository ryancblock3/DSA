def selection_sort(my_list):
    # Iterate through the list to find the minimum element and move it to the correct position
    for i in range(len(my_list) - 1):
        min_index = i
        
        # Iterate through the unsorted part of the list to find the minimum element
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element of the unsorted part
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    
    # Return the sorted list
    return my_list

# Example usage
print(selection_sort([4, 2, 6, 5, 1, 3]))
