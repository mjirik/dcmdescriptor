#! /usr/bin/ipython
# -*- coding: utf-8 -*-

import pdb; 
#  pdb.set_trace();

import logging
logger = logging.getLogger(__name__)

import argparse

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s')
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    logger.addHandler(ch)

    logger.debug('input params')

