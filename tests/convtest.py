#! /usr/bin/python
# -*- coding: utf-8 -*-

# original source
# http://glowingpython.blogspot.cz/2012/02/convolution-with-numpy.html

import numpy
import pylab

beta = [2, 4, 16, 32]

pylab.figure()
for b in beta:
    w = numpy.kaiser(101,b) 
    pylab.plot(range(len(w)),w,label="beta = "+str(b))
pylab.xlabel('n')
pylab.ylabel('W_K')
pylab.legend()
pylab.show()


def smooth(x,beta):
    """ kaiser window smoothing """
    window_len=11
    # extending the data at beginning and at the end
    # to apply the window at the borders
    s = numpy.r_[x[window_len-1:0:-1],x,x[-1:-window_len:-1]]
    w = numpy.kaiser(window_len,beta)
    y = numpy.convolve(w/w.sum(),s,mode='valid')
    return y[5:len(y)-5]





# random data generation
y = numpy.random.random(100)*100 
for i in range(100):
    y[i]=y[i]+i**((150-i)/80.0) # modifies the trend

# smoothing the data
pylab.figure(1)
pylab.plot(y,'-k',label="original signal",alpha=.3)
for b in beta:
    yy = smooth(y,b) 
    pylab.plot(yy,label="filtered (beta = "+str(b)+")")
pylab.legend()
pylab.show()


# 2D convolution

from scipy import signal as sg
#dat = numpy.empty((3,3,3))



print sg.convolve([[255, 7, 3],
                   [212, 240, 4],
                   [218, 216, 230]], [[1, -1]], "valid")
# gives

#a = numpy.empty((3,3,3))

dat = numpy.arange(30).reshape(2,3,5)
mask = numpy.zeros((2,2,2))
mask[0,0,0] = 1
mask[1,1,1] = -1

print sg.convolve(dat, mask, "valid")

