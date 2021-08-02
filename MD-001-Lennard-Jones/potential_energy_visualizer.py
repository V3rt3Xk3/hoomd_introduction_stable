import matplotlib.pyplot
import numpy

sigma = 1.78
epsilon = 2
r = numpy.linspace(1.5, 3, 500)
V_lj = 4 * epsilon * ((sigma / r)**12 - (sigma / r)**6)

matplotlib.pyplot.plot(r, V_lj)
matplotlib.pyplot.xlabel('r')
matplotlib.pyplot.ylabel('V')
matplotlib.pyplot.show()

