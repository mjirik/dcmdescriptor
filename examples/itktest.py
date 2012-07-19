#! /usr/bin/python
# -*- coding: utf-8 -*-



import itk


# typedef
image_type = itk.Image[itk.UC, 3]




# Reading file
print 'Reading file'

file_name = '/usr/share/doc/insighttoolkit-examples/examples/Data/BrainProtonDensity3Slices.mha'
#file_name = './iiBrainProtonDensity3Slices.mha'
file_name = './BrainProtonDensitySlice256x256.png'

reader = itk.ImageFileReader[image_type].New()
reader.SetFileName( file_name )
reader.Update()


# Processing

print 'Processing'

median_filter = itk.MedianImageFilter[image_type, image_type].New()
        
median_filter.SetRadius( 1 )


median_filter.SetInput( reader.GetOutput() )
median_filter.Update()

# VTK test 
print 'VTK Test'
import vtk
s = vtk.vtkSphereSource()
m = vtk.vtkPolyDataMapper()
m.SetInput(s.GetOutput())

a = vtk.vtkActor()
a.SetMapper(m)

ren = vtk.vtkRenderer()
rw = vtk.vtkRenderWindow()
rw.AddRenderer(ren)

ren.AddActor(a)

print 'iren'
#iren = vtk.RenderWindowInteractor()
iren = vtk.vtkRenderWindowInteractor()
print 'iren'
iren.SetRenderWindow(rw)
print 'iren Start'
iren.Start()


# ITK to numpy
itk_py_converter = itk.PyBuffer[image_type]
image_array = itk_py_converter.GetArrayFromImage( reader.GetOutput() )

import scipy
another_image_array = scipy.zeros( (10,10,10) )
itk_image = itk_py_converter.GetImageFromArray( another_image_array.tolist() )

# ITK VTK
print 'ITK VTK'

itk_vtk_converter = itk.ImageToVTKImageFilter[image_type].New()
itk_vtk_converter.SetInput( median_filter.GetOutput() )
itk_vtk_converter.Update()



# Volume Rendering VTK
print 'Volume Rendering'
import vtk

volume_mapper = vtk.vtkVolumeRayCastMapper()
volume_mapper.SetInput( itk_vtk_converter.GetOutput() )

composite_function = vtk.vtkVolumeRayCastCompositeFunction()
volume_mapper.SetVolumeRayCastFunction( composite_function )

color_transfer_func = vtk.vtkColorTransferFunction()
color_transfer_func.AddRGBPoint( 0, 0.0, 0.0, 0.0 )
color_transfer_func.AddRGBPoint( 255, 0.0, 0.0, 1.0 )

opacity_transfer_func = vtk.vtkPiecewiseFunction()
opacity_transfer_func.AddPoint( 0, 0.0 )
opacity_transfer_func.AddPoint( 255, 1.0 )



volume_properties = vtk.vtkVolumeProperty()
volume_properties.SetColor( color_transfer_func )
volume_properties.SetScalarOpacity( opacity_transfer_func )



volume = vtk.vtkVolume()
volume.SetMapper( volume_mapper )
volume.SetProperty( volume_properties )



renderer = vtk.vtkRenderer()
render_window = vtk.vtkRenderWindow()
window_interactor = vtk.vtkRenderWindowInteractor()



render_window.AddRenderer( renderer )
window_interactor.SetRenderWindow( render_window )
renderer.AddVolume( volume )





render_window.Render()
window_interactor.Start()


# Numpy and ITK




