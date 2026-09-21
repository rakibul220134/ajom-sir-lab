import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image.png", 0)

# 256 intensity levels
hist = [0] * 256

# Count pixels manually
for row in img:
    for pixel in row:
        hist[pixel] += 1

# Draw histogram
plt.title("Histogram")
plt.xlabel("Intensity")
plt.ylabel("Frequency")
plt.bar(range(256), hist)

plt.show()