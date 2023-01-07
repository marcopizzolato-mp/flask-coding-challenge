# <img src=".\static\images\logo_terra_transp.png" alt="logo_terra" width="360"/> <br> Raster exploration with Python and Flask

## Project Description

The aim of this project and the **Bird's Eye Viewer** web app, built using **Python** and **Flask**, is to create an
interactive tool that allows users to explore remotely sensed (raster) images with few simple clicks, without the need
of using specific GIS software.  
This tool is intended for both users that do not have a remote sensing background but also for experienced geospatial
ones, that need a quick overview of raster properties.

## Installation

This project is not available live through the internet, but can be easily run locally, creating a virtual python
environment. The _requirements.txt_ file contains information on the necessary libraries to run the Web App.

### Libraries

<br>

> flask~=2.2.2  
> matplotlib~=3.6.2  
> numpy~=1.23.5  
> Werkzeug~=2.2.2  
> rasterio~=1.3.4

<br>

## Web App user interface

For a detailed description on how to use the **Bird's Eye Viewer** web app as well as more information on the code
structure and testing, please refer to the following the [dedicated article](https://www.marcopizzolato.com/posts/python-flask/) in my personal [Portfolio website](https://www.marcopizzolato.com/).

## Limitations

In this current version (v1.0), the tool can only analyse single band rasters in .tif format. Future version will expand
the tool to take as inputs raster different from .tif and with multiple bands, such as netCDF. 









