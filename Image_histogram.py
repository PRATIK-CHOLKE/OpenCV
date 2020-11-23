import cv2
import numpy as np
from matplotlib import pyplot as plt
def wind(image):
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

lena = cv2.imread("Images/lena.jpg", 0)
# wind(lena)

hist = cv2.calcHist([lena], [0], None, [256], [0, 256])

xaxis = np.arange(256).reshape(256, 1)
print (xaxis)

histogram = np.hstack((xaxis, hist)).astype(int)
plt.hist(lena.flatten(), 256, [0, 256])
plt.show()
equ = cv2.equalizeHist(lena)
wind(equ)

res = np.hstack((lena, equ))
wind(res)