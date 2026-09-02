"""Question 15: Polymorphism with a Common Interface
Question: Define a base class Device with a method turn_on. Define derived classes Computer and Printer that implement their own versions of turn_on.
"""

class Device:
    def turn_on(self):
        pass

class Computer(Device):
    def turn_on(self):
        return f"The Computer has turned on!"

class Printer(Device):
    def turn_on(self):
        return f"The Printer has turned on!"

device_type=input("Enter device type:")
if device_type=="computer":
    device=Computer()
elif device_type=="printer":
    device=Printer()
else:
    print("Invalid device type")
    device=None

if device:
    print(device.turn_on())