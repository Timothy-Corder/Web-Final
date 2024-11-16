import os
import shutil
from PIL import Image

def resize_image(image_path, scale_factor):
    """Upscales an image using the nearest neighbor method and overwrites it."""
    with Image.open(image_path) as img:
        new_size = (img.width * scale_factor, img.height * scale_factor)
        img_resized = img.resize(new_size, Image.NEAREST)
        img_resized.save(image_path)  # Overwrite the existing file

def upscale_folder(original_folder, scale_factor):
    """Creates (or updates) a copy of the original folder and upscales all PNG images."""
    # New folder name with the scaling factor
    new_folder = original_folder.replace("_x1", f"_x{scale_factor}")
    
    # Copy the folder if it doesn't exist, otherwise just update the images
    if os.path.exists(new_folder):
        shutil.rmtree(new_folder)
    shutil.copytree(original_folder, new_folder)
        
    
    # Iterate through all files in the folder (existing or newly copied)
    for root, dirs, files in os.walk(new_folder):
        for file in files:
            if file.lower().endswith('.png'):
                image_path = os.path.join(root, file)
                resize_image(image_path, scale_factor)

def main():
    # Get the current directory
    current_dir = os.getcwd()
    
    # Look for folders ending with "_x1"
    for folder in os.listdir(current_dir):
        full_path = os.path.join(current_dir, folder)
        if os.path.isdir(full_path) and folder.endswith("_x1"):
            # Create or update two copies: one with x4 and another with x8 scaling
            upscale_folder(full_path, 4)
            upscale_folder(full_path, 8)
    
    print("Upscaling and overwriting completed for all matching folders.")

if __name__ == "__main__":
    main()
