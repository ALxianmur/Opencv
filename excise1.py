import numpy as np
import cv2 as cv
img = cv.imread('13.jpg')
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'green',(10,400),font,4,(200,255,155),5,cv.LINE_AA)
cv.imshow('example',img)
cv.waitKey(0)
cv.destroyAllWindows()