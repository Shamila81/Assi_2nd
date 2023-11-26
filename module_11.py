#Task 01
print("Task 01")
class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(f"Name: {self.name}")


class Book(Publication):

    def __init__(self, name, author, page_count):

        super().__init__(name)
        self. Author = author
        self.page_count = page_count

    def print_information(self):
        super().print_information()
        print(f"Author: {self.author}")
        print(f"Page count: {self.page_count}")


class Magazine(Publication):
    def __init__(self, name, chief_editor):

        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        super().print_information()
        print(f"Chief editor: {self.chief_editor}")


donald_duck = Magazine("Donald Duck", "Aki Hyyppä")
compartment_no_6 = Book("Compartment No. 6", "Rosa Liksom", 192)

donald_duck.print_information()
compartment_no_6.print_information()


 #Task 02
print("Task 02")


class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0


class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery_capacity):
        super().__init__(registration_number, maximum_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, tank_volume):
        super().__init__(registration_number, maximum_speed)
        self.tank_volume = tank_volume

electric_car = ElectricCar("ABC-15", 180, 52.5)

gasoline_car = GasolineCar("ACD-123", 165, 32.3)

electric_car.current_speed = 120
gasoline_car.current_speed = 135

# Electric car drive for 3 hours
electric_car.travelled_distance += electric_car.current_speed * 3

# Gasoline car drive for 3 hours
gasoline_car.travelled_distance += gasoline_car.current_speed * 3

print("Electric car's kilometer counter:", electric_car.travelled_distance)
print("Gasoline car's kilometer counter:", gasoline_car.travelled_distance)
