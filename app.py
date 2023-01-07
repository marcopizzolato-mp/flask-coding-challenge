import base64
import os
import secrets
from io import BytesIO

import matplotlib
import matplotlib.pyplot as plt
from flask import Flask
from flask import render_template, request, redirect, url_for, abort, session
from werkzeug.utils import secure_filename

from rasterhandler import read_raster, raster_metadata

matplotlib.use('Agg')

app = Flask(__name__)

# Parameters
app.config['UPLOAD_EXTENSIONS'] = ['.tiff', '.tif']
app.config['UPLOAD_PATH'] = 'data'
app.config['IMAGE_PATH'] = os.path.join('static', 'images', 'logo_terra_transp.png')
app.config['FOOTER_TEXT'] = "Bird's eye viewer v1.0 - Marco Pizzolato 2022"

# Set a secret key for the session
secret = secrets.token_urlsafe(32)
app.secret_key = secret


@app.route("/")
def index():
    """Homepage - initial page"""
    # Retrieve parameters
    image = app.config['IMAGE_PATH']
    text = app.config['FOOTER_TEXT']
    # Render
    return render_template("index.html",
                           logo_image=image,
                           footer_text=text)


@app.route('/', methods=['POST'])
def upload_file():
    """Homepage - POST method to receive a file from the browser"""
    # Get input image
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    # Handle uploaded file
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        raster_file_path = os.path.join(app.config['UPLOAD_PATH'], filename)
        # Save on disk
        if os.path.exists(raster_file_path):
            try:
                os.remove(raster_file_path)
                uploaded_file.save(raster_file_path)
            except:
                print(
                    "Sorry. there are some problem removing and saving the file from disk")
        else:
            uploaded_file.save(raster_file_path)
        # Execute raster functions
        file_bytes = os.path.getsize(raster_file_path)
        raster_object = read_raster(raster_file_path)
        dict_metadata = raster_metadata(raster_object)

        session.clear()
        # Set variables
        session['filesize'] = str(round(file_bytes / (1024 * 1024), 3))
        session['metadata'] = dict_metadata
        session['filename'] = filename
        session['filepath'] = raster_file_path
        # Redirect
    return redirect(url_for('index_upload'))


@app.route("/upload")
def index_upload():
    """Page with information on the uploaded file"""
    # Retrieve variables
    filename = session.get('filename', None)
    size_mb = session.get('filesize', None)
    image = app.config['IMAGE_PATH']
    text = app.config['FOOTER_TEXT']
    # Render
    return render_template("index_upload.html",
                           logo_image=image,
                           file=filename,
                           size_mb=size_mb,
                           footer_text=text)


@app.route("/thumbnail")
def thumbnail():
    """Page with thumbnail image of the uploaded file"""
    # Retrieve variables
    raster_file_path = session.get('filepath', None)
    # Execute function
    raster_object = read_raster(raster_file_path)
    array_r = raster_object.get_array
    # Create plot
    img = BytesIO()
    plt.imshow(array_r)
    plt.title("Raster Thumbnail Plot")
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    temp_path = b''.join(img)
    plot_url = base64.b64encode(temp_path).decode('utf8')
    # Retrieve variables
    image = app.config['IMAGE_PATH']
    text = app.config['FOOTER_TEXT']
    # Render
    return render_template(
        'thumbnail.html',
        logo_image=image,
        plot_url=plot_url,
        footer_text=text)


@app.route("/metadata")
def metadata():
    """Page with metadata information of the uploaded file"""
    # Retrieve variables
    metadata = session.get('metadata', None)
    image = app.config['IMAGE_PATH']
    text = app.config['FOOTER_TEXT']
    # Render
    return render_template(
        'metadata.html',
        logo_image=image,
        metadata=metadata,
        footer_text=text)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8888)
