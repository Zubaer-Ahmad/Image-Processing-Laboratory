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

--------------------------- New Code:

from PIL import Image
from PIL import ImageEnhance
from matplotlib import pyplot as plt

# Opens the image file
image = Image.open('boy.png')
if image is None:
    print("Error: Could not read image.")
    exit()

# Enhance Color Level
curr_col = ImageEnhance.Color(image)
new_col = 2.5

# Color level enhanced by a factor of 2.5
img_colored = curr_col.enhance(new_col)

# shows updated image in image viewer
plt.subplot(121)
plt.imshow(image)
plt.title('Original')
plt.axis('off')

plt.subplot(122)
plt.imshow(img_colored)
plt.title('Color_Enhanced')
plt.axis('off')
plt.show()
