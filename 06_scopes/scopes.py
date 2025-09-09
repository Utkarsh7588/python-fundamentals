# -------------------------------
# Python Variable Scope Explained
# -------------------------------

# 1. Local Scope
def local_scope_example():
    x = 10  # Local variable (exists only inside this function)
    print("Inside function, x =", x)

local_scope_example()
# print(x)  # ❌ Error: x is not defined (because it's local to the function)


# 2. Global Scope
y = 20  # Global variable

def global_scope_example():
    print("Inside function, y =", y)  # Can access global variable

global_scope_example()
print("Outside function, y =", y)  # Still accessible globally


# 3. Modifying Global Variables (using 'global')
z = 30

def modify_global():
    global z  # Tell Python we want to use global z
    z = 40    # This changes the global variable
    print("Inside function, z =", z)

modify_global()
print("Outside function, z =", z)  # Value updated globally


# 4. Enclosing Scope (Nested Functions + 'nonlocal')
def outer_function():
    a = 50  # Enclosing variable (in outer function)

    def inner_function():
        nonlocal a  # Allows modifying 'a' from enclosing scope
        a = 60
        print("Inside inner_function, a =", a)

    inner_function()
    print("Inside outer_function, after inner_function, a =", a)

outer_function()


# 5. Built-in Scope
# Python has built-in functions available everywhere
print("Example of built-in function:", len([1, 2, 3]))


# 6. Scope Resolution Order (LEGB Rule)
# Python looks for variables in this order:
# Local → Enclosing → Global → Built-in

x = "global x"

def enclosing():
    x = "enclosing x"

    def local():
        x = "local x"
        print("Inside local(), x =", x)  # Local wins

    local()
    print("Inside enclosing(), x =", x)  # Enclosing wins

enclosing()
print("Outside functions, x =", x)  # Global wins


# 7. Shadowing Example
len = 100  # ⚠️ Bad practice: shadowing built-in 'len'

print("len variable =", len)
# print(len([1,2,3]))  # ❌ Error, because 'len' is now an integer, not a function

# Best practice: avoid using names like 'len', 'list', 'dict', 'str' for variables


# -------------------------------
# EXTRA PYTHON-SPECIFIC SCOPING QUIRKS
# -------------------------------

# 8. No Block Scope
if True:
    block_var = "I leak out!"
print("Block scope test:", block_var)  # ✅ Still accessible (no block scope)


# 9. Mutable Default Argument Trap
def append_item(item, lst=[]):  # Default is reused across calls
    lst.append(item)
    return lst

print("Mutable default 1:", append_item(1))  # [1]
print("Mutable default 2:", append_item(2))  # [1, 2] 😱 Unexpected!

# Correct way
def append_item_fixed(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print("Fixed default 1:", append_item_fixed(1))  # [1]
print("Fixed default 2:", append_item_fixed(2))  # [2]


# 10. Class Scope Oddity
x = 100
class Test:
    x = 200
    print("Inside class body, x =", x)  # 200 (class scope)
    def show(self):
        print("Inside method, x =", x)  # 100 (global scope, not class var!)
        print("Access class var via self.x =", self.x)

obj = Test()
obj.show()


# 11. Late Binding in Closures
funcs = [lambda: i for i in range(3)]
print("Late binding issue:", [f() for f in funcs])  # [2, 2, 2]

# Fixed with default argument trick
funcs_fixed = [lambda i=i: i for i in range(3)]
print("Late binding fixed:", [f() for f in funcs_fixed])  # [0, 1, 2]


# 12. Comprehension Scope (Python 3+)
nums = [1, 2, 3]
squares = [x*x for x in nums]
try:
    print(x)  # ❌ NameError in Python 3
except NameError as e:
    print("Comprehension scope:", e)

