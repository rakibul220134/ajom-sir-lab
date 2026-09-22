import cv2
import numpy as np
import matplotlib.pyplot as plt

img =cv2.imread('image.png',0)

# Step 1: Calculate Histogram
hist=[0]*256
for i in img:
    for j in i:
        hist[j]+=1

# Step 2: Calculate CDF
cdf=[0]*256
cdf[0]=hist[0]
for i in range(1,256):
    cdf[i]=cdf[i-1]+hist[i]

# Total number of pixels
total_pixel=img.shape[0]*img.shape[1]
# Step 3: Create Mapping
mapping=[0]*256
for i in range(256):
    mapping[i]=round((cdf[i]/total_pixel) * 255)

# Step 4: Equalize Image
equlized=np.zeros_like(img)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        equlized[i,j]=mapping[img[i,j]]

# Step 5: Equalized Histogram
hist_equal=[0]*256

for i in equlized:
    for j in i:
        hist_equal[j] +=1

# Display
#plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(equlized, cmap='gray')
plt.title("Equalized Image")
plt.axis('off')

plt.subplot(2, 2, 3)
plt.bar(range(256), hist)
plt.title("Original Histogram")
plt.xlabel("Intensity")
plt.ylabel("Frequency")

plt.subplot(2, 2, 4)
plt.bar(range(256), hist_equal)
plt.title("Equalized Histogram")
plt.xlabel("Intensity")
plt.ylabel("Frequency")

#plt.tight_layout()
plt.show()