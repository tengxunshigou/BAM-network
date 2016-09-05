# BAM
import matplotlib.pyplot as plt
import numpy as np

from BAM_layer import BAMLAYER
from abc import ABCMeta, abstractmethod
import BinaryCoding as bc

# sample size
class BAMNET:
    __metaclass__ = ABCMeta
    # x is input of the net(such as [names])
    # y is output of the net(such as [phone numbers])
    # (already encoding)

    def __init__(self, x, y):

        # encoding for x_input and y_input (int matrix)
        self.x_input = x
        self.y_input = y
        # row and col of input samples
        self.num_data, b = np.shape(x)
        self.num_data, c = np.shape(y)
        # x layer of the net
        self.x_layer = BAMLAYER(b)
        # y layer of the net
        self.y_layer = BAMLAYER(c)

    # encoding for x_samples and y_samples by three parameter(6,8,6)
    # this part should be changed if input data has changed format
    # so this function should move to main.py
    # @abstractmethod
    # def Encoding(self, in_char, out_char, bits_per_char): pass
    #
    # # decoding program
    # @abstractmethod
    # def Decoding(self, layer): pass

    def GetOutput(self, layer):
        return layer.getOutput()

    # system energy according to E=-XWY(T)
    def NetEnergy(self, x, y, weight):
        a = np.dot(x.T, weight.T)
        b = np.dot(a, y)
        return -b

    # should be improved to replace Hebb learning rule
    # calculate weights from x to y (y to x is a transform matrix of weights)
    def CalculateWeights(self):
        weight = np.dot(self.y_input.T, self.x_input)
        self.x_layer.setWeight(weight)
        self.y_layer.setWeight(weight.T)
        print "weights from x to y:\n", self.x_layer.getWeight()[0], "\n"
        print "weights from y to x:\n", self.y_layer.getWeight(), "\n"
        return 0

    # calculate output from "fromm" layer to "to" layer
    def PropagateLayer(self, fromm, to):
        energy = self.NetEnergy(fromm.output, to.output,fromm.weight)
        stable = True
        product = np.dot(fromm.weight, fromm.output)
        for i in range(len(product)):
            if product[i] < 0:
                product[i] = -1
            elif product[i] > 0:
                product[i] = 1
            if product[i] != to.output[i]:
                stable = False
        to.setInput(product)
        # print to.output
        # print fromm.output

        return stable

    def PropagateNet(self, fromm, to):
        stable1 = False
        stable2 = True
        # only both of stable1 and stable2 are true can stop this circle
        while( not(stable1 and stable2)):
            stable1 = self.PropagateLayer(fromm, to)
            stable2 = self.PropagateLayer(to, fromm)

        return 0
        # from fromm layer to 'to' layer ,pattern is association sample

    def SimulateNet(self, fromm, to):
        inputx = self.x_input if (fromm == self.x_layer) else self.y_input
        for pattern in inputx:
            fromm.setInput(pattern)
            print " -> ",
            to.setRandom()
            bc.Decoding(to.getOutput())
            print " | ",
            bc.Decoding(fromm.getOutput())
            self.PropagateNet(fromm, to)
            print " -> ",
            bc.Decoding(to.getOutput())
            print ""
        return 0








