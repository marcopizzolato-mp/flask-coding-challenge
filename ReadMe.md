## Serving geospatial metadata

![S2 image](asset.png)

In this scenario, we have a client who isn't experienced with geospatial data, but understands some basic concepts, such as resolution of imagery.

As a PoC, we are tasked with demonstrating a simple way of interacting with a remotely sensed image - in this case a single image in data/sample.tif.

The product owner has requested two explicit endpoints be developed for the customer to interact with this asset:

1. Display an in-browser thumbnail when at the /thumbnail address
2. Retrieve relevant metadata (resolution, coordinate system, bounding box, statistics) about the asset at the /metadata address

Our team has identified flask as a good start for this PoC, but also considered FastAPI and/or Starlette as possible frameworks to implement the functionality, should you wish to choose one of those.

The scope of this work is limited to the single asset within this project, but should and could be generalizable to any asset available through a http connection.
