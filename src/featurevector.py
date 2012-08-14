#! /usr/bin/python
# -*- coding: utf-8 -*-

#debug
import pdb; 
#  pdb.set_trace();

from sklearn import svm
X = [[0, 0], [1, 1],[0,4],[0.1, 0.2]]
Y = [0, 1, 2 , 0]
clf = svm.SVC()
clf.fit(X, Y)  
print clf.predict([[2,3]])

dec = clf.decision_function([[1]])
dec.shape[1]

#import scipy.io
#mat = scipy.io.loadmat('step0.mat')

#print mat



def fvector(data, method = 'lbp'):
    """ Method for building feature vector """

    fv = 0
    if method == 'lbp':
        from scipy import misc
        import matplotlib.pyplot as plt
        import lbpsimple
        

        lbpkern = lbpsimple.generateKernel2()
        
        imlbp = lbpsimple.lbp2oneslice(data, lbpkern)

        fv = lbpsimple.features(imlbp)

        #pdb.set_trace();
    else:
        print 'Unknow method for feature vetor: ', method
        return -1

    return fv