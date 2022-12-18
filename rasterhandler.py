import rasterio
from os.path import exists
from pathlib import Path


def read_raster(file_path):
    """Takes as input a file path to a geoTif image, opens it using Rasterio and returns a Raster object
    Args:
    file_path (Path): path to the geoTif image
    Raises:
        Exception: raise an error if the parameter is not a Path
        Exception: raise an error if the file does not exists
        Exception: raise an error if the file extension is not correct
    Returns:
        raster_object (Raster): object of the Class Raster
     """
    
    # Raise an error if the parameter is not a Path
    if not isinstance(file_path, (str, Path)):
        raise Exception("Sorry, the path selected is not valid")
    # Raise an error if the file does not exist
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


def raster_metadata(raster_object):
    """Takes as input an object of the Class Raster and returns a dictionary with the Raster metadata
    Args:
    raster_object (Raster): object of the Class Raster
    Raises:
        Exception: raise an error if the parameter is not of the Class Raster
    Returns:
        dict_metadata (dict): dictionary object
     """

    if not isinstance(raster_object, Raster):
        raise Exception(
            "Sorry, the input is not an instance of the Class Raster")
    raster_array = raster_object.get_array
    dict_metadata = {'band': str(raster_object.get_count), 'width': str(raster_object.get_width),
                     'height': str(raster_object.get_height), 'crs': str(raster_object.get_crs),
                     'bounds': str(raster_object.get_bounds), 'driver': str(raster_object.get_driver),
                     'min': str(round(raster_array.min(), 2)), 'max': str(round(raster_array.max(), 2)),
                     'mean': str(round(raster_array.mean(), 2)), 'std': str(round(raster_array.std(), 2))}

    return dict_metadata


class Raster(object):
    """Creates a Raster object
    Args:
    opened_object (rasterio.io.DatasetReader): opened dataset object
     """

    def __init__(self, opened_object):
        self._array = opened_object.read(1)
        self._crs = str(opened_object.crs)
        self._width = str(opened_object.width)
        self._height = str(opened_object.height)
        self._count = str(opened_object.count)
        self._bounds = str(opened_object.bounds)
        self._driver = opened_object.driver

    @property
    def get_array(self):
        return self._array

    @property
    def get_crs(self):
        if self._crs == None:
            string_out = "not set or not available"
        else:
            string_out = self._crs
        return string_out

    @property
    def get_width(self):
        if self._width == None:
            string_out = "not set or not available"
        else:
            string_out = self._width
        return string_out

    @property
    def get_height(self):
        if self._height == None:
            string_out = "not set or not available"
        else:
            string_out = self._height
        return string_out

    @property
    def get_count(self):
        if self._count == None:
            string_out = "not set or not available"
        else:
            string_out = self._count
        return string_out

    @property
    def get_bounds(self):
        if self._bounds == None:
            string_out = "not set or not available"
        else:
            string_out = self._bounds
        return string_out

    @property
    def get_driver(self):
        if self._driver == None:
            string_out = "not set or not available"
        else:
            string_out = self._driver
        return string_out
