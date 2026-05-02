import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread('image.jpg')

# Sharpening kernel
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])

# Apply filter
sharpened = cv2.filter2D(img, -1, kernel)

# Convert for display
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
sharp_rgb = cv2.cvtColor(sharpened, cv2.COLOR_BGR2RGB)

# Show images side by side
plt.subplot(1,2,1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(sharp_rgb)
plt.title("Sharpened Image")
plt.axis("off")

plt.show()