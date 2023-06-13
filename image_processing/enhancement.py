import cv2
import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_laplace
from scipy import fftpack


import os

class ImageProcessor:
    def __init__(self, image_location: str) -> None:
        self.image_location = image_location

    def process(self) -> None:
        # Load image
        img = cv2.imread(self.image_location, 0)

        # # Convert to numpy array
        # img = np.array(img)

        # Your code here
        sharpen_kernel = np.array(([0, -1, 0],
                                    [-1, 5, -1],
                                    [0, -1, 0]), dtype=np.float64)
        
        sharpen_image = cv2.filter2D(src=img,
                             ddepth=-1,
                             kernel=sharpen_kernel)
        
        adjusted = cv2.convertScaleAbs(sharpen_image, 1, 0.7)

        hist,bins = np.histogram(adjusted.flatten(),256,[0,256])
        cdf = hist.cumsum()
        
        cdf_m = np.ma.masked_equal(cdf,0)
        cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
        cdf = np.ma.filled(cdf_m,0).astype('uint8')
        img2 = cdf[adjusted]

        threshold_value = 255  # Maximum pixel value for white
        max_value = 255  # Maximum pixel value in the image
        block_size = 5  # Block size for adaptive thresholding
        constant_add = 15  # Constant subtracted from the mean or weighted mean
        constant_sub = 10  # Constant subtracted from the mean or weighted mean

        # Apply adaptive thresholding
        _, thresholded = cv2.threshold(img2, threshold_value, max_value, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        # Increase the brightness of light pixels
        bright_pixels = cv2.add(img2, constant_add)

        # Decrease the brightness of dark pixels
        dark_pixels = cv2.subtract(bright_pixels, constant_sub)

        # Convert to PIL image
        img = Image.fromarray(dark_pixels)

        return img
    
    def save(self, img: Image) -> str:
        converted_img = img.convert("RGB")
        image_name = os.path.basename(self.image_location)
        
        save_location = os.path.join("resources", "img", "enhanced", image_name + "_enhanced.png")
        converted_img.save(save_location)

        return save_location