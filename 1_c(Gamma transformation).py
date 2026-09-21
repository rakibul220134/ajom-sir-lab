import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image.png", 0)

# পাওয়ার-ল ট্রান্সফরমেশন (Formula: s = c * r^gamma)
gamma = 0.5  # gamma < 1 ইমেজ ব্রাইট করবে, gamma > 1 ডার্ক করবে

gamma_img = (255 * (img / 255) ** gamma)
gamma_img = np.uint8(gamma_img)

images = [img, gamma_img]
titles = ["Original", "Gamma"]
for k in range(2):
    plt.subplot(1, 2, k+1)
    plt.imshow(images[k], cmap="gray")
    plt.title(titles[k])
    plt.axis("off")
plt.show()
