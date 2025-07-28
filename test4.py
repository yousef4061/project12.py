class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.emoji = "🐾"

    def walk(self):
        return f"{self.emoji} {self.name} is walking..."

    def show(self):
        return f"Name: {self.name}, age: {self.age}"

class Eagle(Animal):
    def __init__(self, name, age, speed):
        super().__init__(name, age)
        self.speed = speed
        self.number_of_legs = 2
        self.emoji = "🦅"

    def fly(self):
        return f"{self.emoji} {self.name} is flying at {self.speed} km/h!"

    def show(self):
        return f"{super().show()}, speed: {self.speed} km/h, Legs: {self.number_of_legs}"

class Fish(Animal):
    def __init__(self, name, age, max_height):
        super().__init__(name, age)
        self.max_height = max_height
        self.emoji = "🐟"

    def swim(self):
        return f"{self.emoji} {self.name} is swimming at depth {self.max_height}m!"

    def show(self):
        return f"{super().show()}, Max Depth: {self.max_height}m"

if __name__ == "__main__":
    nemo = Fish("Nemo", 4, 10)
    print(nemo.show())
    print(nemo.swim())
    eagle = Eagle("Sky", 3, 80)
    print(eagle.show())
    print(eagle.fly())
