# -------------------------------------
# Multiple Inheritance in Python
# -------------------------------------
# In Python, a class can inherit from more than one class.
# This allows combining features/behaviors of multiple parent classes.

# -------------------------------
# Base Class 1
# -------------------------------
class Car:
    total_car = 0   # Class variable (shared by all cars)
    
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model
        Car.total_car += 1
            
    def full_name(self):
        return f"{self.brand} {self.__model}"
    
    @property
    def model(self):
        return self.__model
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"    


# -------------------------------
# Base Class 2
# -------------------------------
class Battery:
    def battery_info(self):
        return "This car has a battery."


# -------------------------------
# Base Class 3
# -------------------------------
class Engine:
    def engine_info(self):
        return "This car has an engine."


# -------------------------------
# Derived Class with Multiple Inheritance
# -------------------------------
class ElectricCar(Car, Battery, Engine):
    def __init__(self, brand, model, battery_size):
        # Only calls Car's __init__ (first parent in MRO)
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel(self):
        return "Runs on Electric Charge"


# -------------------------------
# Using Multiple Inheritance
# -------------------------------
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

print(my_tesla.full_name())          # From Car
print(my_tesla.battery_info())       # From Battery
print(my_tesla.engine_info())        # From Engine
print(my_tesla.fuel())               # Overridden in ElectricCar
print("Total cars created:", Car.total_car)


# -------------------------------
# Method Resolution Order (MRO)
# -------------------------------
# Python follows C3 Linearization (depth-first, left-to-right)
print(ElectricCar.mro())
