#! /usr/bin/ipython
# -*- coding: utf-8 -*-


#
import os
import dicom
from sklearn import svm
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




class Clf:
# pointer to classificator init function
    ClfInit = None 
# pointer to flassificatr
    ClfTrain = None
    ClfPredict = None
    ClfFeatVec = None

    def __init__(self):
        print 'Clf init'
        self.ClfInit = svm.SVC()
        self.ClfTrain = self.ClfInit.fit
        self.ClfPredict = self.ClfInit.predict
        self.ClfFeatVec = 1

    #def train(featurevector, classes)

    def save(self):
        import system
        var = [self.ClfInit, self.ClfTrain, self.ClfPredict ]
        system.obj_to_file(var,'Clf.pickle','pickle')
    def load(self):
        var = system.obj_from_file('Clf.pickle','pickle')
        self.ClfInit = var[0]
        self.ClfTrain = var [1]
        self.ClfPredict = var[2]



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


def annotation2filelist (annotation, databasedir):

    classes=[]

    filelist = []
    for itm in annotation['data'].itervalues():
        #pdb.set_trace();
        filepath = os.path.join(databasedir, itm['filepath'])

        filelist.append(filepath)

        classes.append(itm['sliceclass'])
    return filelist, classes

def annotationRndSplitF(annotationfile,  part = 0.5, 
        annotationfile1 = 'ann1.yaml', annotationfile2 = 'ann2.yaml'):
    import system
    annotation = system.obj_from_file(annotationfile)
    ann1, ann2 = annotationRndSplit(annotation,  part)
    system.obj_to_file(ann1, annotationfile1)
    system.obj_to_file(ann2, annotationfile2)
    #pdb.set_trace();


def annotationRndSplit(annotation,  part=0.5, rndseed = 0):
    import copy
    import random
    annotation2 = copy.copy(annotation)
    itms = annotation['data'].items()

    #rindxs = rnd_indexes(len(itms), int(len(itms)*0.75))
    #list1, list2 = split_list(itms, rindxs)

    random.seed(rndseed)
    random.shuffle(itms)

    spl = int(len(itms)*part)
    list1 = itms[0:spl]
    list2 = itms[spl:]

    annotation2['data'] = {}
    ann1d= {}
    for itm in list1:
        ann1d[itm[0]]=itm[1]
    
    annotation['data'] = ann1d
    

    ann2d= {}
    for itm in list2:
        ann2d[itm[0]]=itm[1]
    
    annotation2['data'] = ann2d

    #annotation['data'] = list1
    #annotation['data'] = list1
    return annotation, annotation2


def experiment(ann1file, ann2file, databasedir, features={'type':'lbp','p1': [1, 2] }, classif=['svm']):
    import system

    #clf = Clf()
    #clf.ClfInit()
    #clf.ClfTrain([[1],[5],[9],[4]],[0,1,2,1])
    #prediction2 = clf.ClfPredict([2,4,8])


    ann1 = system.obj_from_file(ann1file)
    ann2 = system.obj_from_file(ann2file)

    fl1, cls1 = annotation2filelist(ann1,databasedir)
    fl2, cls2 = annotation2filelist(ann2, databasedir)

    fv1 = filelist2featurevector(fl1, features)
    pdb.set_trace();
    clf = Clf()
    #clf.ClfInit()
    clf.ClfTrain(fv1, cls1)

    fv2 = filelist2featurevector(fl2, features)
    prediction2 = clf.ClfPredict(fv2)


    print sum(prediction2 != cls2) , ' / ', len(prediction2)

#TODO dokončit experiment



def filelist2featurevector(filelist,fvparam):
    fvs=[]
    for filepath in filelist:
        dcmdata=dicom.read_file(filepath)
        #print 'Modality: ', dcmdata.Modality
        #print 'PatientsName: ' , dcmdata.PatientsName
        #print 'BodyPartExamined: ', dcmdata.BodyPartExamined
        #print 'SliceThickness: ', dcmdata.SliceThickness
        #print 'PixelSpacing: ', dcmdata.PixelSpacing
        # get data
        data = dcmdata.pixel_array
        #print data
        #fvs[itm['filepath']] = 
        # fv: lbp hist , fvbins possible bins in histogram
        fv = featurevector.fvector(data, fvparam)
        fvs.append(fv)

    return fvs

        


    # spilt feature vectors into training and testing group

    #fvs_train = fvs[0:int(len(fvs)*0.75)]
    #fvs_test  = fvs[int(len(fvs)*0.75):]
    #classes_train = classes[0:int(len(fvs)*0.75)]
    #classes_test  = classes[int(len(fvs)*0.75):]




def traindata(annotation, databasedir):
    from sklearn import svm

    #pdb.set_trace();
    filelist, classes =  annotation2filelist(annotation, databasedir)
    rindxs = rnd_indexes(len(filelist), int(len(filelist)*0.75))
    filelist_train, filelist_test = split_list(filelist, rindxs)
    cls_train, cls_test = split_list(classes, rindxs)




    mclf = Clf()

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
    annotation = system.obj_from_file('annotation.yaml')

    #filelist = filesindir('/home/mjirik/data/jatra-kiv/jatra-kma/jatra_5mm/','*.*')

    traindata(annotation,'/home/mjirik/data/')

