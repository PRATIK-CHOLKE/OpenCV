import cv2
from copy import deepcopy

def wind (image):
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

imgCol = cv2.imread("Images/im0.png", 1)
cv2.namedWindow("window", cv2.WINDOW_NORMAL)
imgCol1 = deepcopy(imgCol)

imgres = cv2.resize(imgCol1, dsize=None, fx=0.2, fy=0.2, interpolation=cv2.INTER_CUBIC)

cv2.imshow("window", imgres)
cv2.waitKey(0)
cv2.destroyAllWindows()

cropped = imgres[210:368, 380:570]
wind(cropped)
cv2.imwrite("Images/wheel.png", cropped)
