import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./img/girl.jpg')

plt.imshow(img[:,:,::-1])
plt.xticks([])
plt.yticks([])
plt.show()