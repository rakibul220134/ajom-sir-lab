import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image.png", 0)

# Contrast Stretching
r_min, r_max = np.min(img), np.max(img)
contrast = ((img - r_min) / (r_max - r_min) * 255)
contrast = np.uint8(contrast)

# Gray Level Slicing (Threshold Range: 100 to 200)
slicing = np.zeros_like(img)
slicing[(img >= 100) & (img <= 200)] = 255  #mane ei range er pixel ke 255 (white) set kora hobe, baki sob ke 0 (black) set kora hobe

#plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.imshow(img, cmap="gray")
plt.title("Original")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(contrast, cmap="gray")
plt.title("Contrast Stretching")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(slicing, cmap="gray")
plt.title("Gray Level Slicing")
plt.axis("off")

#plt.tight_layout()
plt.show()