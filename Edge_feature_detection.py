import cv2

def wind(image):
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

crops = cv2.imread("Images/crops.png", 0)
wind(crops)
edges1 = cv2.Canny(crops, 100, 200)
wind(edges1)

bbal = cv2.imread("Images/basketball.jpg", 1)
wind(bbal)
edges = cv2.Canny(bbal, 150, 400)
wind(edges)