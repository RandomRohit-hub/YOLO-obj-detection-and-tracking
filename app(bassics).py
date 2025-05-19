import cv2
import numpy as np
from object_detection import ObjectDetection


#load obj detection
od=ObjectDetection()

cap=cv2.VideoCapture('los_angeles.mp4')


#initialize count
count=0
center_point={}

while True:

    ret, frame=cap.read()
    count+=1
    center_point=[]
    if not ret:
        break


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
        center_point.append((centX,centY))

        print('FRAME NUMBER', count, " ", x, y, w, h)
        # cv2.circle(frame, (centX, centY), 5, (0, 0, 255), -1)

        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)  ## L,W,COLOR,THICK
     

    for pt in center_point:
        cv2.circle(frame, pt, 5, (0, 0, 255), -1) 

    cv2.imshow('Frame',frame)

    key=cv2.waitKey(0)
    if key==27:
        break

cap.release()
cv2.destroyAllWindows()






























