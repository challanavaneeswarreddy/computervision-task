import cv2
import numpy
photo = cv2.imread("lion.jpg")
cv2.imshow("hi",photo)
cv2.waitKey()
cv2.destroyAllWindows()


p2 = cv2.imread("ship.jpeg")
cv2.imshow("hi",p2)
cv2.waitKey()
cv2.destroyAllWindows()


out = numpy.zeros([370,1080,3], dtype=numpy.uint8)
out[10:360,0:525] = photo
out[10:360,545:1070] = p2
cv2.imshow("hi",out)
cv2.waitKey()
cv2.destroyAllWindows()
