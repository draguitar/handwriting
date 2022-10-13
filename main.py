import cv2
import numpy as np

img = cv2.imread('image_1.jpg')

gray = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
blur = cv2.GaussianBlur(binary, (5, 5), 0)
edges = cv2.Canny(blur, 100, 300)

contours, hierarchy = cv2.findContours( edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
hierarchy = hierarchy[0]

# found = []

# for i in range(len(contours)):
#     k = i        # 层次递归指针
#     c = 0        # 层级计数

#     # 获取轮廓包围框及其长宽
#     rect = cv2.minAreaRect(contours[i])
#     w = rect[1][0]
#     h = rect[1][1]
#     if w and h:
#         rate = min(w, h) / max(w, h)
#         # 选取方形轮廓
#         if (rate >= 0.75 and w < img.shape[1] / 4 and h < img.shape[0] / 4):

#             # 判断轮廓层级，筛选多层轮廓的外围轮廓
#             while hierarchy[k][2] != -1:
#                 k = hierarchy[k][2]
#                 c = c + 1
#                 # 超过4层则判断为定位点
#                 if c >= 4:
#                     found.append(i)
#                     continue
#     else:
#         continue

# temp_contours = []
# for i in found:
#     temp_contours.append(contours[i])


# 顯示圖片
cv2.imshow('My Image', hierarchy)

# 按下任意鍵則關閉所有視窗
cv2.waitKey(0)
cv2.destroyAllWindows()