# -------------------------------
# Behind the Scenes of Iteration
# -------------------------------

# 1. An iterable object (list)
fruits = ["apple", "banana", "cherry"]

# Normally we just do:
for fruit in fruits:
    print(fruit)

# But behind the scenes:
# Step A: Get an iterator from the iterable using iter()
fruit_iterator = iter(fruits)

# Step B: Use next() repeatedly to get values
print(next(fruit_iterator))  # apple
print(next(fruit_iterator))  # banana
print(next(fruit_iterator))  # cherry

# Step C: Once items are over, StopIteration is raised
# print(next(fruit_iterator))  # Uncomment -> StopIteration error


# 2. Strings are also iterables
word = "chai"
it = iter(word)
print(next(it))  # c
print(next(it))  # h
print(next(it))  # a
print(next(it))  # i


# 3. Files are "self-iterators"
# They already have __iter__ and __next__ built in
import os

# Get the directory where this script is located
base_dir = os.path.dirname(os.path.abspath(__file__))

# Build the path for sample.txt in the same folder
file_path = os.path.join(base_dir, "sample.txt")

# Now write to that file
with open(file_path, "w") as f:
    f.write("line1\nline2\nline3\n")

# And read from it
with open(file_path, "r") as f:
    for line in f:
        print("File line:", line.strip())



# 4. Dictionary iteration
coffee = {"masala": "spicy", "ginger": "zesty"}
for key in coffee:  # defaults to keys
    print("Key:", key)

# Explicitly using iter() and next()
dict_iter = iter(coffee)
print(next(dict_iter))  # masala
print(next(dict_iter))  # ginger


# 5. Range objects
nums = range(3)  # 0, 1, 2
nums_iter = iter(nums)
print(next(nums_iter))  # 0
print(next(nums_iter))  # 1
print(next(nums_iter))  # 2
# next(nums_iter) -> StopIteration
