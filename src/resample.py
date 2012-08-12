#! /usr/bin/python
# -*- coding: utf-8 -*-

#debug 
import pdb; 

import numpy, scipy
from scipy import interpolate

def resampleImage(img, outShape = (64,64), outType = numpy.uint8):
    """ Function resamples image. At this time is only one channel 2D, 
    in a future there will be implemented genereal dimension and multichannel
    version"""
    inShape = img.shape 
    

    kernelOut = numpy.zeros(outShape,outType)

    x = numpy.array(range(0,inShape[0]))
    y = numpy.array(range(0,inShape[1]))

    z = img

    xx = numpy.linspace(x.min(),x.max(),outShape[0])
    yy = numpy.linspace(y.min(),y.max(),outShape[1])

    newKernel = interpolate.RectBivariateSpline(x,y,z, kx=2,ky=2)

    imgOut = newKernel(xx,yy)
    return imgOut


if __name__ == "__main__":
    import numpy, scipy
    from scipy import interpolate
    from scipy import misc
    import matplotlib.pyplot as plt

    #kernelIn = numpy.array([[0,-2,0],
    #                 [-2,11,-2],
    #                              [0,-2,0]])
    # lena image
    img = misc.lena()
    pdb.set_trace();
    plt.figure()
    #plt.imshow(l)
    imgr = resampleImage(img)
    plt.imshow(imgr, cmap=plt.cm.gray)
    plt.show()
    plt.close()
#    inKSize = len(kernelIn)
#    outKSize = 5
#
#    kernelOut = numpy.zeros((outKSize,outKSize),numpy.uint8)
#
#    x = numpy.array([0,1,2])
#    y = numpy.array([0,1,2])
#
#    z = kernelIn
#
#    xx = numpy.linspace(x.min(),x.max(),outKSize)
#    yy = numpy.linspace(y.min(),y.max(),outKSize)
#
#    newKernel = interpolate.RectBivariateSpline(x,y,z, kx=2,ky=2)
#
#    kernelOut = newKernel(xx,yy)
#
#    print kernelOut
#    
#    # random image
#    #dat = numpy.random.random(100)*255
#    #dat = dat.astype(numpy.int)
#    #dat = dat.reshape(10,10,1)
#    #print dat
#    #print lbp2(dat)
#
#    lbpkern = generateKernel2()
#    #print len(lbpkern)
#    
#    imlbp = lbp2oneslice(dat[:,:], lbpkern)
#    print dat[:,:]
#    print imlbp
#
#    feat=features(imlbp)
#    
#    
#    #print 'lena' , dat
#    
#    
#    #import matplotlib.image as mpimg
#    #import numpy as np
#    plt.figure()
#    #plt.imshow(l)
#    plt.imshow(dat, cmap=plt.cm.gray)
#    plt.show()
#    plt.close()
#    
#    
#    
#    pylab.figure()
#    pylab.plot(feat[0],label="LBP Code")
#    pylab.legend()
#    pylab.show()
#    #
#    
#    #misc.imsave('lena.png', l) # uses the Image module (PIL)
#    
#    #import pylab as pl
#    #pl.imshow(l)
#    print 'Konec'
#
##    beta = [2, 4, 16, 32]
##
##    pylab.figure()
##    for b in beta:
##        w = numpy.kaiser(101,b) 
##        pylab.plot(range(len(w)),w,label="beta = "+str(b))
##    pylab.xlabel('n')
##    pylab.ylabel('W_K')
##    pylab.legend()
##    pylab.show()
##    
##    # random data generation
##    y = numpy.random.random(100)*100 
##    for i in range(100):
##        y[i]=y[i]+i**((150-i)/80.0) # modifies the trend
##
##    # smoothing the data
##    pylab.figure(1)
##    pylab.plot(y,'-k',label="original signal",alpha=.3)
##    for b in beta:
##        yy = smooth(y,b) 
##        pylab.plot(yy,label="filtered (beta = "+str(b)+")")
##    pylab.legend()
##    pylab.show()
##
##
##    # 2D convolution
##
##    from scipy import signal as sg
##    #dat = numpy.empty((3,3,3))
##
##
##
##    print sg.convolve([[255, 7, 3],
##                       [212, 240, 4],
##                       [218, 216, 230]], [[1, -1]], "valid")
##    # gives
##
##    #a = numpy.empty((3,3,3))
##
##    dat = numpy.random(30).reshape(2,3,5)
##    mask = numpy.zeros((2,2,2))
##    mask[0,0,0] = 1
##    mask[1,1,1] = -1
##
##    print sg.convolve(dat, mask, "valid")
##
