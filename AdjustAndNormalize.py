import cv2
import numpy as np
import os

"""
# ==========================================================================================================================================================
#                                                                       PARAMETERS
# ==========================================================================================================================================================
"""

# Name to save the file
name = 'test_image'

# Name to find the folder
name_folder = 'paint'

# Ratio of the luminance
ratio = 145.0

# Name to find the folder where the images are stored
folder_name = 'FolderName'

# Name to find the folder where the images are stored
folder_name_save = 'Images_BGR'

"""
# ==========================================================================================================================================================
#                                                                           MAIN
# ==========================================================================================================================================================
"""

# Paths
path = os.getcwd()
path_folder = os.path.join(path, folder_name)
path_folder_save = os.path.join(path, folder_name_save)
if not os.path.exists(path_folder_save):
    os.makedirs(path_folder_save)

# List of files
list_files = os.listdir(path_folder)

# For each file
for file in list_files:
    # Read the image
    img = cv2.imread(os.path.join(path_folder, file))

    # Convert to HSV
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Get the luminance
    img_lum = img_hsv[:, :, 2]

    # Normalize the luminance
    img_lum = (img_lum - np.min(img_lum)) / (np.max(img_lum) - np.min(img_lum))

    # Normalize the luminance
    img_lum = img_lum * ratio

    # Put the luminance in the image
    img_hsv[:, :, 2] = img_lum

    # Convert to RGB
    img_bgr = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

    # Save the image
    cv2.imwrite(os.path.join(path_folder_save, file), img_bgr)
