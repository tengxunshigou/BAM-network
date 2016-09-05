import matplotlib as plt
import numpy as np

class BAMLAYER:
    def __init__(self, units):
        # number of units in this layer,sum of neuron(bits_per_char * in_chars)
        self.units = units
        # output of ith unit
        self.output = np.ones(self.units)
        # weights
        self.weight = []

    # getter and setter methods
    def setUnits (self, units):
        self.units = units

    def getUnits (self):
        return self.units

    def setInput (self, output):
        self.output = output

    def getOutput (self):
        return self.output

    def getWeight(self):
        return self.weight

    def setWeight(self, weight):
        self.weight = weight

    # should be -1 or +1 , not 0 or 1
    def setRandom(self):
        for i in range(self.units):
            a = np.random.randint(0, 2)
            self.output[i] = (-1 if (a % 2 == 0) else 1)



