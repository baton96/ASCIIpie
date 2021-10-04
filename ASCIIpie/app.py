from flask import Flask, request, render_template, make_response
from ASCIIpie import asciipie_bytes

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    asciipied = asciipie_bytes(file)
    return make_response(asciipied)
