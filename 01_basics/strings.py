# -------------------------------
# String Examples Demonstration
# -------------------------------

# Simple strings
drink = "coffee"
print(drink)  # coffee

# Longer strings
lemon_drink = "lemon coffee"
masala_drink = "masala coffee"
ginger_drink = "ginger tea"  # alternative
print(lemon_drink, masala_drink, ginger_drink)

# Slice example
print(masala_drink[0:6])  # masala

# Using 'in' operator
print("masala" in masala_drink)  # True
print("masalaa" in masala_drink)  # False

# strip() example with leading/trailing spaces
spaced = " masala coffee "
print(spaced.strip())  # masala coffee

# replace() method
print(lemon_drink.replace("lemon", "ginger"))  # ginger coffee

# split() example
flavors = "lemon, ginger coffee, masala, mint"
print(flavors.split(","))  
# ['lemon', ' ginger coffee', ' masala', ' mint']

# count() method
repeat_str = "masala coffee coffee coffee"
print(repeat_str.count("coffee"))  # 3

# format() method
order = "I order {} cups of {} coffee"
print(order.format(2, "ginger"))  
# I order 2 cups of ginger coffee

# join() method
coffee_list = ["lemon coffee", "masala coffee", "ginger"]
print(" | ".join(coffee_list))  
# lemon coffee | masala coffee | ginger

# Escape characters (quotes)
quote_str = "He said \"masala coffee is awesome\""
print(quote_str)

# Escape characters (newline)
newline_str = "masala\ncoffee"
print(newline_str)
# masala
# coffee

# Raw string for Windows path
path = r"C:\user\pwd"
print(path)  # C:\user\pwd

# File name example
filename = "windows.txt"
print(filename)
