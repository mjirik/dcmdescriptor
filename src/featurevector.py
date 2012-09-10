#! /usr/bin/python
# -*- coding: utf-8 -*-

#debug
import lbpsimple
import pdb; 
#  pdb.set_trace();

#from sklearn import svm
#X = [[0, 0], [1, 1],[0,4],[0.1, 0.2]]
#Y = [0, 1, 2 , 0]
#clf = svm.SVC()
#clf.fit(X, Y)  
#print clf.predict([[2,3]])
#
#dec = clf.decision_function([[1]])
#dec.shape[1]
#
#import scipy.io
#mat = scipy.io.loadmat('step0.mat')

#print mat



def fvector(data, method ):
    """ Method for building feature vector """

    fv = 0
    if method['type'] == 'lbp':
        

        lbpkern = lbpsimple.generateKernel2()
        
        imlbp = lbpsimple.lbp2oneslice(data, lbpkern)

        fv,bins = lbpsimple.features(imlbp)

        #pdb.set_trace();
    else:
        raise Exception('Unknow method for feature vector: %s' %(method))

    return fv
