import cv2
import numpy as np

def wind(image):
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

bbal = cv2.imread("Images/sudoko.png", 1)
edges = cv2.Canny(bbal, 150, 400)

lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
print(lines)

for iterator in lines:
    rho = iterator[0][0]
    theta = iterator[0][1]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * a)
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * a)
    cv2.line(bbal, (x1, y1), (x2, y2), (0, 255, 0), 1)
wind(bbal)