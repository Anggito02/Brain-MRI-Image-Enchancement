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
        img = cv2.imread(self.image_location)

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Sharpen
        sharpen_kernel = np.array(([0, -1, 0],
                                    [-1, 5, -1],
                                    [0, -1, 0]), dtype=np.float64)

        sharpen_image = cv2.filter2D(src=gray,
                                    ddepth=-1,
                                    kernel=sharpen_kernel)

        adjusted = cv2.convertScaleAbs(sharpen_image, 100, 1)

        # Brightness
        hist, bins = np.histogram(adjusted.flatten(), 256, [0, 256])
        cdf = hist.cumsum()

        cdf_m = np.ma.masked_equal(cdf, 0)
        cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
        cdf = np.ma.filled(cdf_m, 0).astype('uint8')
        img2 = cdf[adjusted]

        # Contrast
        _, img_res = cv2.threshold(img2, 250, 255, cv2.THRESH_BINARY)

        # Convert to PIL image
        img = Image.fromarray(img_res)

        return img
    
    def save(self, img: Image) -> str:
        converted_img = img.convert("RGB")
        image_name = os.path.basename(self.image_location)
        
        save_location = os.path.join("resources", "img", "enhanced", image_name + "_enhanced.png")
        converted_img.save(save_location)

        return save_location