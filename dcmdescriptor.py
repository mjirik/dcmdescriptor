#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("./src/")
import pdb
#  pdb.set_trace();

import logging
logger = logging.getLogger(__name__)

#import unittest

import argparse

# coputer dependent constant
defaultdatabasedir = '/home/mjirik/data/'
defaultdatatraindir = 'medical/data_orig/jatra-kma/jatra_5mm'
defaultdatatraindir = 'medical/data_orig/51314913'



# TODO vyrobit nevim co
if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.WARNING)

    ch = logging.StreamHandler()
#   output configureation
    #logging.basicConfig(format='%(asctime)s %(message)s')
    logging.basicConfig(format='%(message)s')

    formatter = logging.Formatter("%(levelname)-5s [%(module)s:%(funcName)s:%(lineno)d] %(message)s")
    # add formatter to ch
    ch.setFormatter(formatter)

    logger.addHandler(ch)


    # input parser
    parser = argparse.ArgumentParser(description='Process Dicom file')
    parser.add_argument('-d', '--debug', action='store_true')
    parser.add_argument('-dd', '--datadir', type=str, 
            default = defaultdatabasedir,
            help='Base dir with data')
    parser.add_argument('-tdd', '--trainingdatadir', type=str, 
            default = defaultdatatraindir,
            help='Dir with train data')
    parser.add_argument('-am', '--manualannotation', action='store_true',
            help='Manual data annotation')
    parser.add_argument('-an', '--newannotationfile', action='store_true',
            help='Create new annotation file')
    parser.add_argument('-af', '--annotationfile', type=str,\
            default='./data/annotation.yaml',
            help='Create new annotation file')
    parser.add_argument('-af1', '--annotationfile1', type=str,\
            default='./data/ann1.yaml',
            help='Create new annotation file')
    parser.add_argument('-af2', '--annotationfile2', type=str,\
            default='./data/ann2.yaml',
            help='Create new annotation file')
    parser.add_argument('-asn', '--annotationseriesnumber',type=int, \
            default=None,
            help='Select specific serie from dir')
    parser.add_argument('-ars', '--annotationrandomsplit',type=float, \
            default=None,
            help='Splits annotation into two random annotations')
    parser.add_argument('-as', '--annotationstep', type=int,
            default=3,
            help='Annotation step')
    parser.add_argument('-aw', '--annotationwildcard', type=str,
            default='*.dcm',
            help='Annotation step')
    parser.add_argument('-e', '--experiment', action='store_true',
            help='Annotation step')
    parser.add_argument('-2', '--split', action='store_true',
        help='split image and use only left half')
    parser.add_argument('--outdir', type=str,
        default='',help='output directory')
    args = parser.parse_args()


    if args.debug:
        logger.setLevel(logging.DEBUG)
    logger.debug('input params')
    print args

    

    if args.manualannotation:
        import manualannotation
        manualannotation.manual_annotation_from_dir(\
                args.trainingdatadir, args.datadir, 
                annotationfile = args.annotationfile, 
                newannotationfile = args.newannotationfile,
                step = args.annotationstep,
                wildcard = args.annotationwildcard,
                SeriesNumber = args.annotationseriesnumber
                )

    if args.annotationrandomsplit != None:
        import classif
        classif.annotationRndSplitF(args.annotationfile, part=args.annotationrandomsplit)
    if args.experiment:
        import classif
        classif.experiment(args.annotationfile1, args.annotationfile2, args.datadir)
