class Airplane:
    def __init__(self):
        self.speed = 0
        self.color = None
        self.model = None
        self.capacity = 0
        self.country = None


    def turn_on(self):
        print("Airplane engine started")

    def turn_off(self):
        print("Airplane engine stopped.")

    def fly(self):
        if self.speed > 0:
            print("Airplane is flying.")
        else:
            print("Airplane needs to gain speed to fly.")

    
class Car:
    def __init__(self):
        self.speed = 0
        self.color = None
        self.License_plate = None
        self.model = None
        self.capacity = 0
        self.number_of_wheels = 4

    def turn_on(self):
        print("Car engine started.")

    def turn_off(self):
        print("Car engine stopped.")

    def boooogh(self):
        print("Car horn: Beep beep!")

    
class Bicycle:
    def __init__(self):
        self.color = None
        self.model = None
        self.number_of_wheels = 2
        self.speed = 0

    def turn_on(self):
        print("Bicycle is ready to ride.")

    def turn_off(self):
        self.speed = 0
        print("Bicycle stopped.")


if __name__ == "__main__":

    plane = Airplane()
    plane.color = "white"
    plane.model = "Boeing 737"
    plane.capacity = 200
    plane.speed = 500
    plane.turn_on()
    plane.fly()


    car = Car()
    car.color = "blue"
    car.License_plate = "ABC-123"
    car.model = "Toyota"
    car.turn_on()
    car.boooogh()

    bike = Bicycle()
    bike.color = "red"
    bike.model = "Mountain Bike"
    bike.turn_on()
    