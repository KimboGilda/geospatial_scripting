## Clipping a Raster dataset using a vector dataset as a clipper

from osgeo import gdal
import numpy
import os

# defining the clipper shape
clipper = r"/Users/nikosbakogiannis/Downloads/clipper.shp"

dir = os.getcwd()
for f in  os.listdir(dir):
    if f.endswith('.tif'): # check the type of the files in the folder
        # defining the output
        rout = 'clipped' + f 
        print("Starting clipping...",f)
        
        # calling the gdal function
        gdal.Warp(rout,f, cutlineDSName = clipper)
        
    else:
        print("Nothing to clip here...")
        
        
        
    
