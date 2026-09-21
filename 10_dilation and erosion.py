import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image.png", 0)

_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

#kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
kernel = np.ones((3, 3), np.uint8)

dilation = cv2.dilate(binary, kernel)
erosion = cv2.erode(binary, kernel)

plt.subplot(1, 3, 1)
plt.imshow(binary, cmap="gray")
plt.title("Binary")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(dilation, cmap="gray")
plt.title("Dilation")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.title("Erosion")
plt.imshow(erosion, cmap="gray")
plt.axis("off")

plt.show()