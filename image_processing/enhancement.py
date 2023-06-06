import cv2
import numpy as np
from PIL import Image

import os

class ImageProcessor:
    def __init__(self, image_location: str) -> None:
        self.image_location = image_location

    def process(self) -> None:
        # Load image
        img = Image.open(self.image_location)

        # Convert to numpy array
        img = np.array(img)

        # Convert to grayscale
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Convert to PIL image
        img = Image.fromarray(img)

        return img
    
    def save(self, img: Image) -> str:
        image_name = os.path.basename(self.image_location)
        
        save_location = os.path.join("resources", "img", "enhanced", image_name + "_enhanced.png")
        img.save(save_location)

        return save_location