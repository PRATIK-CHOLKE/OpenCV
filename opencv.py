import cv2
from copy import deepcopy

def wind (image):
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

imgCol = cv2.imread("Images/im0.png", 1)
wind(imgCol)

imgCol1 = deepcopy(imgCol)
circle = cv2.circle(imgCol1, (780, 1280), 350, (125, 255, 50), 20)
wind(circle)

