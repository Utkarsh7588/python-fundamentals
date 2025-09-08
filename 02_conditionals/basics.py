# -------------------------------
# Python Conditionals Explained
# -------------------------------

# Basic if statement
x = 10
if x > 5:  # condition must evaluate to True or False
    print("x is greater than 5")

# if-else statement
if x < 5:
    print("x is less than 5")
else:
    print("x is NOT less than 5")

# if-elif-else chain
y = 0
if y > 0:
    print("y is positive")
elif y == 0:
    print("y is zero")
else:
    print("y is negative")

# Indentation matters in Python (4 spaces is the convention)
z = 7
if z % 2 == 0:
    print("z is even")
    print("Still inside the if block")
else:
    print("z is odd")
print("This line is outside of if/else")

# Comparison operators:
# == (equal), != (not equal), <, <=, >, >=
a, b = 5, 8
if a != b:
    print("a and b are not equal")

# Logical operators: and, or, not
age = 20
has_id = True
if age >= 18 and has_id:
    print("Allowed entry")
if age < 18 or not has_id:
    print("Not allowed entry")

# Nested conditionals
num = 12
if num > 0:
    if num % 2 == 0:
        print("num is positive and even")
    else:
        print("num is positive but odd")

# Shorthand (ternary) conditional expression
n = 3
result = "Even" if n % 2 == 0 else "Odd"
print("Shorthand result:", result)

# Membership tests with "in" and "not in"
fruits = ["apple", "banana", "mango"]
if "apple" in fruits:
    print("Apple is in the list")
if "grape" not in fruits:
    print("Grape is not in the list")

# Identity tests with "is" and "is not"
a_list = []
b_list = []
if a_list is b_list:
    print("They are the same object in memory")
else:
    print("They are different objects in memory")
if a_list == b_list:
    print("But their contents are equal")

# Truthy and Falsy values in conditionals
# Falsy values in Python: 0, 0.0, "", [], {}, set(), None, False
if "":  # empty string is falsy
    print("This won't run")
else:
    print("Empty string is falsy")

if [1, 2, 3]:  # non-empty list is truthy
    print("Non-empty list is truthy")

if None:
    print("None is truthy")
else:
    print("None is falsy")

# Using pass when you need a placeholder in if block
if x > 0:
    pass  # placeholder, does nothing
