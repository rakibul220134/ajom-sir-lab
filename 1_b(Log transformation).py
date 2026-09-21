import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img1.jpg',0)

# Formula: s = c * log(1 + r))
c = 255 / np.log(1 + np.max(img))
img_log = c * (np.log(1 + img))
img_log = np.uint8(img_log)

images = [img, img_log]
titles = ["Original", "Log"]
for k in range(2):
    plt.subplot(1, 2, k+1)
    plt.imshow(images[k], cmap="gray")
    plt.title(titles[k])
    plt.axis("off")

#plt.tight_layout()
plt.show()