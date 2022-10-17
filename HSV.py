import cv2
import matplotlib.pyplot as plt
import numpy as np
image = cv2.imread('./img/image_1.png')

# Converting the image to hsv
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red = np.array([160,50,50])
upper_red = np.array([180,255,255])

mask = cv2.inRange(hsv, lower_red, upper_red)

print(mask)

cv2.imshow('MASK',mask)

res = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow('Result',res)

cv2.waitKey(0)
cv2.destroyAllWindows()