import random

class Qubit():
    # The Constructor
    def __init__(self):
        self.value = random.random()
        self.polarization = random.random()

    # generates a new qubit
    def new(self):
        self.value = random.random()
        self.polarization = random.random()

    # sets the value and the polarization
    def set(self, value, polarization):
        self.value = value
        self.polarization = polarization

    def measure(self, polarization):
        # check if the polarization matches
        if self.polarization == polarization:
            return self.value
        # If not match selt current polartization to the polarization parsed in
        else:
            self.polarization = polarization
            self.value = random.random()
            return self.value

        
    

