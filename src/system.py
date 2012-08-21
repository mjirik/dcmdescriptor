#! /usr/bin/ipython
# -*- coding: utf-8 -*-



# import funkcí z jiného adresáře
import sys
#sys.path.append("../src/")
#import featurevector

import logging
logger = logging.getLogger(__name__)

#import scipy.io
#mat = scipy.io.loadmat('step0.mat')

#print mat


def annotation_from_file(filename = 'annotation.yaml'):
    import yaml
    f = open(filename, 'r')
    yml = yaml.load(f)
    f.close()
    return yml

def annotation_to_file(annotation, filename = 'annotation.yaml'):
    '''Writes annotation in file
    '''
    #import json
    #with open(filename, mode='w') as f:
    #    json.dump(annotation,f)

    # write to yaml

    import yaml
    f = open(filename, 'w')
    yaml.dump(annotation,f)
    f.close

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

