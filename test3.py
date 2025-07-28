class Vehicle:
    def __init__(self):
        self.speed = 0
        self.color = None
        self.model = None
    
    def turn_on(self):
        print("Vehicle is turned on.")
    
    def turn_off(self):
        print("Vehicle is turned off.")

    def gear_change(self):
        print("Gear changed.")

class Airplane(Vehicle):
    def __init__(self):
        super().__init__()
        self.capacity = 0
        self.country = None

    def fly(self):
        print("Airplane is flying.")

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.license_plate = None

    def fly(self):
        print("Airplane is flying.")

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.license_plate = None

    def drive(self):
        print("Car is driving.")


jumbo = Airplane()
pride = Car()


jumbo.capacity = 300
jumbo.country = "Iran"
pride.license_plate = "12384-IRAN12"
pride.color = "green"


jumbo.fly()
pride.drive()
pride.turn_on()
