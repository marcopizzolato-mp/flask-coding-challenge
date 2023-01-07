import os

import numpy as np

from rasterhandler import Raster, read_raster, raster_metadata

RASTER_FILE_PATH = os.path.join('data', 'test_data', 'sample.tif')


def test_readraster_is_raster():
    """Test the read_raster function ensuring it returns a raster object"""
    raster_object = read_raster(RASTER_FILE_PATH)
    assert (isinstance(raster_object, Raster) == True)


def test_rastermetadata_is_dictionary():
    """Test the raster_metadata function ensuring it returns a dictionary object"""
    raster_object = read_raster(RASTER_FILE_PATH)
    dict_metadata = raster_metadata(raster_object)
    assert (isinstance(dict_metadata, dict) == True)


def test_raster_array_is_array():
    """Test the array attribute of the raster is an array"""
    raster_object = read_raster(RASTER_FILE_PATH)
    assert (isinstance(raster_object.get_array, np.ndarray) == True)


def test_raster_crs_is_str():
    """Test the crs attribute of the raster is a string"""
    raster_object = read_raster(RASTER_FILE_PATH)
    assert (isinstance(raster_object.get_crs, str) == True)


def test_raster_bounds_is_str():
    """Test the boundaries attribute of the raster is a string"""
    raster_object = read_raster(RASTER_FILE_PATH)
    assert (isinstance(raster_object.get_bounds, str) == True)


def test_raster_count_is_str():
    """Test the cell count attribute of the raster is a string"""
    raster_object = read_raster(RASTER_FILE_PATH)
    assert (isinstance(raster_object.get_count, str) == True)


def test_raster_driver_is_str():
    """Test the driver attribute of the raster is a string"""
    raster_object = read_raster(RASTER_FILE_PATH)
    assert (isinstance(raster_object.get_driver, str) == True)


def test_raster_height_is_str():
    """Test the height attribute of the raster is a string"""
    raster_object = read_raster(RASTER_FILE_PATH)
    assert (isinstance(raster_object.get_height, str) == True)


def test_raster_width_is_str():
    """Test the width attribute of the raster is a string"""
    raster_object = read_raster(RASTER_FILE_PATH)
    assert (isinstance(raster_object.get_width, str) == True)
