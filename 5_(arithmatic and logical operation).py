import cv2
import matplotlib.pyplot as plt

import edge

# Read two images
img1 = cv2.imread("img1.jpg", 0)
img2 = cv2.imread("img2.jpg", 0)

# Ensure both images have the exact same size
if img1.shape != img2.shape:
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# Arithmetic Operations
add = cv2.add(img1, img2)
sub = cv2.subtract(img1, img2)
mul = cv2.multiply(img1, img2, scale=1/255)

# Logical Operations
AND = cv2.bitwise_and(img1, img2)
OR = cv2.bitwise_or(img1, img2)
XOR = cv2.bitwise_xor(img1, img2)

#display
image=[add,sub,mul,AND,OR,XOR]
title=['Original','Addition','Subtraction','Multiplication','AND','OR','XOR']
for k in range(6):
    plt.subplot(2,3,k+1)
    plt.imshow(image[k],cmap='gray')
    plt.title(title[k])
    plt.axis('off')

#plt.tight_layout()
plt.show()