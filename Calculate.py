import math
from imutils import perspective
import numpy as np
import imutils
import cv2
import time
from matplotlib import pyplot as plt

def getmp(image):
    
    gra = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    gray = gra[:,:,2]
    gray = cv2.GaussianBlur(gray, (7,7), 0)
    gray = cv2.GaussianBlur(gray, (7,7), 0)
    edged = cv2.inRange(gray, 0, 70)
    
    

    
    edged = cv2.dilate(edged, None, iterations=10)
    
    edged = cv2.erode(edged, None, iterations=5)
    
    edged = cv2.dilate(edged, None, iterations=10)
    
    edged = cv2.erode(edged, None, iterations=30)
    edged = cv2.dilate(edged, None, iterations=40)
    ff=np.where(edged>50)
    a1=np.mean(ff[1])

    
    return a1
lo=cv2.imread('a30.jpg')
ro=cv2.imread('b30.jpg')


#lr=getmp(ro)
lp=getmp(lo)
lr=getmp(ro)

pdi=abs(lp-lr)
y=(pdi*(-8.1167))+28875.91
print y/pdi


      
