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


#import scipy.io
#mat = scipy.io.loadmat('step0.mat')

#print mat

def filesindir(dirpath, wildcard):
    import os
    import glob

    filelist = []
    print dirpath

    for infile in glob.glob( os.path.join(dirpath, wildcard) ):
        filelist.append(infile)
        print "current file is: " + infile
    return filelist



def traindata(fileslist):
    import dicom

    for filepath in filelist:
        dcmdata=dicom.read_file(filepath)
        print 'Modality: ', dcmdata.Modality
        print 'PatientsName: ' , dcmdata.PatientsName
        print 'BodyPartExamined: ', dcmdata.BodyPartExamined
        print 'SliceThickness: ', dcmdata.SliceThickness
        print 'PixelSpacing: ', dcmdata.PixelSpacing
        # get data
        data = dcmdata.pixel_array
        #print data
        featurevector.fvector(data)

        #import matplotlib.pyplot as plt

        #plt.figure()

        #plt.imshow(data, cmap=plt.cm.gray)
        #plt.show()
        #plt.close()
    

if __name__ == "__main__":
    print 'ahoj'
    filelist = filesindir('/home/mjirik/data/jatra-kiv/jatra-kma/jatra_5mm/','*.*')
    traindata(filelist)

