import cv2
import numpy as np
import matplotlib.pyplot as plt
# Read image
img = cv2.imread('boy.jpg',1)

# Convert BGR (OpenCV default) to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Show image
plt.figure()
plt.subplot(121)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis("off")

# Plot histogram
plt.subplot(122)
plt.hist(gray.ravel(), bins=256)
plt.title("Grayscale Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")

plt.show()