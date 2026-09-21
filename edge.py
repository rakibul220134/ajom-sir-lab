import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image.png", 0)

Gx = np.array([[-1, 0, 1],
               [-2, 0, 2],
               [-1, 0, 1]])

Gy = np.array([[-1, -2, -1],
               [ 0,  0,  0],
               [ 1,  2,  1]])

edge_x = cv2.filter2D(img, cv2.CV_64F, Gx)
edge_y = cv2.filter2D(img, cv2.CV_64F, Gy)

edge = cv2.convertScaleAbs(edge_x) + cv2.convertScaleAbs(edge_y)

plt.imshow(edge, cmap="gray")
plt.title("Manual Sobel Edge Detection")
plt.axis("off")
plt.show()