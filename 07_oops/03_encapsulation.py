# -------------------------------------
# Encapsulation in Python
# -------------------------------------
# Encapsulation = Hiding internal details of an object
# - In Python, we use "private" attributes (by convention with __) 
#   to prevent direct access from outside the class.
# - Instead, we provide controlled access via methods (getters/setters).

class Car:
    def __init__(self, brand, model):
        # Private attributes (using double underscore __)
        # These cannot be accessed directly from outside the class
        self.__brand = brand
        self.__model = model
        
    # Public method → provides controlled access to private attributes
    def full_name(self):
        return f"{self.__brand} {self.__model}"    
    
    # Getter methods → return private values safely
    def get_brand(self):
        return self.__brand
    
    def get_model(self):
        return self.__model


# -------------------------------------
# Using the Encapsulated Class
# -------------------------------------

my_car = Car("Toyota", "Corolla")

# We interact with the object using methods, not by directly accessing attributes
print(my_car.full_name())   # ✅ "Toyota Corolla"

# Getters provide safe access
print("Brand:", my_car.get_brand())   # Toyota
print("Model:", my_car.get_model())   # Corolla

# Trying to directly access private attributes will fail:
# print(my_car.__brand)   # ❌ AttributeError: 'Car' object has no attribute '__brand'

# Python actually does "name mangling" for private attributes:
# Internally, __brand becomes _Car__brand
print("Access via name mangling (not recommended):", my_car._Car__brand)
