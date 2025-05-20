import cv2
import numpy as np
from object_detection import ObjectDetection
import math


#load obj detection
od=ObjectDetection()

cap=cv2.VideoCapture('los_angeles.mp4')


#initialize count
count=0

center_point_prev_frame=[]


tracking_obj={}
track_id=0

while True:

    ret, frame=cap.read()
    count+=1
    
    if not ret:
        break

# centre point in current frame
    center_point_curr_frame=[]


    # #detect obj on frame
    # (class_id,scores,boxes)=od.detect(frame)
    # for box in boxes:
    #     #print (box)
    #     (x,y,w,h)=box
    #     cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)  ## L,W,COLOR,THICK


      #detect & tracking obj on frame
    (class_id,scores,boxes)=od.detect(frame)
    for box in boxes:
        #print (box)
        (x,y,w,h)=box
        centX = int((x + x + w) / 2)
        centY = int((y + y + h) / 2)
        center_point_curr_frame.append((centX,centY))

        print('FRAME NUMBER', count, " ", x, y, w, h)
        # cv2.circle(frame, (centX, centY), 5, (0, 0, 255), -1)

        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)  ## L,W,COLOR,THICK


    for pt in center_point_curr_frame:
        for pt2 in center_point_prev_frame:
            distance=math.hypot(pt2[0]-pt[0],pt2[1]-pt[1])

            if distance<=10:
                tracking_obj[track_id]=pt
                track_id+=1


    print('TRACKING OBJ')
    print(tracking_obj)



    print('CUR FRAME')
    print(center_point_curr_frame)
    print('PREV FRAME')
    print(center_point_prev_frame)

    cv2.imshow('Frame',frame)

     # make a cpy of point
    center_point_prev_frame=center_point_curr_frame.copy()



    key=cv2.waitKey(0)
    if key==27:
        break

cap.release()
cv2.destroyAllWindows()






























