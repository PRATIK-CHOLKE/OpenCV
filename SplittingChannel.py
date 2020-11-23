import cv2

# imCol = cv2.imread("im0.png", 1)

def wind (image):
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
imCol = cv2.imread("Images/im0.png", 1)
# wind(imCol)

b, g, r = cv2.split(imCol)
wind(imCol)