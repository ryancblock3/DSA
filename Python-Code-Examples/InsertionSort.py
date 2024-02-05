def insertion_sort(my_list):
    # Iterate through the list starting from the second element (index 1)
    for i in range(1, len(my_list)):
        # Store the current element to be compared and inserted
        temp = my_list[i]

        # Start comparing and shifting elements to the right
        j = i - 1
        while temp < my_list[j] and j > -1:
            # Shift elements to the right to make space for the current element
            my_list[j + 1] = my_list[j]
            my_list[j] = temp
            j -= 1

    # Return the sorted list
    return my_list

# Test the insertion_sort function with an example list
print(insertion_sort([4, 2, 6, 5, 1, 3]))
