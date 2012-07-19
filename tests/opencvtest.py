#! /usr/bin/python
# -*- coding: utf-8 -*-


import cv #Import functions from OpenCV

cv.NamedWindow('a_window', cv.CV_WINDOW_AUTOSIZE)
image=cv.LoadImage('../sampledata/image.png', cv.CV_LOAD_IMAGE_COLOR) #Load the image
font = cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 3, 8) #Creates a font
x = 5 #x position of text
y = 20 #y position of text
cv.PutText(image,"Hello World!!!", (x,y),font, 255) #Draw the text
cv.ShowImage('a_window', image) #Show the image
#cv.Waitkey(10000)
cv.SaveImage('imageo.png', image) #Saves the image
