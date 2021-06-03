import cv2
import numpy
photo = numpy.zeros([100,100,3], dtype=numpy.uint8)

i=0;
while i<=99:
    j=0
    while j<=99:
        if (i>40 and i<=60) and (j>40 and j<=60):
            photo[i][j]=[7,57,201]
        elif(i>20 and i<=80) and (j>20 and j<=80):
            photo[i][j]=[191,255,0]
        else:
            photo[i][j]=[255,0,191]
        j = j + 1
    i= i + 1    


cv2.imshow('hi',photo)
cv2.waitKey()
cv2.destroyAllWindows()    
