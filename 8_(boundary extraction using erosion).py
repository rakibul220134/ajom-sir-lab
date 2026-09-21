import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('image.png',0)
h,w=img.shape

# Empty images
binary=np.zeros_like(img)
eroted=np.zeros_like(img)
boundary=np.zeros_like(img)

# 1. Manual Thresholding
for i in range(h):
    for j in range(w):
        if img[i,j]>=128:
            binary[i,j]=255
        else:
            binary[i,j]=0

# 2. Manual Erosion
for i in range(1,h-1):
    for j in range(1,w-1):
        errotion= True

        for x in range(-1,2):
            for y in range(-1,2):
                if binary[i+x,j+y]==0:
                    errotion=False

        if errotion:
            eroted[i,j]=255
        else:
            eroted[i,j]=0

# 3. Manual Boundary
for i in range(h):
    for j in range(w):
        boundary[i,j]=binary[i,j]-eroted[i,j]

# Display
image=[img,binary,eroted,boundary]
title=['original','Binary','Eroted','Boundary']
for k in range(4):
    plt.subplot(2,2,k+1)
    plt.imshow(image[k],cmap='gray')
    plt.title(title[k])
    plt.axis('off')

#plt.tight_layout()
plt.show()