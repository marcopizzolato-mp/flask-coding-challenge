from typing import Dict
from rasterhandler import Raster, readRaster, dictRaster
import numpy as np
import os

RASTER_FILE_PATH = os.path.join('data','test_data', 'sample.tif')


def test_readRaster_is_raster():
    '''Test the readRaster function ensuring it returns a raster object'''
    raster_object = readRaster(RASTER_FILE_PATH)
    assert(isinstance(raster_object, Raster) == True)


def test_dictRaster_is_dictionary():
    '''Test the dictRaster function ensuring it returns a dictionary object'''
    raster_object = readRaster(RASTER_FILE_PATH)
    dict_metadata = dictRaster(raster_object)
    assert(isinstance(dict_metadata, dict) == True)


def test_Raster_array_is_array():
    '''Test the array attribute of the raster is an array'''
    raster_object = readRaster(RASTER_FILE_PATH)
    assert(isinstance(raster_object.getArray, np.ndarray) == True)


def test_Raster_crs_is_str():
    '''Test the array attribute of the raster is a string'''
    raster_object = readRaster(RASTER_FILE_PATH)
    assert(isinstance(raster_object.getCRS, str) == True)


def test_Raster_bounds_is_str():
    '''Test the array attribute of the raster is a string'''
    raster_object = readRaster(RASTER_FILE_PATH)
    assert(isinstance(raster_object.getBounds, str) == True)


def test_Raster_count_is_str():
    '''Test the array attribute of the raster is a string'''
    raster_object = readRaster(RASTER_FILE_PATH)
    assert(isinstance(raster_object.getCount, str) == True)


def test_Raster_driver_is_str():
    '''Test the array attribute of the raster is a string'''
    raster_object = readRaster(RASTER_FILE_PATH)
    assert(isinstance(raster_object.getDriver, str) == True)


def test_Raster_height_is_str():
    '''Test the array attribute of the raster is a string'''
    raster_object = readRaster(RASTER_FILE_PATH)
    assert(isinstance(raster_object.getHeight, str) == True)


def test_Raster_width_is_str():
    '''Test the array attribute of the raster is a string'''
    raster_object = readRaster(RASTER_FILE_PATH)
    assert(isinstance(raster_object.getWidth, str) == True)
