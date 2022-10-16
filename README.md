## 範例
https://huangmiz.com/huangmiz-font/

## 字體
https://github.com/Chenyu-otf/chenyuluoyan_thin

## opencv 定位
https://www.jaspr.me/extract-color-card-with-python-and-opencv/

## 修正傾斜
https://blog.gtwang.org/programming/python-opencv-auto-crop-and-rotate-scanned-image-tutorial/

# findContours
```
cv.findContours(image, mode, method ) ->	contours, hierarchy
```

一、獲取輪廓--findContours
cv2.findContours() 的第二個引數主要有

cv2.RETR_LIST：檢測的輪廓不建立等級關係
cv2.RETR_TREE：L建立一個等級樹結構的輪廓。
cv2.RETR_CCOMP：建立兩個等級的輪廓，上面的一層為外邊界，裡面的一層為內孔的邊界資訊。
cv2.RETR_EXTERNAL：表示只檢測外輪廓
cv2.findContours() 的第三個引數 method為輪廓的近似辦法

cv2.CHAIN_APPROX_NONE儲存所有的輪廓點，相鄰的兩個點的畫素位置差不超過1，即max（abs（x1-x2），abs（y2-y1））==1
cv2.CHAIN_APPROX_SIMPLE壓縮水平方向，垂直方向，對角線方向的元素，只保留該方向的終點座標，例如一個矩形輪廓只需4個點來儲存輪廓資訊
cv2.CHAIN_APPROX_TC89_L1，CV_CHAIN_APPROX_TC89_KCOS使用teh-Chinl chain 近似演算法
返回值：image, contours, hierarchy

contour返回值
cv2.findContours()函式首先返回一個list，list中每個元素都是影像中的一個輪廓，用numpy中的ndarray表示。
hierarchy返回值
該函式還可返回一個可選的hiararchy結果，這是一個ndarray，其中的元素個數和輪廓個數相同，每個輪廓contours[i]對應4個hierarchy元素hierarchy[i][0] ~hierarchy[i][3]，分別表示後一個輪廓、前一個輪廓、父輪廓、內嵌輪廓的索引編號，如果沒有對應項，則該值為負數。

二、繪出輪廓--drawContours
cv2.drawContours(image, contours, contourIdx, color[, thickness[, lineType[, hierarchy[, maxLevel[, offset ]]]]])

第一個引數是指明在哪幅影像上繪製輪廓；
第二個引數是輪廓本身，在Python中是一個list。
第三個引數指定繪製輪廓list中的哪條輪廓，如果是-1，則繪製其中的所有輪廓。後面的引數很簡單。其中thickness表明輪廓線的寬度，如果是-1（cv2.FILLED），則為填充模式。繪製引數將在以後獨立詳細介紹。
