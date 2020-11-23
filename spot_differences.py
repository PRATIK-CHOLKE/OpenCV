import cv2
from copy import deepcopy

imgN = cv2.imread("Images/double.png", 1)
imgN = deepcopy(imgN)

def click2circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(imgN, (x, y), 50, (255, 0, 0), 4)
cv2.namedWindow("differences", cv2.WINDOW_NORMAL)
cv2.setMouseCallback("differences", click2circle)

while True:
    cv2.imshow("differences", imgN)
    a = cv2.waitKey(2000)
    if a == 27:
        break
cv2.destroyAllWindows()