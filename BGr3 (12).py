import math
from imutils import perspective
import numpy as np
import imutils
import cv2
import time
from matplotlib import pyplot as plt

def getmp(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7, 7), 0)

    edged = cv2.Canny(gray, 50, 100)
    edged = cv2.dilate(edged, None, iterations=1)
    edged = cv2.dilate(edged, None, iterations=1)
    edged = cv2.dilate(edged, None, iterations=1)
    edged = cv2.dilate(edged, None, iterations=1)
    edged = cv2.dilate(edged, None, iterations=1)
    edged = cv2.erode(edged, None, iterations=5)

    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        #
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:1]
    for c in cnts:
         # if the contour is not sufficiently large, ignore it
        if cv2.contourArea(c) < 1000:
            continue
            # compute the rotated bounding box of the contour
    box = cv2.minAreaRect(c)
    box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
    box = np.array(box, dtype="int")
    
    box = perspective.order_points(box)
    #print(box)
    cv2.drawContours(image, [box.astype("int")], -1, (0, 255, 0), 2)
    mx=(box[0][0]+box[1][0]+box[2][0]+box[3][0])/4
    my=(box[0][1]+box[1][1]+box[2][1]+box[3][1])/4
    a=[mx,my]
    plt.imshow(image)
    return a
lo=cv2.imread('al.png')
ro=cv2.imread('ar.png')


lr=getmp(ro)
lp=getmp(lo)
#lr=getmp(ro)

pdi=math.sqrt(((lp[0]-lp[1])*(lp[0]-lp[1]))+((lr[0]-lr[1])*(lr[0]-lr[1])))
print pdi


plt.colorbar()
plt.show()
      
