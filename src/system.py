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
#sys.path.append("../src/")
import featurevector

import logging
logger = logging.getLogger(__name__)

#import scipy.io
#mat = scipy.io.loadmat('step0.mat')

#print mat




def filesindir(dirpath, wildcard="*.*", startpath=None):
    """ Function generates list of files from specific dir

    filesindir(dirpath, wildcard="*.*", startpath=None)

    dirpath: required directory
    wilcard: mask for files
    startpath: start for relative path

    Example
    filesindir('medical/jatra-kiv','*.dcm', '/home/mjirik/data/')


    """
    import os
    import glob


    filelist = []
    #print dirpath

    if startpath != None:
        completedirpath = os.path.join( startpath, dirpath)
    else:
        completedirpath = dirpath

    if os.path.exists(completedirpath):
        logger.info('completedirpath = '  + completedirpath )
    else:
        logger.error('Wrong path: '  + completedirpath )
    print 'copmpletedirpath = ', completedirpath
    for infile in glob.glob( os.path.join(completedirpath, wildcard) ):
        filelist.append(infile)
        #print "current file is: " + infile
    return filelist



if __name__ == "__main__":

    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    logger.addHandler(ch)

    logger.debug('input params')
    for arg in sys.argv:
        logger.debug(''+arg)

    databasedir = '/home/mjirik/data'
    if len(sys.argv) < 1:
        datatraindir = '/home/mjirik/data/jatra_06mm_jenjatra'
    else:
        datatraindir = sys.argv[1]

    logger.debug('Adresar ' + datatraindir)
    #dm = Dialogmenu()
    #print dm.retval

