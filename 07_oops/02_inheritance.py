# -------------------------------------
# Importing Class from Another File
# -------------------------------------

import importlib

# Normal `import` doesn't work well with files starting with numbers 
# (like `01_class_basics.py`) because:
#   - Python identifiers (module names, class names, variables) 
#     cannot start with a digit by convention.
#
# Instead, we use `importlib.import_module()` which allows importing 
# using the exact file name (without `.py`).
#
# Example:
#   import 01_class_basics   ❌ invalid (syntax error)
#   class_module = importlib.import_module("01_class_basics") ✅ works

class_module = importlib.import_module("01_class_basics")

# Extract the Car class from the module dynamically
Car = getattr(class_module, "Car")


# -------------------------------------
# Inheritance Basics
# -------------------------------------

# Define a new class ElectricCar that inherits from Car
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        # Call parent (Car) constructor using super()
        super().__init__(brand, model)
        self.battery_size = battery_size   # New attribute specific to ElectricCar


# -------------------------------------
# Creating Objects
# -------------------------------------

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

# full_name() is inherited from Car (no need to redefine in ElectricCar)
print(my_tesla.full_name())   # Tesla Model S

# isinstance() checks relationships in inheritance
print(isinstance(my_tesla, Car))         # True → ElectricCar is a Car (child of Car)
print(isinstance(my_tesla, ElectricCar)) # True → object belongs to ElectricCar as well
