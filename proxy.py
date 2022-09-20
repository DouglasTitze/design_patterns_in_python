from re import L
import time


class Person:
    """Defining the resourse intensive object"""

    def busy(self):
        print("I am busy")

    def available(self):
        print("I am available")


class Proxy:
    """Define the relatively less intensive proxy"""

    def __init__(self):
        self.busy = "No"
        self.person = None

    def is_busy(self):
        print("Checking status")

        if self.busy == "No":
            self.person = Person()
            time.sleep(2)
            self.person.available()

        else:
            time.sleep(2)
            print("Sorry we are busy")


# Create proxy
p = Proxy()

# Create a person
p.is_busy()

# Change status
p.busy = "Yes"

# Try again
p.is_busy()
