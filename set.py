# Creating a set
my_set = {1, 2, 3, 4}
print(f"my_set {my_set}")  # Output: {1, 2, 3, 4}

# Creating set from a list
numbers = [1, 2, 2, 3, 3, 4]
unique_numbers = set(numbers)
print(f"Convert list into set and print unique_numbers :{unique_numbers}")  # Output: {1, 2, 3, 4}



# demonstrating uniqueness
duplicate_set = {1, 1, 2, 2, 3}
print(f"unique_numbers :{duplicate_set}")  # Output: {1, 2, 3}



# adding and removing elements
my_set = {10, 20, 30}

my_set.add(40)
my_set.add(1)
print(f"Test  added element :{my_set}")  # {10, 20, 30, 40}

my_set.remove(20)
print(my_set)  # {10, 30, 40}

# Use discard() to avoid error if item doesn't exist
my_set.discard(100)  # No error


# Common set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union (all unique items)
print(a | b)  # {1, 2, 3, 4, 5, 6}

# Intersection (common items)
print(a & b)  # {3, 4}

# Difference (items in a not in b)
print(a - b)  # {1, 2}

# Symmetric Difference (in a or b, not both)
print(a ^ b)  # {1, 2, 5, 6}

