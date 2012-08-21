#! /usr/bin/ipython
# -*- coding: utf-8 -*-


#
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

# import funkcí z jiného adresáře
import sys
sys.path.append("../src/")
import featurevector

import pdb; 
#  pdb.set_trace();

#import scipy.io
#mat = scipy.io.loadmat('step0.mat')

#print mat


#X = [[0, 0], [1, 1],[0,4],[0.1, 0.2]]
#Y = [0, 1, 2 , 0]
#print clf.predict([[2,3]])
#
#dec = clf.decision_function([[1]])
#dec.shape[1]


def traindata(annotation, databasedir):
    import dicom
    import os
    from sklearn import svm

    fvs=[]
    classes=[]

    for itm in annotation['data'].itervalues():
        #pdb.set_trace();
        filepath = os.path.join(databasedir, itm['filepath'])

        dcmdata=dicom.read_file(filepath)
        print 'Modality: ', dcmdata.Modality
        print 'PatientsName: ' , dcmdata.PatientsName
        print 'BodyPartExamined: ', dcmdata.BodyPartExamined
        print 'SliceThickness: ', dcmdata.SliceThickness
        print 'PixelSpacing: ', dcmdata.PixelSpacing
        # get data
        data = dcmdata.pixel_array
        #print data
        #fvs[itm['filepath']] = 
        # fv: lbp hist , fvbins possible bins in histogram
        fv,fvbins = featurevector.fvector(data)
        fvs.append(fv)
        classes.append(itm['sliceclass'])

        
    clf = svm.SVC()
    clf.fit(fvs, classes)  
    pdb.set_trace();

        #import matplotlib.pyplot as plt

        #plt.figure()

        #plt.imshow(data, cmap=plt.cm.gray)
        #plt.show()
        #plt.close()
    

if __name__ == "__main__":
    import system
    print 'ahoj'
    annotation = system.annotation_from_file('annotation.yaml')
    #filelist = filesindir('/home/mjirik/data/jatra-kiv/jatra-kma/jatra_5mm/','*.*')

    traindata(annotation,'/home/mjirik/data/')

