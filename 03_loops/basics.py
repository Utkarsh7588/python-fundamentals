# -------------------------------
# Python For Loops Explained
# -------------------------------

# 1. Basic for loop with a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

# 2. Looping through a string (strings are iterable)
for char in "coffee":
    print("Character:", char)

# 3. Using range() with for loop
# range(start, stop, step)
for i in range(5):  # 0,1,2,3,4
    print("i:", i)

for i in range(2, 10, 2):  # start=2, stop=10, step=2
    print("Even number:", i)

# 4. Looping through a dictionary
coffee_types = {"masala": "spicy", "ginger": "zesty", "green": "fresh"}
# Looping through keys
for key in coffee_types:
    print("Key:", key)
# Looping through values
for value in coffee_types.values():
    print("Value:", value)
# Looping through key-value pairs
for key, value in coffee_types.items():
    print(f"{key} -> {value}")

# 5. Nested for loops
colors = ["red", "green"]
sizes = ["S", "M"]
for color in colors:
    for size in sizes:
        print(color, size)

# 6. break, continue, pass
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    if n == 3:
        print("Breaking at", n)
        break  # stops the loop entirely
    print("Number:", n)

for n in numbers:
    if n == 3:
        print("Skipping", n)
        continue  # skips this iteration, moves to next
    print("Number:", n)

for n in numbers:
    if n == 3:
        pass  # does nothing, just a placeholder
    print("Number (with pass allowed):", n)

# 7. for-else construct
# else block executes ONLY if loop completes without break
for n in numbers:
    if n == 10:
        break
else:
    print("Loop finished without finding 10")

# 8. List comprehension (shorthand for loop inside [])
squares = [x * x for x in range(6)]
print("Squares:", squares)

evens = [x for x in range(10) if x % 2 == 0]
print("Even numbers:", evens)
