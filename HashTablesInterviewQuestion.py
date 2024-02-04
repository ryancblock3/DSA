def item_in_common(list1, list2):
    # Create an empty dictionary to store elements from list1
    my_dict = {}

    # Iterate through elements in list1 and mark them as True in the dictionary
    for i in list1:
        my_dict[i] = True

    # Iterate through elements in list2
    for j in list2:
        # Check if the element is present in the dictionary (common element)
        if j in my_dict:
            return True  # Return True if a common element is found

    # No common element found between the two lists
    return False

# Example lists
list1 = [1, 3, 5]
list2 = [2, 4, 6]

# Call the function and print the result
print(item_in_common(list1, list2))
