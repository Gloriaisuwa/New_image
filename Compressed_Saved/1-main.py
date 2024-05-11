#!/usr/bin/python3
from compress_image import compress_img
from PIL import Image

if __name__ == "__main__":
    import argparse
    #from compress_img import compress_img

    parser = argparse.ArgumentParser(description="Simple Python script for compressing and resizing images")
    parser.add_argument("image", help="Target image to compress and/or resize")
    parser.add_argument("-j", "--to-jpg", action="store_true", help="Whether to convert the image to the JPEG format")
    parser.add_argument("-q", "--quality", type=int, help="Quality ranging from a minimum of 0 (worst) to a maximum of 95 (best). Default is 90", default=90)
    parser.add_argument("-r", "--resize-ratio", type=float, help="Resizing ratio from 0 to 1, setting to 0.5 will multiply width & height of the image by 0.5. Default is 1.0", default=1.0)
    parser.add_argument("-w", "--width", type=int, help="The new width image, make sure to set it with the `height` parameter")
    parser.add_argument("-hh", "--height", type=int, help="The new height for the image, make sure to set it with the `width` parameter")
    args = parser.parse_args()

    # compress the image
    compressed_filename = f"{args.image.split('.')[0]}_compressed.jpg"  # New filename for compressed image
    resized_dimensions = compress_img(args.image, args.resize_ratio, args.quality, args.width, args.height, args.to_jpg, compressed_filename)

    print("="*50)
    print("[+] Resized Image shape:", resized_dimensions)
    print(f"[+] Compressed image saved as: {compressed_filename}")
