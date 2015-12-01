import pylab
import numpy

x = numpy.linspace(-15, 15, 100)
y = numpy.sin(x)/x

pylab.plot(x,y)
pylab.plot(x,y,'co')
pylab.plot(x,2*y,x,3*y)
pylab.show()

