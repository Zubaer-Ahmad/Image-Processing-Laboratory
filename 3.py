import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread('lab.jpg')

# Convert to grayscale
img_r = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Create negative image
negative = 255 - img_r

# Show results
plt.subplot(1,2,1)
plt.imshow(img_r)
plt.title("Original")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(negative)
plt.title("Negative Image")
plt.axis('off')

plt.show()