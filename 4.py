import cv2
import matplotlib.pyplot as plt

img = cv2.imread('lamp.jpg')

# Enhancement factors
alpha = 1.5   # overall scaling

# Apply directly
enhanced = cv2.convertScaleAbs(img, alpha=alpha, beta=0)

# Display
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
enh_rgb = cv2.cvtColor(enhanced, cv2.COLOR_BGR2RGB)

plt.subplot(1,2,1)
plt.imshow(img_rgb)
plt.title("Original")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(enh_rgb)
plt.title("Enhanced")
plt.axis('off')

plt.show()
