#!/usr/bin/env python
import matplotlib as plt
import numpy as np
from BAM import BAMNET
import BinaryCoding as bc

x = ["zhang", "wangz", "lisa"]
y = ["6843726", "8034673", "726015"]
# x = ["TINA","ANTJE","LISA","TOMCAT","wang","zhang","song"]
# y = ["6843726","8034673","7260915","1234567","42342","7567567","4467457"]

x_samples, y_samples = bc.init_data(x, y)
# print "x_samples after convert:\n", x_samples, "\n", "y_samples after convert:\n", y_samples
x_input, y_input = bc.Encoding(x_samples, y_samples)
bam = BAMNET(x_input, y_input)
bam.CalculateWeights()

print "from x_layer to y_layer:"
bam.SimulateNet(bam.x_layer, bam.y_layer)
print "from y_layer to x_layer:"
bam.SimulateNet(bam.y_layer, bam.x_layer)

