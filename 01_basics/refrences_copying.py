# ----------------------------------------
# Python References & Copying Explained
# ----------------------------------------

# Example 1: Direct assignment = reference copy
l1 = [1, 2, 3]
l2 = l1   # l2 points to the SAME list object as l1

print("l1:", l1)   # [1, 2, 3]
print("l2:", l2)   # [1, 2, 3]

l1.append(4)       # modify l1
print("\nAfter modifying l1:")
print("l1:", l1)   # [1, 2, 3, 4]
print("l2:", l2)   # [1, 2, 3, 4]  <-- l2 also changes, because both point to same memory location


# Example 2: Slicing creates a shallow copy
l3 = l1[:]   # l3 is a NEW list with the same elements
l1.append(5)

print("\nAfter slicing and modifying l1:")
print("l1:", l1)   # [1, 2, 3, 4, 5]
print("l3:", l3)   # [1, 2, 3, 4] (unchanged, because it's a different object)


# Example 3: Nested lists & shallow copy
l4 = [[1, 2], [3, 4]]
l5 = l4[:]  # shallow copy, outer list is new but inner lists are shared

l4[0].append(99)
print("\nNested list shallow copy:")
print("l4:", l4)   # [[1, 2, 99], [3, 4]]
print("l5:", l5)   # [[1, 2, 99], [3, 4]] <-- inner list reference shared!


# Example 4: Deep copy (requires copy module)
import copy
l6 = copy.deepcopy(l4)   # makes a full independent copy
l4[0].append(1000)

print("\nAfter deep copy and modifying l4:")
print("l4:", l4)   # [[1, 2, 99, 1000], [3, 4]]
print("l6:", l6)   # [[1, 2, 99], [3, 4]] (independent)


# Example 5: Immutable objects (numbers, strings, tuples)
a = 10
b = a   # both point to same integer 10
a = 20  # but reassignment makes 'a' point to NEW object, 'b' is unchanged

print("\nImmutable objects:")
print("a:", a)   # 20
print("b:", b)   # 10


# Example 6: "is" vs "=="
x = [1, 2, 3]
y = [1, 2, 3]

print("\n'is' vs '==':")
print(x == y)   # True (values are equal)
print(x is y)   # False (different memory references)


# ----------------------------------------
# Key Takeaways:
# - Assignment does NOT copy objects, it just copies references.
# - Slicing [:] makes a shallow copy (only top level).
# - copy.deepcopy() makes a full independent copy.
# - Immutable objects (int, str, tuple) behave differently:
#   reassignment creates a new object instead of modifying existing one.
# ----------------------------------------
