# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 20:10:34 2020

@author: Karunya V
"""

img = cv2.imread('brain1.jpg',0)
edges = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()