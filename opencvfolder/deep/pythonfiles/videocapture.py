import cv2

# imstance  of videocapture'
cap =cv2.VideoCapture(0)

opened= cap.isOpened()
# codec is the writing scheme for reading and writing videos
# opencv provides a 4 charecter codec known as 4cc 
# it mentions the coding scheme of the video

#  Here MJPEG is the 4 charecter code
fourcc=cv2.VideoWriter_fourcc(*'MJPG')

#properties

height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)

fps=cap.get(cv2.CAP_PROP_FPS)
 
#  now we need to initaite a video writer with a particular format in which we want to store the  video
out= cv2.VideoWriter('jj.avi',fourcc,fps,(int(width),int(height)))

print("frames are {}" .format(fps))



if(opened):
    while(cap.isOpened()):
        ret,frame= cap.read()
        if(ret == True):
            cv2.imshow("firstframe",frame)
            out.write(frame)
            if(cv2.waitKey(2)==27):
                break

out.release()
cap.release()
cv2.destroyAllWindows()
 