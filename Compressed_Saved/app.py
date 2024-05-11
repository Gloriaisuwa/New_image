#!/usr/bin/python3
from flask import Flask, request, send_file
from compress_image import compress_img
import tempfile
import ssl

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compress', methods=['POST'])
def compress_image():
    # Check if the POST request has the file part
    if 'image' not in request.files:
        return "No file part", 400
    
    file = request.files['image']

    # Save the received image data to a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
    file.save(temp_file.name)

    # Compress the image using your Python compression script
    compressed_image_path = compress_img(temp_file.name)

    # Return the compressed image file to the frontend
    return send_file(compressed_image_path, mimetype='image/jpeg')

if __name__ == '__main__':
    # Configure SSL context
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    ssl_context.load_cert_chain('cert.pem', 'key.pem')

    # Run the app with SSL enabled
    app.run(debug=True, ssl_context=ssl_context)
