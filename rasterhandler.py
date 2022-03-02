import rasterio
from os.path import exists
from pathlib import Path


def readRaster(file_path):
    '''Takes as input a file path to a geoTif image, opens it using Rasterio and returns a Raster object

    Args: 
    file_path (Path): path to the geoTif image

    Raises: 
        Exception: raise an error if the parameter is not a Path
        Exception: raise an error if the file does not exists
        Exception: raise an error if the file extension is not correct

    Returns: 
        raster_object (Raster): object of the Class Raster
     '''
    # Raise an error if the parameter is not a Path
    if not isinstance(file_path, (str, Path)):
        raise Exception("Sorry, the path selected is not valid")
    # Raise an error if the file does not exists
    if not exists(file_path):
        raise Exception("Sorry, the selected path does not exists")
    # Raise an error if the file extension is not correct
    elif not file_path.lower().endswith(('.tif', '.tiff')):
        raise Exception(
            "Sorry, the file selected is not in .tif format, please provide a .tif of .tiff raster file")
    else:
        # Load raster as a opened dataset object
        rio_object = rasterio.open(file_path)
        # Create a raster object
        raster_object = Raster(rio_object)

    return raster_object


def dictRaster(raster_object):
    '''Takes as input an object of the Class Raster and returns a dictionary with the Raster metadata

    Args: 
    raster_object (Raster): object of the Class Raster

    Raises: 
        Exception: raise an error if the parameter is not of the Class Raster

    Returns: 
        dict_metadata (dict): dictionary object
     '''
    if not isinstance(raster_object, (Raster)):
        raise Exception(
            "Sorry, the input is not an instance of the Class Raster")
    raster_array = raster_object.getArray
    dict_metadata = {
        'band': '',
        'width': '',
        'height': '',
        'crs': '',
        'bounds': '',
        'driver': '',
        'min': '',
        'max': '',
        'mean': '',
        'std': ''}
    dict_metadata['crs'] = str(raster_object.getCRS)
    dict_metadata['width'] = str(raster_object.getWidth)
    dict_metadata['height'] = str(raster_object.getHeight)
    dict_metadata['band'] = str(raster_object.getCount)
    dict_metadata['bounds'] = str(raster_object.getBounds)
    dict_metadata['driver'] = str(raster_object.getDriver)
    dict_metadata['min'] = str(round(raster_array.min(), 2))
    dict_metadata['max'] = str(round(raster_array.max(), 2))
    dict_metadata['mean'] = str(round(raster_array.mean(), 2))
    dict_metadata['std'] = str(round(raster_array.std(), 2))

    return dict_metadata


class Raster(object):
    '''Creates a Raster object

    Args: 
    opened_object (rasterio.io.DatasetReader): opened dataset object
     '''

    def __init__(self, opened_object):
        self._array = opened_object.read(1)
        self._crs = str(opened_object.crs)
        self._width = str(opened_object.width)
        self._height = str(opened_object.height)
        self._count = str(opened_object.count)
        self._bounds = str(opened_object.bounds)
        self._driver = opened_object.driver

    @ property
    def getArray(self):
        return self._array

    @ property
    def getCRS(self):
        if self._crs == None:
            string_out = "not set or not available"
        else:
            string_out = self._crs
        return string_out

    @ property
    def getWidth(self):
        if self._width == None:
            string_out = "not set or not available"
        else:
            string_out = self._width
        return string_out

    @ property
    def getHeight(self):
        if self._height == None:
            string_out = "not set or not available"
        else:
            string_out = self._height
        return string_out

    @ property
    def getCount(self):
        if self._count == None:
            string_out = "not set or not available"
        else:
            string_out = self._count
        return string_out

    @ property
    def getBounds(self):
        if self._bounds == None:
            string_out = "not set or not available"
        else:
            string_out = self._bounds
        return string_out

    @ property
    def getDriver(self):
        if self._driver == None:
            string_out = "not set or not available"
        else:
            string_out = self._driver
        return string_out
