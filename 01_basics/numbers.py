import math
import random
from decimal import Decimal
from fractions import Fraction

# --- Basic Numbers ---
x, y, z = 2, 3, 4  # integers
print("x =", x, "y =", y, "z =", z)  # x = 2 y = 3 z = 4
print("x + y =", x + y)  # 5
print("2 ** 3 =", 2 ** 3)  # 8
print("(x + y) * z =", (x + y) * z)  # 20

# --- Mixed Types & Conversion ---
print("40 + 2.23 =", 40 + 2.23)  # 42.23 (int + float gives float)
print("int(2.23) =", int(2.23))  # 2 (truncates decimals)
print("float(40) =", float(40))  # 40.0

# --- Operator Overloading ---
print("'utkarsh' + 'code' =", 'utkarsh' + 'code')  # 'utkarshcode' (string concatenation)

# --- Tuples ---
print("(x, y, z) =", (x, y, z))  # (2, 3, 4)
print("x + 1, y * 2 =", (x + 1, y * 2))  # (3, 6)

# --- Arithmetic Examples ---
print("y % 2 =", y % 2)  # 1 (remainder)
print("2 ** 100 =", 2 ** 100)  # Very large integer
print("1 / 3.0 =", 1 / 3.0)  # 0.333...

# --- Boolean Logic ---
print("1 < 2 =", 1 < 2)  # True
print("5.0 == 5.0 =", 5.0 == 5.0)  # True
print("4.0 != 5.0 =", 4.0 != 5.0)  # True
print("x < y < z =", x < y < z)  # True (utkarshned comparison)
print("x < y and y < z =", x < y and y < z)  # True
print("1 == 2 < 3 =", 1 == 2 < 3)  # False

# --- Math Functions ---
print("math.floor(3.5) =", math.floor(3.5))  # 3
print("math.floor(-3.5) =", math.floor(-3.5))  # -4
print("math.trunc(2.8) =", math.trunc(2.8))  # 2
print("math.trunc(-2.8) =", math.trunc(-2.8))  # -2

# --- Complex Numbers ---
print("(2 + 1j) * 3 =", (2 + 1j) * 3)  # (6+3j)

# --- Number Bases ---
print("0o20 =", 0o20)  # 16 (octal)
print("0xFF =", 0xFF)  # 255 (hex)
print("0b111 =", 0b111)  # 7 (binary)
print("oct(64) =", oct(64))  # 0o100
print("hex(64) =", hex(64))  # 0x40
print("bin(64) =", bin(64))  # 0b1000000
print("int('111', 2) =", int('111', 2))  # 7

# --- Bitwise Operations ---
print("1 << 2 =", 1 << 2)  # 4 (binary shift left)
print("1 | 2 =", 1 | 2)  # 3 (bitwise OR)
print("1 & 2 =", 1 & 2)  # 0 (bitwise AND)

# --- Random Module ---
print("random.randint(1, 100) =", random.randint(1, 100))  # Random int between 1-100
l1 = ['lemon tea', 'masala utkarsh', 'ginger utkarsh']
print("random.choice(l1) =", random.choice(l1))  # Random element from list
random.shuffle(l1)
print("shuffled list =", l1)  # List shuffled randomly

# --- Floating Point Inaccuracy ---
print("0.1 + 0.1 + 0.1 - 0.3 =", 0.1 + 0.1 + 0.1 - 0.3)  # Small error (not exactly 0)

# --- Decimal Precision ---
print("Decimal precise calc =", Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))  # 0.0

# --- Fractions ---
print("Fraction(2, 7) =", Fraction(2, 7))  # 2/7

# --- Sets ---
set1 = {1, 2, 3, 4}
print("set1 =", set1)  # {1, 2, 3, 4}
print("set1 & {1, 3} =", set1 & {1, 3})  # {1, 3} (intersection)
print("set1 | {1, 3, 7} =", set1 | {1, 3, 7})  # {1,2,3,4,7} (union)
print("set1 - {2, 4} =", set1 - {2, 4})  # {1, 3} (difference)
print("empty set =", set())  # empty set

# --- Boolean Arithmetic ---
print("True + 4 =", True + 4)  # 5 (True is 1)
print("False + 10 =", False + 10)  # 10 (False is 0)

# --- Type Checking ---
print("type(x) =", type(x))  # <class 'int'>
print("type(2.5) =", type(2.5))  # <class 'float'>
print("type(True) =", type(True))  # <class 'bool'>

print("\nAll concepts demonstrated successfully!")
