#task 01
print("Task 01")
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

car=Car("ABC-123","142 km/h")
print("Registration number:", car.registration_number)
print("Maximum speed:", car.maximum_speed)
print("Current speed:", car.current_speed)
print("Travelled distance:", car.travelled_distance)

#Task 02

print("Task 02")

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        if change_of_speed < 0:
            new_speed = self.current_speed + change_of_speed
            if new_speed >= 0:
                self.current_speed = new_speed
                print(f"Car is slowing down. Current speed: {self.current_speed} km/h")
            else:
                print("Cannot slow down below zero")
        else:
            new_speed = self.current_speed + change_of_speed
            if new_speed <= self.maximum_speed:
                self.current_speed = new_speed
                print(f"Car is accelerating. Current speed: {self.current_speed} km/h")
            else:
                print(f"Cannot exceed maximum speed is: {self.maximum_speed} km/h")

car = Car("ABC-123", 142)

print("Initial speed:", car.current_speed)

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
car.accelerate(-200)

print("Emergency brake:",car.current_speed, " Final speed: 0 ")

#Task 03
print("Task 03")

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        if change_of_speed < 0:
            new_speed = self.current_speed + change_of_speed
            if new_speed >= 0:
                self.current_speed = new_speed
                print(f"Car is slowing down. Current speed: {self.current_speed} km/h")
            else:
                print("Cannot slow down below zero")
        else:
            new_speed = self.current_speed + change_of_speed
            if new_speed <= self.maximum_speed:
                self.current_speed = new_speed
                print(f"Car is accelerating. Current speed: {self.current_speed} km/h")
            else:
                print(f"Cannot exceed maximum speed is: {self.maximum_speed} km/h")

    def drive(self, hours):
        self.hours = hours
        travelled_distance = self.current_speed * hours
        self.travelled_distance += travelled_distance

        if self.current_speed > self.maximum_speed:
            print(f"Warning: Car exceeded maximum speed of {self.maximum_speed} km/h.")
            self.current_speed = self.maximum_speed

car = Car("ABC-123", 142)
car.current_speed = 60


print("Initial speed:", car.current_speed)

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)

car.drive(1.5)
print("Initial traveled distance:", car.travelled_distance)
print("Final traveled distance:", car.travelled_distance)

car.accelerate(-200)
print("Emergency brake:",car.current_speed,)

# task 04
print("task 04")
import random

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        if change_of_speed < 0:
            new_speed = self.current_speed + change_of_speed
            if new_speed >= 0:
                self.current_speed = new_speed
            else:
                print("Cannot slow down below zero")
        else:
            new_speed = self.current_speed + change_of_speed
            if new_speed <= self.maximum_speed:
                self.current_speed = new_speed
            else:
                print("Cannot exceed maximum speed")

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

cars = []

for i in range(1, 11):
    registration_number = f"ABC-{i}"
    maximum_speed = random.randint(100, 200)
    car = Car(registration_number, maximum_speed)
    cars.append(car)

race_over = False
hour = 0

while not race_over:

    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)


    for car in cars:
        car.drive(1)


    for car in cars:
        if car.travelled_distance >= 10000:
            race_over = True
            break

    hour += 1

# Print the properties of each car
print("Race results:")
print("Registration Number | Maximum Speed | Current Speed | Travelled Distance")
print("------------------ | ------------ | ------------ | -------------------")
for car in cars:
    print(f"{car.registration_number} | {car.maximum_speed} | {car.current_speed} | {car.travelled_distance}")

