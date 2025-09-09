# -------------------------------------
# Polymorphism in Python
# -------------------------------------
# Polymorphism = "Many forms"
# In OOP, this means the same method name can behave differently
# depending on the object (class) that is calling it.

# -------------------------------
# Base Class
# -------------------------------
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def full_name(self):
        return f"{self.brand} {self.model}"   
    
    # Common method (will be overridden in child class)
    def fuel(self):
        return "Petrol or Diesel" 


# -------------------------------
# Derived Class (Inheritance + Overriding)
# -------------------------------
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        # Reuse parent constructor with super()
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    # Overriding parent method → Polymorphism in action
    def fuel(self):
        return "Electric Charge"   


# -------------------------------
# Using Polymorphism
# -------------------------------

my_car = Car("Toyota", "Corolla")
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

# Same method name → behaves differently depending on object
print(my_car.fuel())     # Petrol or Diesel
print(my_tesla.fuel())   # Electric Charge

# Both objects can be used interchangeably in a loop
for vehicle in [my_car, my_tesla]:
    print(vehicle.full_name(), "runs on", vehicle.fuel())
