import cv2
# im opencv for images -> imradd and imwrite
# in opencv for videos -> videocapture and videowrite are used

#  this reads the file and stores it inside a  image as a  matrix
# here there is  a default parameter cv2.IMAGE_COLOR that reads the image in colour
# channel order BGR
# cv2.imread_greyscle=grayscale image
#cv2.imread_UNCHANGED= alpha mask
image= cv2.imread("test.png")

# to show the file we use cv2.imshow passing the window name and the image matrix we wish to display 
cv2.imshow("food image", image)

# this will only show and close the image hence we use waitkey for waiting after the image is shown

cv2.waitKey()
