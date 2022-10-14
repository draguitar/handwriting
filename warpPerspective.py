# coding by 刘云飞
# email: liuyunfei.1314@163.com  
# date: 2018-5-18

from cgitb import handler
import cv2
import numpy as np

# 读取名称为 p19.jpg的图片
img = cv2.imread("p19.jpg",1)
img_org = cv2.imread("p19.jpg",1)

w = 215
h = 215
# 得到图片的高和宽
img_height,img_width = img.shape[:2]

# 定义对应的点
points1 = np.float32([[316,256], [613,334], [227,515], [652,514]])
points2 = np.float32([[0,0], [w,0], [0,h], [w,h]])

# 计算得到转换矩阵
M = cv2.getPerspectiveTransform(points1, points2)

# 实现透视变换转换
processed = cv2.warpPerspective(img,M,(w, h))

# 显示原图和处理后的图像
cv2.imshow("org",img_org)
cv2.imshow("processed",processed)

cv2.waitKey(0)