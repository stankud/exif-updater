import json
import piexif
from PIL import Image
import datetime

# Function to convert timestamp to EXIF format
def timestamp_to_exif_format(timestamp):
    dt = datetime.datetime.utcfromtimestamp(timestamp)
    return dt.strftime("%Y:%m:%d %H:%M:%S")

# Load JSON data
with open('2009/IMG_0077.JPG.json', 'r') as file:
    metadata = json.load(file)

# Extract the photo taken time
photo_taken_time = metadata['photoTakenTime']['timestamp']

# Convert timestamp to EXIF format
exif_date = timestamp_to_exif_format(int(photo_taken_time))

# Load the image
img = Image.open('2009/IMG_0077.JPG')

# Check if the image has EXIF data
exif_dict = piexif.load(img.info['exif']) if 'exif' in img.info else {'Exif': {}}

# Update the EXIF date
exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = exif_date
exif_bytes = piexif.dump(exif_dict)

# Save the image with updated EXIF data
img.save('2009/IMG_0077_updated.JPG', exif=exif_bytes)

print("EXIF data updated successfully.")
