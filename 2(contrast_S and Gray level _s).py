import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image.png", 0)

# Contrast Stretching
min= np.min(img)
max =np.max(img)
contrast = ((img - min) / (max - min) * 255)
contrast = np.uint8(contrast)

# Gray Level Slicing (Threshold Range: 100 to 200)
slicing = np.zeros_like(img)
slicing[(img >= 100) & (img <= 200)] = 255  #mane ei range er pixel ke 255 (white) set kora hobe, baki sob ke 0 (black) set kora hobe

# 4. Display Images
images = [img, contrast, slicing]
titles = ["Original", "Contrast",  "Slicing"]
for k in range(3):
    plt.subplot(1, 3, k+1)
    plt.imshow(images[k], cmap="gray")
    plt.title(titles[k])
    plt.axis("off")

#plt.tight_layout()
plt.show()