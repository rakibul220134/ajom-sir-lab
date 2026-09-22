import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

img = cv2.imread('image.png', 0)

h,w = img.shape

smooth=np.zeros_like(img)
sharp=np.zeros_like(img)
edge=np.zeros_like(img)

for i in range(1,h-1):
    for j in range(1,w-1):

        #smooth
        total=0
        for x in range(-1,2):
            for y in range(-1,2):
                total +=int(img[i+x ,j+y])

        smooth[i,j]=total /9

        #sharp
        s= (
            5*int(img[i,j])
            - int(img[i-1,j])
            - int(img[i+1,j])
            - int(img[i,j-1])
            - int(img[i,j+1])
        )

        sharp[i,j]=max(0,min(255,s))

        #soble
        gx=(
            -int(img[i-1,j-1])
            + int(img[i-1,j+1])
            - 2* int(img[i,j-1])
            + 2* int(img[i,j+1])
            - int(img[i+1,j-1])
            + int(img[i+1,j+1])
        )

        gy=(
            - int(img[i-1,j-1])
            - 2* int(img[i-1,j])
            - int(img[i-1,j+1])
            + int(img[i+1,j-1])
            + int(img[i+1,j])
            + int(img[i+1,j+1])
        )
        magnatude=math.sqrt(gx*gx + gy*gy)
        edge[i,j]=min(255,int(magnatude))


#display
image=[img,smooth,sharp,edge]
title=['Original','smoothing','sharpning','edge detection']
for k in range(4):
    plt.subplot(2,2,k+1)
    plt.imshow(image[k],cmap='gray')
    plt.title(title[k])
    plt.axis('off')

#plt.tight_layout()
plt.show()