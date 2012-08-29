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

def rnd_indexes(ln, nind):
    """ Function return random indexes of list with length ln
    rnd_indexes(10,5)

    [1, 3, 4, 8, 9] 
    """
    import random
    rindxs = random.sample(range(0,ln),nind)

    return rindxs




def split_list(restlist, rindxs):
    """ Split list by list of indexes

    a,b = split_list([2, 1, 2, 3, 4, 5], [2,4])
    a = [1, 3]
    b = [2, 2, 4, 5]
    """
    rindxs = sorted(rindxs, reverse=True)
    selectlist = []

    for rind in rindxs:
        selectlist.append(restlist.pop(rind))

    return selectlist, restlist


def traindata(annotation, databasedir):
    import dicom
    import os
    from sklearn import svm
    import random

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

        


    # spilt feature vectors into training and testing group

    #fvs_train = fvs[0:int(len(fvs)*0.75)]
    #fvs_test  = fvs[int(len(fvs)*0.75):]
    #classes_train = classes[0:int(len(fvs)*0.75)]
    #classes_test  = classes[int(len(fvs)*0.75):]


    pdb.set_trace();
    rindxs = rnd_indexes(len(fvs), int(len(fvs)*0.75))
    fvs_train, fvs_test = split_list(fvs, rindxs)
    classes_train, classes_test = split_list(classes, rindxs)

    clf = svm.SVC()
    clf.fit(fvs_train, classes_train)  
    prediction = clf.predict(fvs_test)
    print sum(prediction != classes_test) , ' / ', len(prediction)

#
#dec = clf.decision_function([[1]])
#dec.shape[1]

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

