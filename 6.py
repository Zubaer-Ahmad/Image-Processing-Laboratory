import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread('lab.jpg')

# Contrast enhancement
contrast = cv2.convertScaleAbs(img, alpha=2.0, beta=0)

# Convert BGR → RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
contrast_rgb = cv2.cvtColor(contrast, cv2.COLOR_BGR2RGB)

# Display images
plt.subplot(1,2,1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(contrast_rgb)
plt.title("Contrast Enhanced Image")
plt.axis('off')

plt.show()
