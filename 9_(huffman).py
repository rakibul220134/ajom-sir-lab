import cv2
from collections import Counter

img = cv2.imread("image.png", 0)
#pixel value frequency count
frequency = Counter(img.flatten())

# Each item is: [frequency, [[pixel, code], ...]]
groups = [[number, [[pixel, ""]]] for pixel, number in frequency.items()]
# Sort groups by frequency
while len(groups) > 1:
    groups.sort()
    # Pop the two groups with the lowest frequency
    left = groups.pop(0)
    right = groups.pop(0)

# Add "0" to the codes of the left group and "1" to the codes of the right group
    for item in left[1]:
        item[1] = "0" + item[1]
    for item in right[1]:
        item[1] = "1" + item[1]

# merge the two groups and append back to the list
    groups.append([left[0] + right[0], left[1] + right[1]])

codes = dict(groups[0][1])
encoded = "".join(codes[pixel] for pixel in img.flatten())

original_bits = img.size * 8
compressed_bits = len(encoded)

print("Original bits   :", original_bits)
print("Compressed bits :", compressed_bits)
print("Compression Ratio:", original_bits / compressed_bits)
