import matplotlib.pyplot as plt
import base64
from io import BytesIO
from flask import Flask
from flask import render_template, request, redirect, url_for, abort, session
from werkzeug.utils import secure_filename
from rasterhandler import readRaster, dictRaster, createRaster
import datetime
import re
import os
import secrets
import numpy as np
import matplotlib
matplotlib.use('Agg')

app = Flask(__name__)

# Validation parameters
app.config['UPLOAD_EXTENSIONS'] = ['.tiff', '.tif']
app.config['UPLOAD_PATH'] = 'data'

# Set a secret key for the session
secret = secrets.token_urlsafe(32)
app.secret_key = secret


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        raster_file_path = os.path.join(app.config['UPLOAD_PATH'], filename)
        # Check if a file with the same name exists on disk
        if os.path.exists(raster_file_path):
            try:
                os.remove(raster_file_path)
                uploaded_file.save(raster_file_path)
                print("here")
            except:
                print("There are some problem removing and saving the file from disk")
        else:
            uploaded_file.save(raster_file_path)
        rio_object = readRaster(raster_file_path)
        raster_object = createRaster(rio_object)
        dict_metadata = dictRaster(raster_object)
        session.clear()
        session['metadata'] = dict_metadata
        session['filename'] = filename
        session['filepath'] = raster_file_path
    return redirect(url_for('index_upload'))


@app.route("/upload")
def index_upload():
    filename = session.get('filename', None)
    return render_template("index_upload.html", file=filename)


@app.route("/thumbnail")
def thumbnail():
    img = BytesIO()
    raster_file_path = session.get('filepath', None)
    rio_object = readRaster(raster_file_path)
    array_r = rio_object.read(1)
    plt.imshow(array_r)
    # Add Title
    plt.title("Matplotlib PLot NumPy Array")
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    temp_path = b''.join(img)
    plot_url = base64.b64encode(temp_path).decode('utf8')
    return render_template(
        'thumbnail.html',
        plot_url=plot_url)


@app.route("/metadata")
def metadata():
    metadata = session.get('metadata', None)
    return render_template(
        'metadata.html',
        metadata=metadata
    )
