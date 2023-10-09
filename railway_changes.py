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

wnd_name = 'cvtest_wnd_1'
cv2.namedWindow(wnd_name, cv2.WINDOW_AUTOSIZE)

# https://yandex.ru/video/preview/8287708474737001929

with open('./temp/train_1.json', "r", encoding='utf-8') as f:
    sections = json.loads(f.read())

zones = []
for i in range(len(sections)):
    if i == 0: continue
    s = [sections[i-1], sections[i]]
    # s[1][0]    s[1][1]
    #  .  _______
    #    /      /
    #   /______/ .
    # s[0][0]  s[0][1]
    x = s[0][0][0]
    y = s[1][0][1]
    w = s[1][1][0] - s[0][0][0]
    h = s[0][0][1] - s[1][0][1]
    zones.append({
        'trap': [s[0][0], s[1][0], s[1][1], s[0][1]],
        'rect': [[x,y], [w, h]],
        'image': None,
        'stat': {
            'err': 0.0,
            'mse': 0.0
        }
    })



stream = cv2.VideoCapture('./temp/train_1.mp4')
frame_width = int(stream.get(3))
frame_height = int(stream.get(4))

counter = 0
x = 378
y = 398
w = 179
h = 104
while True:
    ret, frame = stream.read()
    if ret:
        counter += 1
        #if counter < 130:
        #    continue
        time.sleep(0.05)
        '''
        for zone in zones:
            trap = zone['trap']
            cv2.line(frame, trap[0], trap[1], (0,255,0), 2)
            cv2.line(frame, trap[1], trap[2], (0,255,0), 2)
            cv2.line(frame, trap[2], trap[3], (0,255,0), 2)
            cv2.line(frame, trap[3], trap[0], (0,255,0), 2)
        '''
        frame = cv2.blur(frame, (3,3))
        for zone in zones:
            rect = zone['rect']
            x, y = rect[0]
            w, h = rect[1]
            prev_img = zone['image']
            img = frame[y:y+h, x:x+w]
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            if prev_img is not None:
                h, w = img.shape
                diff = cv2.subtract(prev_img, img)
                err = np.sum(diff**2)
                mse = err/(float(h*w))
                zone['stat']['err'] = err
                zone['stat']['mse'] = int(mse * 10) / 10
            zone['image'] = img
            blue = int(min(zone["stat"]["mse"] / 30, 1) * 255)
            cv2.rectangle(frame, (x, y), (x+w,y+h), (blue,0,0), 2)
            cv2.putText(frame, 
                        f'{zone["stat"]["mse"]}', 
                        (x+w//2, y+h//2),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        (0, 255, 0),
                        1,
                        cv2.LINE_AA)
        cv2.imshow(wnd_name, frame)
        
    else:
        break
    print(counter, frame.shape)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

stream.release()
exit(0)
