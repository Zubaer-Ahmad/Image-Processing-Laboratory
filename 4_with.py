import cv2
import matplotlib.pyplot as plt

img = cv2.imread('lamp.jpg')

# Convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(hsv)

# Increase saturation (color enhancement)
s = cv2.add(s, 60)

hsv_enhanced = cv2.merge([h, s, v])

enhanced = cv2.cvtColor(hsv_enhanced, cv2.COLOR_HSV2BGR)

# Convert for display
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
enh_rgb = cv2.cvtColor(enhanced, cv2.COLOR_BGR2RGB)

plt.subplot(1,2,1)
plt.imshow(img_rgb)
plt.title("Original")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(enh_rgb)
plt.title("Color Enhanced")
plt.axis('off')

plt.show()