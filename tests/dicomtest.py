#! /usr/bin/python
# -*- coding: utf-8 -*-

import dicom

plan=dicom.read_file("../sampledata/IM-0001-0060.dcm")
print 'Modality: ', plan.Modality
print 'PatientsName: ' , plan.PatientsName
print 'BodyPartExamined: ', plan.BodyPartExamined
print 'SliceThickness: ', plan.SliceThickness
print 'PixelSpacing: ', plan.PixelSpacing


# get data
data = plan.pixel_array
print data

import matplotlib.pyplot as plt

plt.figure()

plt.imshow(data, cmap=plt.cm.gray)
plt.show()
plt.close()
