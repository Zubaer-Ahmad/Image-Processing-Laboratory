import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread('lamp.jpg')
# img = cv2.imread('boy.png')

if img is None:
    print("Error: Could not read image.")
    exit()

# Apply Gaussian filter
gaussian = cv2.GaussianBlur(img, (5,5), 0)

# Convert for display
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gauss_rgb = cv2.cvtColor(gaussian, cv2.COLOR_BGR2RGB)

# Display
plt.subplot(1,2,1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1,2,2)
cv2.imwrite('blur.png',gauss_rgb)
cv2.imwrite('blur.jpg', gauss_rgb)
plt.imshow(gauss_rgb)
plt.title("Gaussian Smoothed")
plt.axis('off')

plt.show()