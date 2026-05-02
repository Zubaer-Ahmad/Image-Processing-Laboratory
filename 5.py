import cv2
import numpy as np
import matplotlib.pyplot as plt
# Read image
img = cv2.imread('bird.jpg')

# Increase brightness
beta = 50

bright = cv2.convertScaleAbs(img, alpha=1,beta=beta)
# Display
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
bright_rgb = cv2.cvtColor(bright, cv2.COLOR_BGR2RGB)

plt.subplot(2,1,1)
plt.imshow(img_rgb)
plt.title("Original")
plt.axis('off')

plt.subplot(2,1,2)
plt.imshow(bright_rgb)
plt.title("Bright Image")
plt.axis('off')
plt.show()
