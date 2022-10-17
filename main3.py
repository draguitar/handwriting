import cv2
import numpy as np
sp = np.float32()


def SortPoint(points):
    """
    对四个定位点进行排序，排序后顺序分别为左上、右上、左下、右下
    :param points: 待排序的点集
    :return: 排序完成的点集
    """
    sp = sorted(points, key=lambda x: (int(x[1]), int(x[0])))
    if sp[0][0] > sp[1][0]:
        sp[0], sp[1] = sp[1], sp[0]

    if sp[2][0] > sp[3][0]:
        sp[2], sp[3] = sp[3], sp[2]

    return sp

def _intersection(a, b):
    """
    判断两个 rect 是否相交
    :param a: rect1
    :param b: rect2
    :return: 是否相交，bool， 相交为 True，不相交为 False
    """
    x = max(a[0], b[0])
    y = max(a[1], b[1])
    w = min(a[0] + a[2], b[0] + b[2]) - x
    h = min(a[1] + a[3], b[1] + b[3]) - y
    if w < 0 or h < 0:
        return False  # or (0, 0, 0, 0) ?
    return True

def is_duplicate(c, contours):
    """
    判断当前轮廓是否与其他轮廓属于同一定位点，用于筛选同一定位点的唯一轮廓
    :param c: 当前判断的 contour
    :param contours: 当前所有非重叠 contours 集合
    :return: contours 中是否存在与 c 相交的轮廓，bool，重复轮廓返回 True，不重复返回 False
    """
    r = cv2.boundingRect(c)
    for contour in contours:
        rect = cv2.boundingRect(contour)
        if _intersection(r, rect):
            return True
        else:
            continue
    return False

img = cv2.imread('step_2.png')
print(img.shape)

top = int(img.shape[0]*0.3)
bottom = int(img.shape[0]*0.6)

left = int(img.shape[1]*0.3)
right = left = int(img.shape[1]*0.6)



gray = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(
    gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
blur = cv2.GaussianBlur(binary, (3, 3), 0)
edges = cv2.Canny(blur, 100, 300)

contours, hierarchy = cv2.findContours(
    edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
hierarchy = hierarchy[0]


found = []

for i in range(len(contours)):
    k = i        # 层次递归指针
    c = 0        # 层级计数

    # 获取轮廓包围框及其长宽
    rect = cv2.minAreaRect(contours[i])
    w = rect[1][0]
    h = rect[1][1]
    if w and h:
        rate = min(w, h) / max(w, h)
        # 选取方形轮廓
        if (rate >= 0.75 and w < img.shape[1] / 4 and h < img.shape[0] / 4):
            # 判断轮廓层级，筛选多层轮廓的外围轮廓
            while hierarchy[k][2] != -1:
                k = hierarchy[k][2]
                c = c + 1
                # 超过4层则判断为定位点
                if c >= 4:
                    found.append(i)
                    continue
    else:
        continue



temp_contours = []
for i in found:
    temp_contours.append(contours[i])

candidate_contours = []
candidate_contours.append(contours[0])

for i in range(1, 12):
    if is_duplicate(contours[i], candidate_contours):
        continue
    else:
        candidate_contours.append(contours[i])


img=cv2.drawContours(img,temp_contours,-1,(0,0,255),2, cv2.LINE_AA)  # img为三通道才能显示轮廓

# cv2.imshow('drawimg',img)
left_top = []
left_bottom = []
right_top = []
right_bottom =[]

pos_list = len(temp_contours)
for i in range(pos_list):
    pos_rect = cv2.minAreaRect(temp_contours[i])
    x = int(pos_rect[0][0])
    y = int(pos_rect[0][1])
    if x > left:
        if y > top:
            right_bottom.append((x, y))
        else:
            right_top.append((x, y))
    else:
        if y > top:
            left_bottom.append((x, y))
        else:
            left_top.append((x, y))

lt = np.mean(np.array(left_top), axis=0 ,dtype="int32")
lb = np.mean(np.array(left_bottom), axis=0 ,dtype="int32")
rt = np.mean(np.array(right_top), axis=0 ,dtype="int32")
rb = np.mean(np.array(right_bottom),axis=0 ,dtype="int32")


cv2.circle(img,(lt), 2, (255, 0, 0), -1)
cv2.circle(img,(lb), 2, (255, 255, 0), -1)
cv2.circle(img,(rt), 2, (255, 0, 255), -1)
cv2.circle(img,(rb), 2, (0, 0, 0), -1)

    # if i%3==0:
    #     cv2.circle(img,(int(pos_rect[0][0]),int(pos_rect[0][1])), 4, (255, 0, 0), -1)
    # elif i%3==1:
    #     cv2.circle(img,(int(pos_rect[0][0]),int(pos_rect[0][1])), 4, (0, 255, 0), -1)
    # else:
    #     cv2.circle(img,(int(pos_rect[0][0]),int(pos_rect[0][1])), 4, (0, 0, 255), -1)

# def out(candidate_contours):
#     if len(candidate_contours) >= 4:
#         candidate_contours = candidate_contours[0:4]
#         for i in range(4):
#             img2 = cv2.drawContours(img, candidate_contours, i,(0, 0, 255), 2, cv2.LINE_AA)
#             cv2.imshow(str(i,img2)
#         location_points = []

#         for i in range(0, 4):
#             pos_rect = cv2.minAreaRect(candidate_contours[i])
#             location_points.append(pos_rect[0])

#         # 对定位点排序，排序后顺序为：左上，右上，左下，右下
#         location_points = SortPoint(location_points)
#         return location_points
#     else:
#         print(len(contours))
#         for i in range(len(contours)):
#             cv2.drawContours(img, contours, i,
#                             (255, 255, 0), 2, cv2.LINE_AA)
#             print("未找到足够的定位点")

# sp = out(candidate_contours)

# # 透视变换，转换为正视图
# pts1 = np.float32(sp)
# pts2 = np.float32([[0, 0], [1000, 0], [0, 750], [1000, 750]])
# transform = cv2.getPerspectiveTransform(pts1, pts2)
# warpedimg = cv2.warpPerspective(img, transform, (1000, 750))

# # 设定裁剪边距，完全去除定位标志
# padding = np.int0(warpedimg.shape[0] * 0.06)
# img_cropped = warpedimg[padding:(
#     warpedimg.shape[0] - padding), padding:(warpedimg.shape[1] - padding)]
# img_output = cv2.resize(img_cropped, (400, 300),
#                         interpolation=cv2.INTER_CUBIC)

cv2.imshow('2',img)
cv2.waitKey(0)
cv2.destroyAllWindows()