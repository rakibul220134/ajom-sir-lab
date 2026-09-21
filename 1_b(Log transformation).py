import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img1.jpg',0)

# Formula: s = c * log(1 + r))
c = 255 / np.log(1 + np.max(img))
img_log = c * (np.log(1 + img))
img_log = np.uint8(img_log)

#plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Log Transformation")
plt.imshow(img_log, cmap='gray')
plt.axis('off')

#plt.tight_layout()
plt.show()