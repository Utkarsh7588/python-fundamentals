# In Python, variables are names (labels) that point to objects in memory.
# Objects themselves have types (int, str, list, etc.) that decide if they are mutable or immutable.

a = 10      # 'a' is a name pointing to an integer object 10 in memory.
b = a       # 'b' now points to the SAME object (10). No new object is created.

print(a)    # prints 10 (since 'a' points to 10)
print(b)    # prints 10 (since 'b' also points to 10)

a = 20      # Here, a NEW integer object (20) is created.
            # 'a' is reassigned to point to 20.
            # 'b' still points to the old object (10).

print(a)    # prints 20 (a → 20 now)
print(b)    # prints 10 (b → 10 still)

# ⚡ Key Concept:
# Integers (int), strings (str), and tuples are IMMUTABLE.
# This means their values cannot be changed in place. 
# Instead, reassigning creates a new object, and the variable name points to it.

# Example with mutable type:
lst1 = [1, 2, 3]   # 'lst1' points to a list object in memory.
lst2 = lst1        # 'lst2' points to the same list object (not a copy).

lst1.append(4)     # The list object is MUTATED in place (changed internally).
print(lst1)        # [1, 2, 3, 4]
print(lst2)        # [1, 2, 3, 4] -> both names see the same updated object.

# ⚡ Mutable vs Immutable:
# - Immutable: int, float, str, tuple → reassigning creates NEW objects.
# - Mutable: list, dict, set → can be modified in place, and all references see changes.
