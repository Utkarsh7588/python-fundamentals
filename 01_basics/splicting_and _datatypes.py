# ---------------------------
# LIST (Mutable)
# ---------------------------
# Lists can be changed (append, remove, modify elements)
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")        # adds new element
fruits[1] = "blueberry"        # modifies element
print("List:", fruits)         # ['apple', 'blueberry', 'cherry', 'orange']


# ---------------------------
# TUPLE (Immutable)
# ---------------------------
# Tuples cannot be changed after creation
coordinates = (10, 20, 30)
print("Tuple:", coordinates)   # (10, 20, 30)

# coordinates[0] = 50  # ❌ This will give TypeError (immutable)


# ---------------------------
# DICTIONARY (Mutable)
# ---------------------------
# Key-value pairs, can add, update, delete
person = {"name": "Alice", "age": 25}
person["city"] = "Pune"        # add new key-value
person["age"] = 26             # update existing value
print("Dictionary:", person)   # {'name': 'Alice', 'age': 26, 'city': 'Pune'}


# ---------------------------
# SET (Mutable, unique elements, no order)
# ---------------------------
# No duplicates, useful for membership testing
numbers = {1, 2, 3, 3, 2, 1}   # duplicates removed automatically
numbers.add(4)                 # add element
print("Set:", numbers)         # {1, 2, 3, 4}


# ---------------------------
# STRING SLICING
# ---------------------------
text = "Python"

# [start:end] -> gets characters from start index up to end-1
print(text[0:4])   # 'Pyth'

# Omitting start -> begins at 0
print(text[:2])    # 'Py'

# Omitting end -> goes till last
print(text[2:])    # 'thon'

# Negative indexes -> count from end
print(text[-1])    # 'n' (last char)
print(text[-3:])   # 'hon' (last 3 chars)

# Step value: [start:end:step]
print(text[::2])   # 'Pto' (every 2nd char)
print(text[::-1])  # 'nohtyP' (reverses string)

# Trick: negative step means direction is reversed
print(text[5:2:-1])  # 'noh' (from index 5 down to 3)
