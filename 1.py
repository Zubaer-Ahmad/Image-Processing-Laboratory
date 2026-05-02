import numpy as np 
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('lab.jpg',1)
img_r = cv.cvtColor(img,cv.COLOR_BGR2RGB)

laplacian = cv.Laplacian(img,cv.CV_64F)
sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize=7)
sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=7)

plt.figure()
plt.subplot(2,2,1)
plt.imshow(img_r)
plt.title('Original')
plt.axis("off")

plt.subplot(2,2,2)
plt.imshow(sobelx)
plt.title('Sobel X')
plt.axis("off")

plt.subplot(2,2,3)
plt.imshow(sobely)
plt.title('Sobel Y')
plt.axis("off")

plt.subplot(2,2,4)
plt.imshow(laplacian)
plt.title('Laplacian')
plt.axis("off")
plt.show()