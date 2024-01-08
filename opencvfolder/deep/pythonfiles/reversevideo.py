import cv2

# instance of video camera
cap= cv2.VideoCapture('sample.webm')

# getting properties of video
frames= cap.get(cv2.CAP_PROP_FRAME_COUNT)
fps= cap.get(cv2.CAP_PROP_FPS)
height= cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width= cap.get(cv2.CAP_PROP_FRAME_WIDTH)

# Intializing the output writer for video
fourcc= cv2.VideoWriter_fourcc(*'MJPG')
out= cv2.VideoWriter('reversed_image',fourcc,fps,(int(width*0.5),int(height*0.5)))

print("No of frames : {}".format(frames))
print("fps : {}".format(fps))

# getting index of the last frame

frame_index=frames-1

# checking if the video instance is ready
if(cap.isOpened()):
    # reding till the end of video from last to the fist in reverse order
    while(frame_index!=0):
        cap.set(cv2.CAP_PROP_POS_FRAMES,frame_index)
        ret,frame=cap.read()

        # resizing the frame
        frame = cv2.resize(frame,(int(width*0.5),int(height*0.5)))

        # Writng the reversed video
        out.write(frame)
        # decrementing frame index at each step
        frame_index=frame_index-1  
        
        # printing the progress
        if(frame_index%100==0):
            print(frame_index)

out.release()
cap.release()
cv2.destroyAllWindows()