import cv2

def wind(image):
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

imgN = cv2.imread("Images/double.png", 1)
hsv = cv2.cvtColor(imgN, cv2.COLOR_BGR2HSV)
wind(hsv)

gray = cv2.cvtColor(imgN, cv2.COLOR_BGR2GRAY)
wind(gray)

r, t = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
print (r)
print (t)
wind(t) 
