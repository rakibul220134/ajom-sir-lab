import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image.png", 0)

h, w = img.shape

# Empty images
binary = np.zeros_like(img)
eroded = np.zeros_like(img)
dilated = np.zeros_like(img)

# 1. Manual Thresholding
for i in range(h):
    for j in range(w):

        if img[i, j] >= 128:
            binary[i, j] = 255
        else:
            binary[i, j] = 0

# 2. Manual Erosion
for i in range(1, h-1):
    for j in range(1, w-1):
        errotion = True
        for x in range(-1, 2):
            for y in range(-1, 2):
                if binary[i+x, j+y] == 0:
                    errotion = False

        if errotion:
            eroded[i, j] = 255
        else:
            eroded[i, j] = 0
# 3. Manual Dilation
for i in range(1, h-1):
    for j in range(1, w-1):
        dilation = False
        for x in range(-1, 2):
            for y in range(-1, 2):

                if binary[i+x, j+y] == 255:
                    dilation = True
        if dilation:
            dilated[i, j] = 255
        else:
            dilated[i, j] = 0

# 4. Display Images
images = [img, binary, eroded, dilated]
titles = ["Original", "Binary",  "Erosion","Dilation"]
for k in range(4):
    plt.subplot(2, 2, k+1)
    plt.imshow(images[k], cmap="gray")
    plt.title(titles[k])
    plt.axis("off")

plt.show()