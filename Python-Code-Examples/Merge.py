def merge(list1, list2):
    # Combine two sorted lists into a single sorted list
    combined = []
    i = 0
    j = 0

    # Compare elements from both lists and append the smaller one to the combined list
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    
    # Append remaining elements from list1 (if any)
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    
    # Append remaining elements from list2 (if any)
    while j < len(list2):
        combined.append(list2[j])
        j += 1

    # Return the combined sorted list
    return combined

def merge_sort(my_list):
    # Recursively divide the list into halves until it reaches single-element lists
    if len(my_list) == 1:
        return my_list
    
    mid_index = int(len(my_list) / 2)

    # Recursively apply merge_sort to the left and right halves
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])

    # Combine the sorted left and right halves using the merge function
    return merge(left, right)

# Example usage
original_list = [3, 1, 4, 2]
sorted_list = merge_sort(original_list)

# Print the original and sorted lists
print('Original List:', original_list)
print('\nSorted List:', sorted_list)
