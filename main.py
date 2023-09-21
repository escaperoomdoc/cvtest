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

def go_blur(img_name):
    img = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)
    blur = cv2.blur(img,(5,5))
    cv2.imshow('blur', blur)
    cv2.waitKey(0)


def go_canny(img_name):
    img = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)
    canny = cv2.Canny(img,100,400)
    cv2.imshow('canny', canny)
    cv2.waitKey(0)

def go_filter_1(img_name):
    img = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)
    kernel = np.ones((5,5),np.float32)/25
    print(kernel)
    dst = cv2.filter2D(img,-1,kernel)
    cv2.imshow('go_filter_1', dst)
    cv2.waitKey(0)

webcam_canny_threshold1 = 100
webcam_canny_threshold2 = 200

def go_webcam():
    webcam = cv2.VideoCapture(0)
    while True:
        ret, frame = webcam.read()
        if ret:
            # filter = cv2.Canny(frame, webcam_canny_threshold1, webcam_canny_threshold2)
            filter = cv2.blur(frame,(webcam_canny_threshold1//10,webcam_canny_threshold2//10))
            cv2.imshow(wnd_name, filter)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break
    webcam.release()

def callback_function1(*args):
    global webcam_canny_threshold1
    webcam_canny_threshold1 = args[0]
    pass

def callback_function2(*args):
    global webcam_canny_threshold2
    webcam_canny_threshold2 = args[0]
    pass

cv2.createTrackbar('contours1', wnd_name, 100, 500, callback_function1)
cv2.createTrackbar('contours2', wnd_name, 200, 500, callback_function2)

# go_blur('./temp/pic_1.jpeg')
# go_canny('./temp/pic_rzd_1.png')
# go_filter_1('./temp/pic_rzd_1.png')
go_webcam()

