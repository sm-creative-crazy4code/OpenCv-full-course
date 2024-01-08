import cv2 
import numpy as np

# Creating a canvas 500x500 (3 channels)
canvas = np.zeros((500,500,3))

# drawing a line
# @params 
# img=canvas to draw the image
# pt1,pt2----> points to specify the starting point and end points of a the line
# color----> 3 chanel color in bgr format
# Thickness----> thickness of the lines in pixels
# line type---> 3 types of linetyoes Quadraple(4),Octa(8),antialise line(AA)

# Aliasing and Antialiasing Lines
# Aliased lines= no transparent pixels are present 
# Antialiased lines= transparent pixels are present

# line 4 ,line 8 -> drawn using bresenham algorithm
#line AA -> Gausian filtering

cv2.line(canvas,(0,0),(100,100),(0,255,0),2,cv2.LINE_4 )
cv2.line(canvas,(0,0),(150,150),(0,255,0),2,cv2.LINE_AA )

# Drawing a Rectangle
# here the points are diagonal points
# thickness -1 leads to filling of the shapes

cv2.rectangle(canvas,(200,200),(250,279),(0,0,255),-1)

# circle takes centerpoint and radius
cv2.circle(canvas,(350,350),10,(255,0,0),3)

# drawing a arrowtip
# requires additional tiplength parameter
cv2.arrowedLine(canvas,(400,400),(400,500),(255,255,255),tipLength=0.3)

# showing the images
cv2.imshow('shapes', canvas)
cv2.waitKey(20000)