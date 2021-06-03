import cv2

photo = cv2.imread("wall.jpeg")
cv2.imshow("hi",photo)
cv2.waitKey()
cv2.destroyAllWindows()


p2 = cv2.imread("love.jpg")
cv2.imshow("hi",p2)
cv2.waitKey()
cv2.destroyAllWindows()

cp2=p2[40:145,150:245]
cv2.imshow("hi",cp2)
cv2.waitKey()
cv2.destroyAllWindows()


photo[40:145,150:245]=p2[70:175,285:380]
cv2.imshow("hi",photo)
cv2.waitKey()
cv2.destroyAllWindows()

p2[70:175,285:380]= cp2
cv2.imshow("hi",p2)
cv2.waitKey()
cv2.destroyAllWindows()
