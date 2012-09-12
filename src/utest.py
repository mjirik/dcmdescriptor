#! /usr/bin/ipython
# -*- coding: utf-8 -*-
import sys
sys.path.append("./../src/")
sys.path.append("./")
import unittest

class TestSequenceFunctions(unittest.TestCase):
    def test_xxx(self):
        #assert(1 == 2)
        pass

    def test_classif_Clf(self):
        ''' Classifer test'''
        import classif

        clf = classif.Clf()
        clf.ClfTrain([[2],[5],[9],[4]],[0,1,2,1])
        prediction2 = clf.ClfPredict([[2],[4],[8]])
        sumErr = sum (prediction2 != [0 , 1 , 2])
        assert (sumErr == 0)

if __name__ == '__main__':
    unittest.main()
