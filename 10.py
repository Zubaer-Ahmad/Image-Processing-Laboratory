import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread('lamp.jpg')

# Apply median filter (kernel size must be odd)
median = cv2.medianBlur(img, 5)

# Convert for display
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
med_rgb = cv2.cvtColor(median, cv2.COLOR_BGR2RGB)

# Display
plt.subplot(1,2,1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(med_rgb)
plt.title("Median Filtered")
plt.axis('off')

plt.show()