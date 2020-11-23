import cv2
import numpy as np
from matplotlib import pyplot as plt

def wind(image):
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread("Images/im0.png", 1)
# wind(img)

imgCL = np.float32(img.reshape((-1, 3)))
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 15, 1.0)
K = 4
ret, lab, center = cv2.kmeans(imgCL, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
# print(ret, lab, center)

center = np.uint8(center)
res = center[lab.flatten()]
# print(res)

res2 = res.reshape(img.shape)
wind(res2)