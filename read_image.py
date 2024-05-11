#!/usr/bin/env python3

import tensorflow as tf
import os

# Function to read image from file
def read_image(file_path):
    # Read image file
    image = tf.io.read_file(file_path)
    # Decode image based on file format
    if file_path.lower().endswith('.png'):
        image = tf.image.decode_png(image, channels=3)  # RGB image
    elif file_path.lower().endswith('.jpg') or file_path.lower().endswith('.jpeg'):
        image = tf.image.decode_jpeg(image, channels=3)  # RGB image
    else:
        raise ValueError("Unsupported image format")
    return image

# Test reading an image
image_filename = "IMG-20230402-WA0001.jpg"
image_path = os.path.join("Image_compression_Algorithm", IMG-20230402-WA0001.jpg)
if os.path.exists(image_path):
    image = read_image(image_path)
    print("Image shape:", image.shape)
else:
    print("Image file not found")
