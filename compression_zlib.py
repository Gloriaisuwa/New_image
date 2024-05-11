#!/usr/bin/env python3

import zlib

def compress_with_zlib(image_path):
    """
    Compresses image data using zlib.

    Args:
    - image_path: Path to the image file.

    Returns:
    - Compressed image data.
    """
    with open(image_path, 'rb') as f:
        image_data = f.read()

    # Adjust compression level to optimize compression ratio
    compression_level = 9  # Highest compression level
    compressed_data = zlib.compress(image_data, compression_level)

    # Debug statement to track compressed data size
    print("Compressed data size:", len(compressed_data))

    return compressed_data

if __name__ == "__main__":
    # Path to the image file
    image_path = "/Image_Compression_Algorithm/IMG-20230402-WA0001.jpg"
    
    # Compress the image data
    compressed_data = compress_with_zlib(image_path)
