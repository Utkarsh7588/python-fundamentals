# -------------------------------
# List Examples Demonstration
# -------------------------------

# Initial Tea Varieties
T_varieties = ["Black Tea", "Green Tea", "Oolong Tea", "White Tea"]
print("Initial:", T_varieties)

# Replace "White Tea" with "Herbal"
T_varieties[3] = "Herbal"
print("After replacing White Tea with Herbal:", T_varieties)

# Replace "Green Tea" with "Lemon Tea"
T_varieties[1] = "Lemon Tea"
print("After replacing Green Tea with Lemon Tea:", T_varieties)

# Replace "Oolong Tea" with "Masala"
T_varieties[2] = "Masala"
print("After replacing Oolong Tea with Masala:", T_varieties)

# Insert "Test" at index 1 (via slicing)
T_varieties[1:1] = ["Test"]
print("After inserting Test at index 1:", T_varieties)
# if you dont add it as list then every letter will be added as seperate element in list example below

T_varieties[1:1] = "Test" # ["Black Tea","T", "e", "s", "t", "Green Tea", "Oolong Tea", "White Tea"]

# Append "Lemon" to the list
T_varieties.append("Lemon")
print("After appending Lemon:", T_varieties)

# Delete a slice (remove index 2 and 3 for example)
T_varieties[2:4] = []
print("After deleting slice [2:4]:", T_varieties)

# Loop through the list
print("Looping through list:")
for T in T_varieties:
    print("-", T)

# Copying the list
T_variety_copy = T_varieties.copy()
print("Copied list:", T_variety_copy)

# -------------------------------
# List Comprehension and Range
# -------------------------------

# List comprehension: squares of numbers 0–9
squared_nums = [x * x for x in range(10)]
print("Squares (0–9):", squared_nums)

# List comprehension: cubes of numbers 0–4
cube_numbers = [y * y * y for y in range(5)]
print("Cubes (0–4):", cube_numbers)

# Showing range directly
print("Range(10) as list:", list(range(10)))
print("Range(5) as list:", list(range(5)))
