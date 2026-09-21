import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image.png", 0)

# 256 intensity levels
hist = [0] * 256

# Count pixels manually
for i in range(len(img)):
    for j in range(len(img[i])):
        hist[img[i][j]] += 1

#original image
plt.subplot(1, 2, 1)
plt.title("original")
plt.imshow(img, cmap="gray")
plt.axis("off")

# Draw histogram
plt.subplot(1, 2, 2)
plt.title("Histogram")
plt.xlabel("Intensity")
plt.ylabel("Frequency")
plt.bar(range(256), hist)

plt.show()