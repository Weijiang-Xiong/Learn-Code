import os
import glob
from PIL import Image, ExifTags
import matplotlib.pyplot as plt

folder_path = "C:\Media\Photography"
all_images = glob.glob(os.path.join(folder_path, "DSC*.jpg"))

focal_lengths = []
# Loop through all files in the folder
for filename in all_images:
        # Open the image
        with Image.open(filename) as img:
            # Extract EXIF data
            exif_data = {
                ExifTags.TAGS[k]: v
                for k, v in img._getexif().items()
                if k in ExifTags.TAGS
            }
            if exif_data:
                # Find the focal length tag
                focal_lengths.append(float(exif_data["FocalLength"]))

# Create a histogram of focal lengths
plt.hist(focal_lengths, bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Focal Length (mm)')
plt.ylabel('Frequency')
plt.title('Histogram of Focal Lengths')
plt.show()