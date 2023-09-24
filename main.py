import os
import time
import json
from datetime import date, datetime
import zlib
import queue
import hashlib
import uuid

from dotenv import load_dotenv
import numpy as np

import cv2

img = cv2.imread('./temp/apk_niias_pts.png')
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(img.shape)

w = img.shape[1]
h = img.shape[0]
output_pts = np.float32([[0, 0], [w - 1, 0], [w - 1, h - 1], [0, h - 1]])

pt_A = (202,719)
pt_B = (562,400)
pt_C = (733,400)
pt_D = (1238,719)
input_pts = np.float32([pt_B, pt_C, pt_D, pt_A])
M = cv2.getPerspectiveTransform(input_pts,output_pts)


wnd_name = 'cvtest_wnd_1'
cv2.namedWindow(wnd_name, cv2.WINDOW_AUTOSIZE)
stream = cv2.VideoCapture('./temp/apk_niias.mp4')
time.sleep(1)
frame_width = int(stream.get(3))
frame_height = int(stream.get(4))
video_writer = cv2.VideoWriter('./temp/apk_niias_backperspective.mp4', 
                         cv2.VideoWriter_fourcc(*'XVID'), 10, (frame_width,frame_height))

counter = 0
while True:
    ret, frame = stream.read()
    if ret:
        counter += 1
        #print(frame.shape)
        #filter = cv2.blur(frame,(5,5))
        filtered = cv2.warpPerspective(frame, M,(w, h),flags=cv2.INTER_LINEAR)
        video_writer.write(filtered)
        cv2.imshow(wnd_name, filtered)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        if counter >= 1000:
            break
    else:
        break

stream.release()
video_writer.release()
