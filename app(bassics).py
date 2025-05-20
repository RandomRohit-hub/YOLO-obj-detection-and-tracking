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





    #only at beginning we compare prev and current frame

    if count<=1:
        for pt in center_point_curr_frame:
            for pt2 in center_point_prev_frame:
                distance=math.hypot(pt2[0]-pt[0],pt2[1]-pt[1])

                if distance<=20:
                    tracking_obj[track_id]=pt
                    track_id+=1


    else:
        for pt2 in center_point_curr_frame:

           for pt2 in tracking_obj.items():
            
                distance=math.hypot(pt2[0]-pt[0],pt2[1]-pt[1])
                if distance<20:
                    tracking_obj[obj_id]=pt


    for obj_id, pt in tracking_obj.items():
     pt = tuple(map(int, pt))  # Ensure coordinates are integers
     cv2.circle(frame, pt, 5, (0, 0, 255), -1)
     cv2.putText(frame, str(obj_id), (pt[0], pt[1] - 7), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)



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






























