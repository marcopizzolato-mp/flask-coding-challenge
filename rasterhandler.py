import rasterio
from os.path import exists
from pathlib import Path


def readRaster(file_path):
    ''''''
    if not isinstance(file_path, (str, Path)):
        raise Exception("The path selected is not valid")

    # Check if file exists ans raise and error of not
    if not exists(file_path):
        raise Exception("Sorry, the selected path does not exists")
    # Check if file extension is the desired one
    elif not file_path.lower().endswith(('.tif', '.tiff')):
        raise Exception(
            "Sorry, the file selected is not in .tif format, please provide a .tif of .tiff raster file")
    else:
        # Load raster as a opened dataset object
        rio_object = rasterio.open(file_path)
        # Create a raster object

    return rio_object


def createRaster(rio_object):
    ''''''
    raster_object = Raster(rio_object)
    return raster_object


def dictRaster(raster_object):
    ''''''
    if not isinstance(raster_object, (Raster)):
        raise Exception("The input is not an instance of hte Class Raster")

    dict_metadata = {}

    dict_metadata['crs'] = str(raster_object.getCRS)
    dict_metadata['width'] = str(raster_object.getWidth)
    dict_metadata['height'] = str(raster_object.getHeight)
    dict_metadata['band'] = str(raster_object.getCount)
    dict_metadata['bounds'] = str(raster_object.getBounds)
    dict_metadata['driver'] = str(raster_object.getDriver)
    return dict_metadata


class Raster(object):
    '''A class to represent 2-D Rasters'''
# Basic constructor method

    def __init__(self, opened_object):
        self._array = opened_object.read(1)
        self._crs = opened_object.crs
        self._width = opened_object.width
        self._height = opened_object.height
        self._count = opened_object.count
        self._bounds = opened_object.bounds
        self._driver = opened_object.driver
        self._meta = opened_object.meta

    @property
    def getArray(self):
        return self._array

    @property
    def getCRS(self):
        if self._crs == None:
            crs_out = "CRS not available or not set"
        else:
            crs_out = self._crs
        return crs_out

    @property
    def getWidth(self):
        return self._width

    @property
    def getHeight(self):
        return self._height

    @property
    def getCount(self):
        return self._count

    @property
    def getBounds(self):
        return self._bounds

    @property
    def getDriver(self):
        return self._driver

    @property
    def getMetadata(self):
        return self._meta
