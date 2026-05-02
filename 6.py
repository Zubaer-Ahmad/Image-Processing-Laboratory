import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageEnhance

image = Image.open('lab.jpg')

contrast = ImageEnhance.Contrast(image)

new_contrast = 8.3

img_contrast = contrast.enhance(new_contrast)


plt.subplot(221)
plt.imshow(image)
plt.title("Original Image")
plt.axis('off')

plt.subplot(222)
plt.imshow(img_contrast)
plt.title("contrast")
plt.axis('off')

plt.show()


