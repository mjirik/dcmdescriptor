#! /usr/bin/ipython
# -*- coding: utf-8 -*-

import pdb; 
#  pdb.set_trace();

import logging
logger = logging.getLogger(__name__)

import argparse

# coputer dependent constant
defaultdatabasedir = '/home/mjirik/data/'
defaultdatatraindir = 'medical/data_orig/jatra-kma/jatra_5mm'


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s')
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    logger.addHandler(ch)


    # input parser
    parser = argparse.ArgumentParser(description='Process Dicom file')
    parser.add_argument('-d', '--debug', action='store_true')
    parser.add_argument('-m', '--manualannotation', action='store_true',
            help='Manual data annotation')
    parser.add_argument('-dd', '--datadir', type=str, 
            default = defaultdatabasedir,
            help='Base dir with data')
    parser.add_argument('-tdd', '--trainingdatadir', type=str, 
            default = defaultdatabasedir,
            help='Dir with train data')
    parser.add_argument('-na', '--newannotation', action='store_true',
            help='Create new annotation file')
    parser.add_argument('-dd', '--datadir', type=str, 
            default = defaultdatabasedir,
            help='Base dir with data')
    parser.add_argument('-2', '--split', action='store_true',
        help='split image and use only left half')
    parser.add_argument('--outdir', type=str,
        default='',help='output directory')
    args = parser.parse_args()

    logger.debug('input params')
    print args

