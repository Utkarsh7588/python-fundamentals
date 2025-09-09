# -------------------------------
# Python Functions Explained
# -------------------------------

# 1. Basic function
def greet():
    """This is a docstring (function documentation).
    It explains what the function does."""
    print("Hello from the greet() function!")

greet()  # Calling the function


# 2. Function with parameters
def greet_person(name):
    """Functions can take parameters (inputs)."""
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")


# 3. Function with return value
def add(a, b):
    """Functions can return values using 'return'."""
    return a + b

result = add(5, 3)
print("Sum is:", result)


# 4. Default parameter values
def power(base, exp=2):
    """If 'exp' is not provided, default = 2 (square)."""
    return base ** exp

print("Square of 4:", power(4))
print("Cube of 4:", power(4, 3))


# 5. Keyword arguments
def introduce(name, age):
    """We can use keyword arguments when calling a function."""
    print(f"My name is {name} and I am {age} years old.")

introduce(age=25, name="John")


# 6. Arbitrary arguments (*args)
def print_numbers(*args):
    """*args lets you pass any number of arguments (tuple)."""
    for num in args:
        print("Number:", num)

print_numbers(1, 2, 3, 4, 5)


# 7. Arbitrary keyword arguments (**kwargs)
def print_profile(**kwargs):
    """**kwargs lets you pass key=value pairs (dictionary)."""
    for key, value in kwargs.items():
        print(key, ":", value)

print_profile(name="Alice", age=30, city="Delhi")


# 8. Nested functions
def outer():
    print("This is outer function.")

    def inner():
        print("This is inner function.")

    inner()  # Call inner function inside outer

outer()


# 9. Functions as first-class citizens (can be passed around)
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def speak(func, message):
    """Functions can be passed as arguments to other functions."""
    print(func(message))

speak(shout, "hello world")
speak(whisper, "HELLO WORLD")


# 10. Lambda (anonymous) functions
square = lambda x: x * x
print("Square using lambda:", square(6))

# Example with 'map' and lambda
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x * x, nums))
print("Squared list:", squared)


# 11. Scope of variables
x = 10  # Global variable

def test_scope():
    x = 5  # Local variable
    print("Inside function, x =", x)

test_scope()
print("Outside function, x =", x)


# 12. Recursion (function calling itself)
def factorial(n):
    """Recursion example: factorial of n."""
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))


# 13. Function with type hints (not mandatory, just for clarity)
def multiply(a: int, b: int) -> int:
    """Type hints: suggest that inputs/outputs are integers."""
    return a * b

print("Multiply 3 * 4 =", multiply(3, 4))


# 14. Generators and 'yield'
def generate_numbers(limit):
    """
    'yield' turns a function into a GENERATOR.
    Instead of returning all results at once,
    it produces values one by one when requested.
    Saves memory for large sequences.
    """
    num = 1
    while num <= limit:
        yield num  # returns a value but pauses function state
        num += 1

# Using the generator
print("Generator output (numbers up to 5):")
for value in generate_numbers(5):
    print(value)

# You can also manually call next() on a generator
gen = generate_numbers(3)
print("Using next():")
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
# next(gen)  # would raise StopIteration (no more values)


# 15. Main guard (good practice in larger programs)
# This ensures code runs only when file is executed directly,
# not when imported as a module in another file.
if __name__ == "__main__":
    print("This code runs only when file is executed directly.")
