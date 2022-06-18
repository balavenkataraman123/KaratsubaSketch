from fileinput import filename
from flask import Flask, render_template, Response, request, send_file
from PIL import Image, ImageGrab
import base64
from io import BytesIO
import os
import uuid

from urllib3 import HTTPResponse

app = Flask(__name__)

@app.route('/draw', methods = ['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        data_url = request.values.get('image')
        content = data_url.split(';')[1]
        im_b64 = content.split(',')[1]
        im_bytes = base64.b64decode(im_b64)
    
        imgdata = base64.b64decode(im_b64)
        filename = "images/" + str(uuid.uuid4()) + '.png'
        with open(filename, 'wb') as f:
            f.write(imgdata)
        return "the path for the image is   " + filename
@app.route('/images/<filename>', methods=['GET'])
def getimage(filename):
    return send_file(f"images/{filename}")


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=False)
