
#!/usr/bin/python3
from PIL import Image
import os
from utils import get_size_format

def compress_img(image_name, new_size_ratio=0.9, quality=90, width=None, height=None, to_jpg=True, output_filename=None):
    # Load the image
    img = Image.open(image_name)

    # Get the original image size in bytes
    image_size = os.path.getsize(image_name)

    # Print the original image shape
    print("[*] Image shape:", img.size)

    # Print the size before compression/resizing
    print("[*] Size before compression:", get_size_format(image_size))

    # Resize the image if necessary
    if new_size_ratio < 1.0:
        # Resize with the specified ratio
        new_width = int(img.size[0] * new_size_ratio)
        new_height = int(img.size[1] * new_size_ratio)
        img = img.resize((new_width, new_height), Image.ANTIALIAS)
        # Print new image shape
        print("[+] New Image shape:", img.size)
    elif width and height:
        # Resize with the specified width and height
        img = img.resize((width, height), Image.ANTIALIAS)
        # Print new image shape
        print("[+] New Image shape:", img.size)

    # Generate a new filename with a counter if output_filename is not specified
    if not output_filename:
        filename, ext = os.path.splitext(image_name)
        i = 1
        while True:
            new_output_filename = f"{filename}_compressed_{i}{ext}"
            if not os.path.exists(new_output_filename):
                break
            i += 1
        output_filename = new_output_filename

    # Save the compressed image with the corresponding quality and optimize set to True
    img.save(output_filename, quality=quality, optimize=True)
    print("[+] New file saved:", output_filename)

    # Get the new image size in bytes
    new_image_size = os.path.getsize(output_filename)

    # Print the new size in a good format
    print("[+] Size after compression:", get_size_format(new_image_size))

    # Calculate the saving bytes
    saving_diff = new_image_size - image_size

    # Print the saving percentage
    print(f"[+] Image size change: {saving_diff/image_size*100:.2f}% of the original image size.")

    # Return the dimensions of the resized image
    return img.size
