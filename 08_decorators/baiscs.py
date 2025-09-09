# -------------------------------------
# Python Decorators Explained
# -------------------------------------
# A decorator is a function that **takes another function as input**
# and **returns a new function**, adding some extra behavior.
# Decorators are often used for logging, timing, access control, etc.

import time

# -------------------------------
# 1. Basic Decorator
# -------------------------------
def simple_decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")
    return wrapper

# Function to decorate
def greet():
    print("Hello!")

# Decorating manually
greet = simple_decorator(greet)
greet()
# Output:
# Before calling the function
# Hello!
# After calling the function

# -------------------------------
# 2. Using the @ syntax
# -------------------------------
@simple_decorator  # Equivalent to greet = simple_decorator(greet)
def greet2():
    print("Hi there!")

greet2()

# -------------------------------
# 3. Decorator with arguments (*args, **kwargs)
# -------------------------------
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def example_function(seconds):
    """Function that sleeps for 'seconds' seconds"""
    time.sleep(seconds)
    print(f"Slept for {seconds} seconds")

example_function(2)

# -------------------------------
# 4. Decorator returning a value
# -------------------------------
def double_result(func):
    """Decorator that doubles the returned value"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper

@double_result
def add(a, b):
    return a + b

print(add(5, 3))  # 16 because (5+3)*2

# -------------------------------
# 5. Decorators with parameters (decorator factory)
# -------------------------------
def repeat(n_times):
    """Decorator factory: repeats the function n_times"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n_times):
                print(f"Run {i+1}:")
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello(name):
    print(f"Hello {name}!")

say_hello("Alice")

# -------------------------------
# 6. Key Takeaways
# -------------------------------
# 1. Decorators are just functions that take functions as arguments.
# 2. Use *args and **kwargs to handle any number of parameters.
# 3. @decorator syntax is shorthand for manually decorating a function.
# 4. Decorators can modify behavior, log info, measure performance, repeat execution, etc.
