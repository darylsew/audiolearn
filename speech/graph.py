#Example of how to extract data from a wav file using the modified svt library.
#Also useful for graphing or playing around with data.
import svt
import matplotlib
from matplotlib import pyplot
import pylab
from mpl_toolkits.mplot3d import Axes3D
import random
import numpy

#The line needed to get data from the first channel.
centroids, frequencies, volumes = svt.processWav("../pyaudio/ooo.wav", 1)
"""
#Samples some of the data.
print centroids[1]
print frequencies[1]
print volumes[1]

for i in range(0, int(len(frequencies[1])/20)):
    print frequencies[1][i]
"""
#Graphs frequencies, centroids, and volumes on 2d plots; frequencies should really be 3d but I can't figure out how to 3d graph them so a number of 2d graphs should suffice for understanding the data.

numbers = []
for i in range(len(frequencies[1])):
    numbers.append(i)

#analysis codeeeeeeeee
for i in range(3):
    matplotlib.pyplot.scatter(numbers, frequencies[i])
    matplotlib.pyplot.show()

matplotlib.pyplot.scatter(range(len(centroids)), centroids)
matplotlib.pyplot.show()
matplotlib.pyplot.scatter(range(len(volumes)), volumes)
matplotlib.pyplot.show()

"""
#Failed 3d graph code
fig = pylab.figure()
ax = Axes3D(fig)

sequence_containing_x_vals = range(0, 2050
sequence_containing_y_vals = range(0, 2050)
sequence_containing_z_vals = range(0, 2050)

random.shuffle(sequence_containing_x_vals)
random.shuffle(sequence_containing_y_vals)
random.shuffle(sequence_containing_z_vals)

ax.scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals)
pyplot.show()
"""
"""
f = open("volumes.txt", 'w')
for item in volumes:
    print>>f, item
f.close()
f = open("centroids.txt", 'w')
for item in centroids:
    print>>f, item
f.close()
f = open("frequencies.txt", 'w')
for i in range(len(frequencies)):
    print>>f, "Frequencies at frame"+str(i)
    for item in frequencies[i]:
        print>>f, item
f.close()
"""
#Simple statistics

print "Volumes"
print "Max: " + str(max(volumes))
print "Avg: " + str(numpy.mean(volumes))
print "Min: " + str(min(volumes))
print "Std: " + str(numpy.std(volumes))
print "Med: " + str(numpy.median(volumes))

print "Centroids"
print "Max: " + str(max(centroids))
print "Avg: " + str(numpy.mean(centroids))
print "Min: " + str(min(centroids))
print "Std: " + str(numpy.std(centroids))
print "Med: " + str(numpy.median(centroids))
q = []
for i in range(len(frequencies)):
    for j in frequencies[i]:
        q.append(j)
print "Frequencies"
print "Max: " + str(max(q))
print "Avg: " + str(numpy.mean(q))
print "Min: " + str(min(q))
print "Std: " + str(numpy.std(q))
print "Med: " + str(numpy.median(q))
