import cv2
import numpy as np
from matplotlib import pyplot as plt

def wind(image):
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

lena = cv2.imread("Images/lena.jpg", 0)

blur = cv2.blur(lena, (7,7))
wind(blur)

blurG = cv2.GaussianBlur(lena, (15, 15), 0)
wind(blurG)
res = np.hstack((lena, blurG))
wind(res)