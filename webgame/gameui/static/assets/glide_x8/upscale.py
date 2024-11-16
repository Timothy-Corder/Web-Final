import os
import shutil
from PIL import Image

def resize_image(image_path, output_path, scale_factor=2):
    # Open the image
    with Image.open(image_path) as img:
        # Resize the image without smoothing (using nearest neighbor for pixel art)
        new_size = (img.width * scale_factor, img.height * scale_factor)
        img_resized = img.resize(new_size, Image.NEAREST)
        # Save the resized image
        img_resized.save(output_path)

def copy_and_resize_folder(size):
    # Get the current script directory
    script_dir = os.path.dirname(os.path.realpath(__file__))
    
    # Destination directory (we'll copy to a new folder with "_copy" suffix)
    copy_dir = script_dir + f"_x{size}"
    
    # Copy the entire directory structure (including files)
    shutil.copytree(script_dir, copy_dir)
    
    # Iterate through all files in the copied directory
    for root, dirs, files in os.walk(copy_dir):
        for file in files:
            if file.lower().endswith('.png'):
                # Construct the full file path
                image_path = os.path.join(root, file)
                # Resize the PNG image and save it in place
                resize_image(image_path, image_path, size)

if __name__ == "__main__":
    copy_and_resize_folder(int(input('Size: ')))
    print("Folder copied and images resized.")
