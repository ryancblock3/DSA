class HashTable:
    def __init__(self, size=7):
        # Initialize the hash table with a specified size (default is 7)
        self.data_map = [None] * size

    def __hash(self, key):
        # Private method to calculate the hash value for a given key
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        # Print the current state of the hash table (index and value at each position)
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        # Add an item (key, value pair) to the hash table
        index = self.__hash(key)
        # Check for collisions, create a new list if the index is empty, and append the item
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        # Retrieve the value associated with a given key
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                # Check if the key exists in the list at the calculated index
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        # Return a list of all keys in the hash table
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
    
# Testing Constructor
            
# my_hash_table = HashTable()
# my_hash_table.print_table()
        
# Testing Set Item
        
# my_hash_table = HashTable()
# my_hash_table.set_item('bolts', 1400)
# my_hash_table.set_item('washers', 50)
# my_hash_table.set_item('lumber', 70)
# my_hash_table.print_table()
    
# Testing Get Item
    
# my_hash_table = HashTable()
# my_hash_table.set_item('bolts', 1400)
# my_hash_table.set_item('washers', 50)
# print(my_hash_table.get_item('bolts'))
# print(my_hash_table.get_item('washers'))
# print(my_hash_table.get_item('lumber'))
    
# Testing Keys

# my_hash_table = HashTable()
# my_hash_table.set_item('bolts', 1400)
# my_hash_table.set_item('washers', 50)
# my_hash_table.set_item('lumber', 70)
# print(my_hash_table.keys())
