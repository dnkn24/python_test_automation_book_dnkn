class Car:
    make = ''
    model = ''
    year = ''
    color = 'undefined'
    def __init__(self,make, model, year):
        count = 0
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        self.color = 'Yellow'
        return f"Returning info about a car"
        return f"Count: {count}"
        return f"Make: {self.make}"


my_car=Car('Ford','Ranger', 2024)

print(my_car)
print(type(1))
print(type(my_car))
print(my_car.make,my_car.model,my_car.year)
print(my_car.color)
print(my_car.display_info())
print(my_car.color)