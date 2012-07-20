#! /usr/bin/python
# -*- coding: utf-8 -*-

# original source
# http://glowingpython.blogspot.cz/2012/02/convolution-with-numpy.html
import numpy
import pylab
from scipy import signal as sg

def generateKernel2():
    kern1=numpy.zeros((3,3))
    kern1[1,1] = -1
    kern1[0,0] = 1

    kern2=numpy.zeros((3,3))
    kern2[1,1] = -1
    kern2[1,0] = 1

    kern3=numpy.zeros((3,3))
    kern3[1,1] = -1
    kern3[2,0] = 1

    kern4=numpy.zeros((3,3))
    kern4[1,1] = -1
    kern4[0,1] = 1

    kern5=numpy.zeros((3,3))
    kern5[1,1] = -1
    kern5[2,1] = 1


    kern6=numpy.zeros((3,3))
    kern6[1,1] = -1
    kern6[0,2] = 1

    kern7=numpy.zeros((3,3))
    kern7[1,1] = -1
    kern7[1,2] = 1

    kern8=numpy.zeros((3,3))
    kern8[1,1] = -1
    kern8[2,2] = 1


    
##    kern1=[[1, 0, 0],[0, -1, 0], [0, 0, 0]]
##    kern2=[[0, 1, 0],[0, -1, 0], [0, 0, 0]]
##    kern3=[[0, 0, 1],[0, -1, 0], [0, 0, 0]]
##    kern4=[[0, 0, 0],[1, -1, 0], [0, 0, 0]]
##    kern5=[[0, 0, 0],[0, -1, 1], [0, 0, 0]]
##    kern6=[[0, 0, 0],[0, -1, 0], [1, 0, 0]]
##    kern7=[[0, 0, 0],[0, -1, 0], [0, 1, 0]]
##    kern8=[[0, 0, 0],[0, -1, 0], [0, 0, 1]]

    return [kern1, kern2, kern3, kern4, kern5, kern6, kern7, kern8]
    

def lbp2oneslice (dat, lbpkern):
    """ Function return LBP code of 2D data"""
    dataout = numpy.zeros(dat.shape, dtype=numpy.int)
    
    for i in range(1,len (lbpkern)):
        print i
        onekern = lbpkern[i]

        
        dataconv = sg.convolve(dat, onekern, "same")
        
        dataout  = (dataconv > 0) * 1 * pow(2,i-1) + dataout
        print dataout
        
    return dataout


def lbp2(dat):
    """ Function returns LBP code """
    szdat = dat.shape

    # float has no sense, will be changed in future
    outdat = numpy.zeros(szdat, dtype=float)
    
    # number of slices
    szz = 1
    
    if len(szdat) > 2:
        szz = szdat[2]
        
    
    for i in range(0,(szz)):
        outdat[:,:,i] = dat[:,:,i]

    return outdat
        

def smooth(x,beta):
    """ kaiser window smoothing """
    window_len=11
    # extending the data at beginning and at the end
    # to apply the window at the borders
    s = numpy.r_[x[window_len-1:0:-1],x,x[-1:-window_len:-1]]
    w = numpy.kaiser(window_len,beta)
    y = numpy.convolve(w/w.sum(),s,mode='valid')
    return y[5:len(y)-5]

if __name__ == "__main__":
    dat = numpy.random.random(100)*255
    dat = dat.astype(numpy.int)
    dat = dat.reshape(10,10,1)
    print dat
    print lbp2(dat)

    lbpkern = generateKernel2()
    print len(lbpkern)
    
    dataout = lbp2oneslice(dat[:,:,0], lbpkern)
    print dat[:,:,0]
    print dataout
    
    

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
