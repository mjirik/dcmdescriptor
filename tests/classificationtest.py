#! /usr/bin/python
# -*- coding: utf-8 -*-



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
