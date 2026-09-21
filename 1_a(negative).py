import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image.png", 0)

negative = 255 - img

images = [img, negative]
titles = ["Original", "Negative"]
for k in range(2):
    plt.subplot(1, 2, k+1)
    plt.imshow(images[k], cmap="gray")
    plt.title(titles[k])
    plt.axis("off")

plt.show()