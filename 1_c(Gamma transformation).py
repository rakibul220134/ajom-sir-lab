import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image.png", 0)

# পাওয়ার-ল ট্রান্সফরমেশন (Formula: s = c * r^gamma)
gamma = 0.5  # gamma < 1 ইমেজ ব্রাইট করবে, gamma > 1 ডার্ক করবে

gamma_img = (255 * (img / 255) ** gamma)
gamma_img = np.uint8(gamma_img)

plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(img, cmap="gray")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Gamma")
plt.imshow(gamma_img, cmap="gray")
plt.axis("off")

plt.show()
