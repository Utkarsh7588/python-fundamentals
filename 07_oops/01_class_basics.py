# -------------------------------
# Python Class Basics Explained
# -------------------------------

class Car:
    # Class variable (shared by all instances of Car)
    total_car = 0

    def __init__(self, brand, model):
        """
        Constructor (initializer)
        Runs automatically when a new Car object is created.
        'self' represents the instance being created.
        """
        self.brand = brand          # Instance variable (unique per object)
        self.__model = model        # Private variable (name mangled: _Car__model)
        Car.total_car += 1          # Increase total_car count whenever a Car is created

    def full_name(self):
        """
        Instance method: works with object data (self).
        Returns the brand and model of the car.
        """
        return f"{self.brand} {self.__model}"

    @property
    def model(self):
        """
        Property decorator: lets us access __model like an attribute,
        without needing to call it like a method.
        Example: my_car.model instead of my_car.get_model()
        """
        return self.__model

    @staticmethod
    def general_description():
        """
        Static method: belongs to the class, but does not depend on any instance.
        Can be called using class or object.
        """
        return "Cars are means of transport"


# -------------------------------
# Creating Objects (Instances)
# -------------------------------

my_car = Car("Toyota", "Corolla")     # First car
another_car = Car("TATA", "Safari")   # Second car

# -------------------------------
# Accessing Class & Instance Features
# -------------------------------

print(Car.total_car)                # 2 → Shared by all objects
print(my_car.full_name())           # Toyota Corolla
print(Car.general_description())    # Cars are means of transport (called from class)
print(my_car.general_description()) # Also works when called from instance
print(my_car.model)                 # Corolla (accessed using @property)
