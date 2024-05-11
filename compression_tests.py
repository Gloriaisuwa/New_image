#!/usr/bin/env python3

import unittest
from compression_zlib import compress_with_zlib

class TestCompression(unittest.TestCase):
    def test_compress_with_zlib(self):
        # Path to the image file
        image_path = "/Image_Compression_Algorithm/IMG-20230402-WA0001.jpg"

        # Call the compress_with_zlib function with the image path
        compressed_data = compress_with_zlib(image_path)

        # Verify the result
        # Adjust the expected compressed size based on your expectations
        expected_compressed_size = ...  # Adjust this based on your expectations
        self.assertLess(len(compressed_data), expected_compressed_size)

        # Print a message indicating the test passed
        print("compress_with_zlib test passed.")

if __name__ == '__main__':
    unittest.main()
