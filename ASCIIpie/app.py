from flask import Flask, request, render_template, send_file  # make_response
from ASCIIpie import asciipie
from io import BytesIO

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    return_text = (request.args.get('type') == 'text')
    asciipied = asciipie(file, save=False, text_mode=return_text)
    if return_text:
        return asciipied
    # return make_response(asciipied.tobytes())
    buffer = BytesIO()
    asciipied.save(buffer, 'PNG')
    buffer.seek(0)
    return send_file(buffer, mimetype='image/png')
