from flask import Flask, send_from_directory, send_file, request
import random
import numpy
from PIL import Image
import imageio
import os
from libs.algorithms.remove_noise import remove_noise
from libs.algorithms.bilateral import bilateral_filter
from libs.algorithms.guided import guided_filter

from libs.utils import getSourceImg, getI420FromBase64

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

target = os.path.join(APP_ROOT, 'static/images')

targetUpload = os.path.join(APP_ROOT, 'static/images/uploaded')

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)


@app.route("/upload", methods=["POST"])
def upload():
    data_req = request.get_json()
    imgdata = getI420FromBase64(data_req['image'])

    filename = 'static/images/uploaded/uploaded.png'
    with open(filename, 'wb') as f:
        f.write(imgdata)

    return send_from_directory("static/images/uploaded", "uploaded.png")

@app.route('/static/images/<filename>')
def send_image(filename):
    return send_from_directory("static/images", filename)


@app.route("/mean", methods=["POST"])
def mean():

    req = request.get_json()

    new_filename = "edited/mean.png"
    input_img = Image.open(getSourceImg(targetUpload, 'uploaded.png'))
    result = remove_noise(input_img,req['kernel_dim'],"mean")
    imageio.imwrite(target + '/' + new_filename, result) 

    return send_image(new_filename)

@app.route("/median", methods=["POST"])
def median():

    req = request.get_json() # dict type

    new_filename = "edited/median.png"
    input_img = Image.open(getSourceImg(targetUpload, 'uploaded.png'))
    result = remove_noise(input_img,req['kernel_dim'],"median")
    imageio.imwrite(target + '/' + new_filename, result) 


    return send_image(new_filename)

@app.route("/bilateral", methods=["POST"])
def bilateral():

    req = request.get_json()

    radius = req['radius']
    sigma_d = req['sigma_d']
    sigma_r = req['sigma_r']

    new_filename = "edited/bilateral.png"
    input_img = Image.open(getSourceImg(targetUpload, 'uploaded.png'))
    result = bilateral_filter(input_img, radius, sigma_d, sigma_r)
    imageio.imwrite(target + '/' + new_filename, result) 

    return send_image(new_filename)

@app.route("/guided", methods=["POST"])
def guided():
    req = request.get_json()

    radius = req['radius']
    eps = req['eps']

    new_filename = "edited/guided.png"
    input_img = Image.open(getSourceImg(targetUpload, 'uploaded.png'))
    result = guided_filter(input_img, radius, eps)
    imageio.imwrite(target + '/' + new_filename, result) 

    return send_image(new_filename)

if __name__ == "__main__":
    app.run(debug=True)
