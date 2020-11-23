import cv2
import numpy as np

def wind(image):
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

imN = cv2.imread("Images/double.png", 1)
# wind(imN)

diffs = np.array([[538, 109], [1203, 739], [758, 137], [1240, 467]])

def euclid(x1, x2, y1, y2):
    return int(np.sqrt((x1 - x2)**2 + (y1 - y2)**2))

def click2circle(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        for diff in diffs:
            if euclid(x, diff[0], y, diff[1]) < 50:
                cv2.circle(imN, (x, y), 50, (255, 0, 0), 4)
cv2.namedWindow("differences", cv2.WINDOW_NORMAL)
cv2.setMouseCallback("differences", click2circle)

while True:
    cv2.imshow("differences", imN)
    a = cv2.waitKey(2000)
    if a == 27:
        break
cv2.destroyAllWindows()