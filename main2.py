import cv2

# img = cv2.imread('sample_0.png')
img = cv2.imread('Eng2.png')
gray = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
blur = cv2.GaussianBlur(binary, (5, 5), 0)


contours, hierarchy = cv2.findContours(blur.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print(f'矩形數量:{len(contours)}')

# Next、Previous、First_child、Parent
# print(hierarchy[0][2][2])


draw_img = cv2.drawContours(img.copy(),contours,-1,(0,255,255),2)

found = []
center = []

for i in range(len(contours)):
    rect = cv2.minAreaRect(contours[i])
    w = rect[1][0]
    h = rect[1][1]

    if w and h:
        rate = min(w, h) / max(w, h)
        # 取定位矩形，非最外層
        # if (rate >= 0.75 and w < img.shape[1] / 4 and h < img.shape[0] / 4):
        if rate >= 0.8 :
            if hierarchy[0][i][2] != -1:
                if hierarchy[0][i][2] >= 4:
                    found.append(i)
    else:
        pass
print(found)
# print(hierarchy)
# --------------TODO--------------
# 取最小外接舉行的中心點

for i in found:
    rect = cv2.minAreaRect(contours[i])
    c = tuple(int(iten) for iten in rect[0])
    center.append(c)
    cv2.circle(draw_img, c, 2, (0, 0, 255), -1)


print(center)
# --------------TODO--------------


# 按下任意鍵則關閉所有視窗



cv2.imshow("img", draw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()