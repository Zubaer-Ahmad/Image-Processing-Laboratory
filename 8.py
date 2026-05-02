import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread('lamp.jpg')

# Apply average filter (5x5 kernel)
smooth = cv2.blur(img, (5,5))

# Convert for display
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
smooth_rgb = cv2.cvtColor(smooth, cv2.COLOR_BGR2RGB)

# Display
plt.subplot(1,2,1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(smooth_rgb)
plt.title("Smoothed Image")
plt.axis('off')

plt.show()