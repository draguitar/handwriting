import cv2

img = cv2.imread('sample_0.png')
gray = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)



contours, hierarchy = cv2.findContours(binary.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print(len(contours))
print(hierarchy[0][0])


draw_img0 = cv2.drawContours(img.copy(),contours,-1,(0,255,255),3)


# for i in range(len(contours)):
#     if 

# 按下任意鍵則關閉所有視窗

# cv2.imshow("img", draw_img0)
# cv2.waitKey(0)
# cv2.destroyAllWindows()