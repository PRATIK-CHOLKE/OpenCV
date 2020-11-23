import cv2

def wind(image):
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

crops = cv2.imread("Images/crops.png", 0)
# wind(crops)
sobelx = cv2.Sobel(crops, cv2.CV_8U, 1, 0, ksize=3)
wind(sobelx)

laplacian = cv2.Laplacian(crops, cv2.CV_8U)
wind(laplacian)