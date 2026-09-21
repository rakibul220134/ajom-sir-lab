import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image.png", 0)

negative = 255 - img

plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(img, cmap="gray")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Negative")
plt.imshow(negative, cmap="gray")
plt.axis("off")

plt.show()