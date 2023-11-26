# Task 01
print("Task 01")
class Elevator:
  def __init__(self, bottom, top):
    self.bottom = bottom
    self.top = top
    self.current_floor = bottom

  def go_to_floor(self, floor):
    if floor < self.bottom or floor > self.top:
      print("Invalid floor")
      return

    while self.current_floor != floor:
      if self.current_floor < floor:
        self.floor_up()
      else:
        self.floor_down()

  def floor_up(self):
    if self.current_floor < self.top:
      self.current_floor += 1
      print("Going up to floor", self.current_floor)
    else:
      print("Already at the top floor")

  def floor_down(self):
    if self.current_floor > self.bottom:
      self.current_floor -= 1
      print("Going down to floor", self.current_floor)
    else:
      print("Already at the bottom floor")

if __name__ == "__main__":
  elevator = Elevator(1, 5)
  elevator.go_to_floor(5)
  elevator.go_to_floor(1)

  #task 02
print("TasK 02")


class Elevator:
  def __init__(self, bottom, top):
    self.bottom = bottom
    self.top = top
    self.current_floor = bottom

  def go_to_floor(self, floor):
    if floor < self.bottom or floor > self.top:
      print(f"Invalid floor {floor}")
      return

    while self.current_floor != floor:
      if self.current_floor < floor:
        self.floor_up()
      else:
        self.floor_down()

  def floor_up(self):
    if self.current_floor < self.top:
      self.current_floor += 1
      print(f"Going up to floor {self.current_floor}")
    else:
      print("Already at the top floor")

  def floor_down(self):
    if self.current_floor > self.bottom:
      self.current_floor -= 1
      print(f"Going down to floor {self.current_floor}")
    else:
      print("Already at the bottom floor")


class Building:
  def __init__(self, bottom, top, num_elevators):
    self.bottom = bottom
    self.top = top
    self.elevators = []
    for _ in range(num_elevators):
      self.elevators.append(Elevator(bottom, top))

  def run_elevator(self, elevator_num, destination_floor):
    if elevator_num < 0 or elevator_num >= len(self.elevators):
      print(f"Invalid elevator number {elevator_num}")
      return

    if destination_floor < self.bottom or destination_floor > self.top:
      print(f"Invalid destination floor {destination_floor}")
      return

    self.elevators[elevator_num].go_to_floor(destination_floor)


if __name__ == "__main__":
  building = Building(1, 10, 2)
  building.run_elevator(0, 5)
  building.run_elevator(1, 7)
  building.run_elevator(0, 1)
  building.run_elevator(1, 3)

#task 03
print("Task 03")


class Elevator:
  def __init__(self, bottom, top):
    self.bottom = bottom
    self.top = top
    self.current_floor = bottom

  def go_to_floor(self, floor):
    if floor < self.bottom or floor > self.top:
      print(f"Invalid floor {floor}")
      return

    while self.current_floor != floor:
      if self.current_floor < floor:
        self.floor_up()
      else:
        self.floor_down()

  def floor_up(self):
    if self.current_floor < self.top:
      self.current_floor += 1
      print(f"Going up to floor {self.current_floor}")
    else:
      print("Already at the top floor")

  def floor_down(self):
    if self.current_floor > self.bottom:
      self.current_floor -= 1
      print(f"Going down to floor {self.current_floor}")
    else:
      print("Already at the bottom floor")

  def fire_alarm(self):
    self.go_to_floor(self.bottom)
    print(f"Elevator {self.current_floor} moved to the bottom floor due to fire alarm")


class Building:
  def __init__(self, bottom, top, num_elevators):
    self.bottom = bottom
    self.top = top
    self.elevators = []
    for _ in range(num_elevators):
      self.elevators.append(Elevator(bottom, top))

  def run_elevator(self, elevator_num, destination_floor):
    if elevator_num < 0 or elevator_num >= len(self.elevators):
      print(f"Invalid elevator number {elevator_num}")
      return

    if destination_floor < self.bottom or destination_floor > self.top:
      print(f"Invalid destination floor {destination_floor}")
      return

    self.elevators[elevator_num].go_to_floor(destination_floor)

  def fire_alarm(self):
    for elevator in self.elevators:
      elevator.fire_alarm()


if __name__ == "__main__":
  building = Building(1, 10, 2)
  building.run_elevator(0, 5)
  building.run_elevator(1, 7)
  building.run_elevator(0, 1)
  building.run_elevator(1, 3)

  # Trigger a fire alarm
  building.fire_alarm()
 #task 04
print("Task 04")

import random


class Car:
    def __init__(self, registration_number):
        self.registration_number = registration_number
        self.maximum_speed = random.randint(100, 200)
        self.current_speed = self.maximum_speed
        self.travelled_distance = 0

    def accelerate(self):
        speed_change = random.randint(-10, 15)
        self.current_speed = max(0, min(self.current_speed + speed_change, self.maximum_speed))

    def drive(self):
        self.travelled_distance += self.current_speed


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate()
            car.drive()

    def print_status(self):
        print("| Registration number | Maximum speed | Current speed | Travelled distance |")
        print("|---|---|---|---|")
        for car in self.cars:
            print(f"|{car.registration_number}|{car.maximum_speed}|{car.current_speed}|{car.travelled_distance}|")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
            return False


def main():
    cars = []
    for i in range(1, 11):
        max_speed = random.randint(100, 200)
        registration_number = f"ABC-{i}"
        car = Car(max_speed)
        car.registration_number = registration_number
        cars.append(car)

    race = Race("Grand Demolition Derby", 8000, cars)

    hour = 0
    while not race.race_finished():
        race.hour_passes()
        hour += 1

        if hour % 10 == 0 or race.race_finished():
                race.print_status()

    print("Race finished!")

if __name__ == "__main__":
    main()


