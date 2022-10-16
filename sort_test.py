import numpy as np
def order_points(pts):
    ''' sort rectangle points by clockwise '''
    sort_x = pts[np.argsort(pts[:, 0]), :]

    Left = sort_x[:2, :]
    Right = sort_x[2:, :]
    # Left sort
    Left = Left[np.argsort(Left[:,1])[::-1], :]
    # Right sort
    Right = Right[np.argsort(Right[:,1]), :]

    return np.concatenate((Left, Right), axis=0)

img = np.zeros((512, 512, 3), dtype=np.uint8)
pts = np.array([[128,128],[256,256],[256,100],[128,256],[128, 127]], dtype=np.int32)
pts = order_points(pts)
print(pts)