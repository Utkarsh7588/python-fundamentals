# -------------------------------
# Taking Inputs in Python
# -------------------------------

# 1. Basic input (always returns string)
name = input("Enter your name: ")
print("Hello,", name)

# 2. Converting input to integer
age = int(input("Enter your age: "))  # convert str -> int
print("You will be", age + 1, "next year")

# 3. Converting input to float
price = float(input("Enter the price: "))
print("Price with 10% tax:", price * 1.1)

# 4. Taking multiple values in one line (space-separated)
a, b = input("Enter two numbers separated by space: ").split()
print("a:", a, "b:", b)  # both are still strings

# Convert them to integers
a, b = map(int, input("Enter two numbers (int) separated by space: ").split())
print("Sum:", a + b)

# 5. Taking a list of integers
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Numbers list:", numbers)

# 6. Taking multiple lines of input using a loop
n = int(input("How many items do you want to enter? "))
items = []
for i in range(n):
    item = input(f"Enter item {i+1}: ")
    items.append(item)
print("Items entered:", items)

# 7. Taking inputs into a dictionary
person = {}
person["name"] = input("Enter your name: ")
person["age"] = int(input("Enter your age: "))
person["city"] = input("Enter your city: ")
print("Dictionary input:", person)

# 8. Using list comprehension with input
squared_numbers = [int(x)**2 for x in input("Enter numbers to square (space-separated): ").split()]
print("Squares:", squared_numbers)
