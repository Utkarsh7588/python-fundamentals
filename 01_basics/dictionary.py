# -------------------------------
# Dictionary Examples Demonstration
# -------------------------------

# 1. Dictionary Creation
coffee_types = {
    "masala": "spicy",
    "ginger": "zesty",
    "green": "mild"
}
print("Initial dictionary:", coffee_types)

# 2. Accessing Dictionary Items
print("coffee_types['masala']:", coffee_types["masala"])  # spicy
print("coffee_types.get('ginger'):", coffee_types.get("ginger"))  # zesty
print("coffee_types.get('gingery'):", coffee_types.get("gingery"))  # None
# print(coffee_types["masalaa"])  # ❌ KeyError

# 3. Modifying Dictionary Items
coffee_types["green"] = "fresh"
print("After modifying 'green':", coffee_types)

# 4. Iterating Through Dictionaries
print("Looping through keys:")
for coffee in coffee_types:
    print("-", coffee)

print("Looping through keys and values:")
for coffee in coffee_types:
    print(coffee, ":", coffee_types[coffee])

print("Looping through items:")
for key, value in coffee_types.items():
    print(key, "->", value)

# 5. Conditional Checks
if "masala" in coffee_types:
    print("I have masala coffee")

# 6. Dictionary Length
print("Length of dictionary:", len(coffee_types))

# 7. Adding New Items
coffee_types["earl grey"] = "citrus"
print("After adding earl grey:", coffee_types)

# 8. Removing Items
removed = coffee_types.pop("ginger")
print("Removed ginger:", removed)
last_removed = coffee_types.popitem()
print("Last removed (popitem):", last_removed)
del coffee_types["green"]
print("After deleting 'green':", coffee_types)

# 9. Copying Dictionaries
copy_dict = coffee_types.copy()
print("Copy of dictionary:", copy_dict)

# 10. Nested Dictionaries
tea_shop = {
    "coffee": {
        "masala": "spicy",
        "ginger": "zesty"
    },
    "tea": {
        "green": "mild",
        "black": "strong"
    }
}
print("Nested tea_shop dictionary:", tea_shop)
print("tea_shop['coffee']:", tea_shop["coffee"])
print("tea_shop['coffee']['ginger']:", tea_shop["coffee"]["ginger"])

# 11. Dictionary Comprehension
squared_nums = {x: x**2 for x in range(6)}
print("Squared numbers:", squared_nums)

# 12. Clearing a Dictionary
squared_nums.clear()
print("After clearing:", squared_nums)

# 13. Creating Dictionaries from Keys
keys = ["masala", "ginger", "lemon"]
default_value = "delicious"
new_dict = dict.fromkeys(keys, default_value)
print("Fromkeys with default value:", new_dict)

problematic_dict = dict.fromkeys(keys, keys)
print("Fromkeys with keys as value:", problematic_dict)
