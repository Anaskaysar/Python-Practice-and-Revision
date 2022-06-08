class Vehicle:
    def general_usage(self):
        print("General use: transportation")

class Car(Vehicle):
    def __init__(self):
        print("I am car")
        self.wheels = 4
        self.has_roof = True
    def specific_usage(self):
        print("Specific use: Big transprotation")


class MotorCycle(Vehicle):
    def __init__(self):
        print("I am motor cycle")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        print("Specific use: Racing")


c = Car()
c.general_usage()
c.specific_usage()