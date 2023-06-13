import os
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

# Ambil gambar
print(os.getcwd())
img = cv.imread(os.path.join(os.getcwd(), "resources", "temp", "img.png"))
assert img is not None, "file could not be read, check with os.path.exists()"

# Ubah ke grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

# Noise removal
kernel = np.ones((3,3),np.uint8)
opening = cv.morphologyEx(thresh,cv.MORPH_OPEN,kernel, iterations = 4)

# Sure background area
sure_bg = cv.dilate(opening,kernel,iterations=3)

# Finding sure foreground area
dist_transform = cv.distanceTransform(opening,cv.DIST_L2,5)
ret, sure_fg = cv.threshold(dist_transform,0.7*dist_transform.max(),255,0)

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv.subtract(sure_bg,sure_fg)

# Marker labelling
ret, markers = cv.connectedComponents(sure_fg)
markers = markers+1
markers[unknown==255] = 0

# Watershed
markers = cv.watershed(img,markers)
img[markers == -1] = [255,0,0]

# Tampilkan
plt.subplot(221)
plt.imshow(img, cmap='gray')

# Save image
img = Image.fromarray(img)
img.save(os.path.join(os.getcwd(), "resources", "temp", "img.png"))