from osgeo import gdal
import os

dir = os.getcwd()

# create a list for saving the tif files of a folder
fileToMerge = []

for f in os.listdir(dir):
    if f.endswith('.tif'):
        fileToMerge.append(f)
        

g = gdal.Warp("output.tif", fileToMerge, format="GTiff",
              options=["COMPRESS=LZW", "TILED=YES"]) 
        


