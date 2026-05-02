import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread('lab.jpg')

# Convert to Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create figure
plt.figure(figsize=(12,5))

# ----------- RGB Histogram -----------
plt.subplot(1,2,1)

colors = ('r', 'g', 'b')
for i, col in enumerate(colors):
    hist = cv2.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=col)

plt.title("RGB Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.xlim([0,256])

# ----------- Grayscale Histogram -----------
plt.subplot(1,2,2)

hist_gray = cv2.calcHist([gray], [0], None, [256], [0,256])
plt.plot(hist_gray, color='black')

plt.title("Grayscale Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.xlim([0,256])

# Show both
plt.tight_layout()
plt.show()