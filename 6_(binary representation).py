import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.png', 0)

h,w = img.shape

binary=np.zeros_like(img)

# 1. Manual Thresholding
for i in range(h):
    for j in range(w):
        if img[i,j]>=128:
            binary[i,j]=255
        else:
            binary[i,j]=0

#display
image=[img,binary]
title=['Original','Binary image']
for k in range(2):
    plt.subplot(1,2,k+1)
    plt.imshow(image[k],cmap='gray')
    plt.title(title[k])
    plt.axis('off')

#plt.tight_layout()
plt.show()